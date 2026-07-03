"""
Model Selection Page (리팩토링됨)
불필요한 래퍼 함수 제거, 새로운 컴포넌트 및 비즈니스 로직 구조 적용
"""

import streamlit as st
import asyncio
import time
import os
import sys
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 프로젝트 루트 경로 추가
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# MLflow (DagsHub) 실험 추적 초기화 - 설정 없으면 자동 비활성화
from src.utils.tracking import mlflow_tracker
mlflow_tracker.init_tracking()

# 새로운 컴포넌트들
from frontend.web.components.model_selection import ModelSelectionComponent
from frontend.web.components.theme_ui import ThemeUIComponent

# 리팩토링된 비즈니스 로직
from frontend.web.core.app_state import get_app_state_manager
from frontend.web.core.executor_manager import get_executor_manager
from frontend.web.core.model_manager import get_model_manager

# 유틸리티
from frontend.web.utils.constants import ICON, ICON_TEXT, COMPANY_LINK



# 전역 매니저들 초기화
app_state = get_app_state_manager()
executor_manager = get_executor_manager()
model_manager = get_model_manager()

# UI 컴포넌트들 초기화
theme_ui = ThemeUIComponent()
model_selection = ModelSelectionComponent()


def main():
    """모델 선택 페이지 메인"""
    
    # 페이지 설정 (직접 사용)
    st.set_page_config(
        page_title="Decepticon",
        page_icon=ICON,
        layout="wide",
    )
    
    # 테마 초기화
    current_theme = "dark" if st.session_state.get('dark_mode', True) else "light"
    theme_ui.apply_theme_css(current_theme)
    
    # 로고 표시 (직접 사용)
    st.logo(ICON_TEXT, icon_image=ICON, size="large", link=COMPANY_LINK)
    
    # 현재 상태 확인
    if st.session_state.get("initialization_in_progress", False):
        _handle_initialization_state()
        return
    
    # 모델이 이미 선택되어 있고 준비된 경우
    elif st.session_state.get("current_model") and st.session_state.get("executor_ready", False):
        st.switch_page("pages/01_Chat.py")
        return
    
    # 모델 선택되었지만 초기화 안된 경우
    elif st.session_state.get("current_model") and not st.session_state.get("executor_ready", False):
        st.session_state.initialization_in_progress = True
        st.rerun()
        return
    
    # 모델 선택 UI 표시
    else:
        _display_model_selection()


def _handle_initialization_state():
    """초기화 상태 처리"""
    model = st.session_state.get("current_model")
    if not model:
        st.session_state.initialization_in_progress = False
        st.rerun()
        return
    
    # 기존 코드처럼 placeholder.container() 구조 사용
    placeholder = st.empty()
    
    with placeholder.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # 실제 초기화 수행 (container 내부에서)
            _perform_model_initialization_in_container(model)


def _perform_model_initialization_in_container(model_info):
    """모델 초기화 수행 (container 내부에서 직접 수행)"""
    try:
        with st.spinner(f"Initializing {model_info.get('display_name', 'Model')}..."):
            success = asyncio.run(executor_manager.initialize_with_model(model_info))
        
        if success:
            st.session_state.executor_ready = True
            st.success(f"✅ {model_info.get('display_name', 'Model')} initialized successfully!")
            time.sleep(1.0)
            st.switch_page("pages/01_Chat.py")
        else:
            error_msg = st.session_state.get("initialization_error", "Unknown error")
            st.error(f"❌ Initialization failed: {error_msg}")
            
            # 재시도 버튼
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Retry", use_container_width=True):
                    st.rerun()
            with col2:
                if st.button("⬅️ Back", use_container_width=True):
                    st.session_state.current_model = None
                    st.session_state.initialization_in_progress = False
                    st.rerun()
    except Exception as e:
        st.error(f"❌ Initialization error: {str(e)}")
        
        # 재시도 버튼
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retry", use_container_width=True):
                st.rerun()
        with col2:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.current_model = None
                st.session_state.initialization_in_progress = False
                st.rerun()
    finally:
        st.session_state.initialization_in_progress = False



def _display_model_selection():
    """모델 선택 UI 표시"""
    placeholder = st.empty()
    
    with placeholder.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # 모델 데이터 로드
            models_result = model_manager.get_cached_models_data()
            
            if not models_result["success"]:
                _handle_models_loading_error(models_result)
                return
            
            # 성공/Ollama 메시지 표시
            if models_result["type"] == "success" and "ollama_message" in models_result:
                model_selection.display_provider_status(models_result)
            
            # 기본 선택값 가져오기
            default_provider, default_model = model_manager.get_default_selection()
            
            # 콜백 함수들 정의
            callbacks = {
                "on_model_change": _reset_model_selection,
                "get_export_data": lambda session_id: None  # 모델 선택에서는 사용 안함
            }
            
            # 모델 선택 UI 렌더링
            selected_model = model_selection.render_complete_selection_ui(
                providers_data=models_result["models_by_provider"],
                current_model=st.session_state.get("current_model"),
                default_provider=default_provider,
                default_model=default_model,
                callbacks=callbacks
            )
            
            if selected_model:
                _handle_model_selection(selected_model)


def _handle_models_loading_error(models_result):
    """모델 로딩 에러 처리"""
    if models_result["type"] == "import_error":
        model_selection.display_error_state(
            models_result["error"],
            models_result.get("info")
        )
    else:
        model_selection.display_error_state(models_result["error"])


def _handle_model_selection(selected_model):
    """모델 선택 처리"""
    # 모델 정보 검증
    preparation_result = model_manager.prepare_model_initialization(selected_model)
    
    if not preparation_result["ready"]:
        st.error(f"Model validation failed: {', '.join(preparation_result['errors'])}")
        return
    
    # 모델 설정 및 초기화 시작
    st.session_state.current_model = selected_model
    st.session_state.initialization_in_progress = True
    st.rerun()


def _reset_model_selection():
    """모델 선택 리셋"""
    # 모델 관련 상태 초기화
    st.session_state.current_model = None
    st.session_state.executor_ready = False
    st.session_state.initialization_in_progress = False
    st.session_state.initialization_error = None
    
    # 실행기 리셋
    executor_manager.reset()
    
    # 모델 캐시 리셋 (필요한 경우)
    # model_manager.reset_cache()
    
    st.rerun()


if __name__ == "__main__":
    main()