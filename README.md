[![English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge)](README.md)
[![한국어](https://img.shields.io/badge/Language-한국어-red?style=for-the-badge)](./docs/README_KO.md)

---

> ## 📣 **Attribution & Fork Notice**
> 
> This repository is a **fork/learning implementation** based on [**Decepticon**](https://github.com/PurpleAILAB/Decepticon) by [**PurpleAILAB**](https://github.com/PurpleAILAB).
> 
> **Original Project:** https://github.com/PurpleAILAB/Decepticon  
> **License:** [Apache-2.0](LICENSE)  
> **All credit** for the original concept, architecture, and core implementation goes to the PurpleAILAB team.
>
> ### 🎓 My Learning Journey
> 
> This fork was created for **educational purposes** to deeply understand modern AI-driven security frameworks. Through studying and experimenting with this project, I gained invaluable knowledge in:
>
> #### **🤖 AI & LLM Integration**
> - **LangChain/LangGraph Framework**: Understanding state machines, graph-based agent orchestration, and workflow management
> - **Multi-Agent Systems**: Learned how autonomous agents communicate, handoff tasks, and collaborate towards a common goal
> - **ReAct Pattern**: Explored Reasoning + Acting paradigm for building intelligent decision-making agents
> - **Prompt Engineering**: Crafted and optimized system prompts for specialized security agents (Reconnaissance, Initial Access, Planner, Summary)
> - **Model Context Protocol (MCP)**: Integrating external tools and APIs into agent workflows using stdio and HTTP transports
> - **LLM Provider Integration**: Working with OpenAI, Anthropic, OpenRouter, and local models via Ollama
>
> #### **🔴 Offensive Security & Red Teaming**
> - **Penetration Testing Automation**: How AI agents can autonomously conduct reconnaissance, exploitation, and post-exploitation
> - **MITRE ATT&CK Framework**: Mapping agent behaviors to real-world tactics, techniques, and procedures
> - **Network Reconnaissance**: Automated service enumeration, vulnerability scanning, and target profiling
> - **Credential Attacks**: Understanding brute-force, password spraying, and credential stuffing techniques
> - **Exploit Development Workflow**: From vulnerability discovery to exploitation in an agent-driven context
> - **Docker-based Attack Infrastructure**: Setting up isolated Kali Linux environments for safe testing
>
> #### **🏗️ Software Architecture & Design Patterns**
> - **State Management**: Using LangGraph's state system to maintain context across agent interactions
> - **Modular Tool Design**: Building reusable, composable security tools following MCP standards
> - **Agent Handoff Patterns**: Designing seamless transitions between specialized agents (Planner → Recon → InitAccess → Summary)
> - **Swarm vs Supervisor Architecture**: Comparing decentralized peer-to-peer vs centralized orchestration patterns
> - **Error Handling & Resilience**: Building robust agents that gracefully handle failures and unexpected scenarios
> - **Logging & Replay Systems**: Implementing comprehensive activity logging for debugging, auditing, and knowledge sharing
>
> #### **💻 Full-Stack Development**
> - **Streamlit Web Framework**: Building interactive, real-time web UIs for agent monitoring and control
> - **CLI Development**: Creating powerful command-line interfaces for automated workflows
> - **Terminal UI Components**: Real-time output streaming, syntax highlighting, and interactive terminals
> - **Theme System**: Implementing dark/light mode with CSS customization
> - **Chat History & Replay**: Building temporal replay systems to review past agent interactions
> - **Model Selection UI**: Dynamic switching between different LLM providers and configurations
>
> #### **🐳 DevOps & Infrastructure**
> - **Docker & Docker Compose**: Containerizing attack infrastructure and target environments
> - **Python Dependency Management**: Using `uv` for fast, modern Python package management
> - **Environment Configuration**: Managing API keys, secrets, and configurations via `.env` files
> - **Langsmith Integration**: Tracing, monitoring, and debugging LLM-powered applications
> - **Cross-platform Scripting**: Writing portable scripts for Windows (PowerShell) and Unix (Bash)
>
> #### **🔬 Research & Experimentation**
> - **Agentic Workflow Design**: Experimenting with different agent communication patterns and decision trees
> - **Tool Integration**: Connecting security tools (nmap, hydra, metasploit) to AI agents via MCP
> - **Persona Development**: Creating specialized agent personalities for different red team roles
> - **Memory & Context Windows**: Understanding token limits and context management in long-running operations
> - **Chain-of-Thought Reasoning**: Studying how agents break down complex security tasks into manageable steps
>
> #### **📚 Best Practices I Learned**
> - The importance of **ethical hacking boundaries** and proper authorization
> - How to structure **reproducible security research** through comprehensive logging
> - The value of **open-source collaboration** in advancing security tools
> - Why **transparent AI systems** matter in security contexts (explainability, auditability)
> - The critical role of **continuous learning** in both AI and cybersecurity fields
>
> ---
>
> **🙏 Acknowledgment:**  
> Massive thanks to the **PurpleAILAB team** for building such a comprehensive, well-architected, and educational project. This repository represents countless hours of research, development, and community contribution. If you're interested in the **original, actively maintained version** with the latest features and updates, please visit the [official PurpleAILAB/Decepticon repository](https://github.com/PurpleAILAB/Decepticon).
>
> **⭐ Please star the original project** if you find this technology valuable!

---

<div align="center">
  <img src="assets/logo_banner.png" alt="Decepticon Logo">
</div>

<h1 align="center"> Decepticon - Vibe Hacking Agent</h1>

<div align="center">


<!-- GitHub License -->
<a href="https://github.com/PurpleAILAB/Decepticon/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/PurpleAILAB/Decepticon?style=for-the-badge&color=blue" alt="License: Apache 2.0">
</a>

<!-- GitHub Stars -->
<a href="https://github.com/PurpleAILAB/Decepticon/stargazers">
  <img src="https://img.shields.io/github/stars/PurpleAILAB/Decepticon?style=for-the-badge&color=yellow" alt="Stargazers">
</a>

<!-- GitHub Contributors -->
<a href="https://github.com/PurpleAILAB/Decepticon/graphs/contributors">
  <img src="https://img.shields.io/github/contributors/PurpleAILAB/Decepticon?style=for-the-badge&color=orange" alt="Contributors">
</a>

<br/>

<!-- Discord -->
<a href="https://discord.gg/TZUYsZgrRG">
  <img src="https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white&style=for-the-badge" alt="Join us on Discord">
</a>

<!-- Website -->
<a href="https://purplelab.framer.ai">
  <img src="https://img.shields.io/badge/Visit%20Website-brightgreen?logo=vercel&logoColor=white&style=for-the-badge" alt="Visit Website">
</a>
</div>

<div align="center">
<!-- Logo Image -->
<!-- <img src="assets/decepticon_logo.png" alt="Decepticon Logo" width="256" height="256" /> -->

https://github.com/user-attachments/assets/92e1dffd-92af-4d63-b682-c4a1810586a9

<br>

[CLI Demo](.github/cli.gif)

</div>

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

- [💡 Community Contribution ](#-community-contribution)
- [💡 What is Vibe Hacking ?](#-what-is-vibe-hacking-)
- [💡 Why Decepticon?](#-why-decepticon)
- [Quick Start](#-quick-start)
- [Key features](#key-features)
  - [Agents](#-agents)
    - [🔴 Red Team Agents](#-red-team-agents)
    - [🔵 Utility Agents](#-utility-agents)
  - [Multi-Agent-System Architecture](#multi-agent-system-architecture)
  - [Replay](#replay)
- [Installation](#-installation)
- [Advanced AI Models](#-advanced-ai-models)
  - [☁️ Cloud Models](#️-cloud-models)
  - [🏠 Local Models (Ollama)](#-local-models-ollama)
- [MCP Support](#-mcp-support)
  - [Supported MCP Transports](#-supported-mcp-transports)
  - [`mcp_config.json` Structure](#-mcp_configjson-structure)
  - [Example](#-example)
- [⚠️ Experimental Technology Disclaimer](#️-experimental-technology-disclaimer)
- [🤝 Contributing](#-contribution)
  - [What You Can Contribute](#-what-you-can-contribute)
    - [Migrate Security Tools to MCP Format](#-migrate-security-tools-to-mcp-format)
    - [Develop ReAct-style Red Team Agents](#-develop-react-style-red-team-agents)
    - [Architect Multi-Agent Flows](#-architect-multi-agent-flows)
  - [How to Contribute](#-how-to-contribute)
- [Join the Community](#-join-the-community)
- [📝 License](#-license)

</details>

---

> ## ⚠️ Disclaimer
> Do not attempt to use this project on any system or network without explicit authorization.
> You are solely responsible for your actions.

> ## 💡 **Community Contribution**
> If you have interesting penetration testing scenarios, export your **logs** and share them with the community through PR! 
> Your experiences will greatly help other users in their learning journey.
> Please refer to the Replay section for more details.

<div align="center">

![replay](.github/replay.gif)

</div>

## 💡 What is **Vibe Hacking** ?

**Vibe Hacking** is a new paradigm in Offensive Security defined by PurpleAILAB.  

Unlike traditional red teaming methods that rely on manual execution, **AI agents autonomously perform red teaming tasks** in Vibe Hacking.

> ### *The Best Defense is a Good Offense.*

## 💡 Why **Decepticon**?

As agents become more sophisticated, attackers evolve accordingly.  
From AI-driven phishing to self-learning malware, offensive techniques are becoming increasingly automated and intelligent.

To effectively defend against AI-powered threats, **we must act faster**—and **we must act first**.  
**Decepticon** is designed for that very purpose: using AI agents to automate red teaming **before attackers automate theirs.**

Built on the robust foundation of **LangChain/LangGraph**, Decepticon grows alongside the thriving AI agent ecosystem. By leveraging the same cutting-edge frameworks that power the future of AI, we ensure compatibility, scalability, and continuous innovation through community collaboration.

Delegate repetitive and manual tasks to agents, and focus on intuition and decision-making to fulfill the true essence of a **CyberSecurity Supervisor**.

> ### *Prepare before AI Hacks First.*


## Quick Start

### 1. Set up the environment with
```bash
uv venv
uv sync
or
uv pip install -e .
```

### 2. Copy environment file 
```bash
cp .env.example .env
```

### 3. Docker (10m ~ 20m)
```bash
docker-compose up -d --build
```

### 4. Run MCP servers
#### Option 1: Use provided scripts
- On Windows:
```bash
./run_mcp.ps1
```
- On macOS/Linux:
```bash
./run_mcp.sh
```

#### Option 2: Run manually
```bash
python src/tools/mcp/(your mcp server).py
```

### 4. Run CLI or Web interface
```bash
python frontend/cli/cli.py
streamlit run frontend/streamlit_app.py
```


## Key features

### Agents

#### 🔴 Red Team Agents
- **Reconnaissance Agent**: Network scanning, service enumeration, vulnerability discovery
- **Initial Access Agent**: Exploitation, credential attacks, system compromise
- **Privilege Escalation Agent**(Planned): Rights elevation and lateral movement
- **Defense Evasion Agent**(Planned): Anti-detection and stealth techniques
- **Persistence Agent**(Planned): Maintaining access and backdoor installation
- **Execution Agent**(Planned): Command execution and payload deployment

#### 🔵 Utility Agents 
- **Planner Agent**: Strategic brain coordinating the entire operation
- **Summary Agent**: Analysis compilation, reporting, and documentation
- **Supervisor Agent**(Planned): Workflow orchestration and decision routing


### Multi-Agent-System Architecture

**Flexible Architecture Options:**
- **Swarm Architecture**: Direct peer-to-peer agent communication and collaboration
- **Supervisor Architecture**(Planned): Centralized control with supervisor-managed workflows
- **Hybrid Architecture**(Planned): Combined approach with both direct communication and centralized oversight
- **your custom Architecture**


### Replay

The Replay feature is implemented to maximize collaboration and knowledge sharing within Decepticon's open-source community.
Please share your usage methods and execution results through PRs!

1. **Execution results are saved** under the `logs/` folder
2. **Replay functionality**: Click the Chat History button to replay JSON-formatted logs stored under the `logs/` folder  
3. **Community sharing**: Use the export feature to share with the community!


## Installation

### 1. **Clone the repository**
```bash
git clone https://github.com/PurpleCHOIms/Decepticon.git
cd Decepticon
```

### 2. **Install dependencies** 
**UV (Recommended)**
```bash
# Create virtual environment
uv venv
# Install dependencies
uv pip install -e .
```

### 3. environment file .env

```bash
# Create environment file
cp .env.example .env
```

```bash
# Configure API Keys

# LLM API
OPENAI_API_KEY=your-api-key
ANTHROPIC_API_KEY=your-api-key
OPENROUTER_API_KEY=your-api-key

# Langsmith
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY=your-api-key
LANGSMITH_PROJECT=Decepticon
LANGGRAPH_API_URL=http://127.0.0.1:2024
```

### 4. Docker Setup

```bash
# Start Kali Linux container with target
docker-compose up -d
```

### 5. Run MCP Server
```bash
python src/tools/mcp/(your mcp server).py
```

### 6. CLI 
```bash
# Run CLI
python frontend/cli/cli.py
```

### 7. Web Interface

```bash
# Run web interface
streamlit run frontend/web/streamlit_app.py
```

## Advanced AI Models

### ☁️ Cloud Models
- **OpenAI**: 4.1, 4o, 4o Mini, o4 Mini, o3 Mini, o1 Mini, o1, o3
- **Anthropic**: Sonnet 4, Opus 4, Sonnet 3.7, Sonnet 3.5, Haiku 3.5, 

### 🏠 Local Models (Ollama)
- your installed Models


## MCP Support

This project supports loading tools via the [LangGraph MCP Adapter](https://github.com/langchain-ai/langchain-mcp-adapters).

You can define your MCP tools in a configuration file called `mcp_config.json`.  
Tools are grouped by **agent names**, and each agent can have multiple MCP servers.

### Supported MCP Transports

- `stdio` - Standard input/output communication
- `streamable_http` - HTTP-based streaming communication

### `mcp_config.json` Structure

```json
{
  "agent_name": {
    "mcp_server_1": {
      "command": "python",
      "args": ["./path/to/script.py"],
      "transport": "stdio"
    },
    "another_mcp_server_streamable_HTTP": {
      "url": "mcp-url"
    }
  }
}
```

### Example

```json
{
  "reconnaissance": {
    "reconnaissance": {
      "command": "python",
      "args": ["./src/tools/mcp/Reconnaissance.py"],
      "transport": "stdio"
    },
    "desktop_commander": {
      "url": "https://server.smithery.ai/@wonderwhy-er/desktop-commander/mcp?api_key=your-api-key"
    }
  },
  "initial_access": {
    "initial_access": {
      "command": "python",
      "args": ["./src/tools/mcp/Initial_Access.py"],
      "transport": "stdio"
    }
  }
}
```

**To add a new MCP tool:**
1. Create your MCP tool script under `src/tools/mcp/`
2. Add the corresponding entry in `mcp_config.json`
3. Restart the application to load the new tool


## ⚠️ Experimental Technology Disclaimer

**Decepticon** is an experimental project currently under active development. It is not yet stable and may contain bugs, incomplete features, or undergo breaking changes.

We're building this project openly with the community and warmly welcome:

- Bug reports  
- Feature requests  
- Pull requests  
- Good vibes  

Help us make Decepticon better by filing issues or submitting PRs (see the section below for how to contribute)!


## 🤝 Contribution

We welcome contributions from the community to make this project better, more powerful, and more secure.  
Whether you're an experienced developer, a security researcher, or just getting started in open-source, there are many ways to get involved.

### What You Can Contribute

#### 1. Migrate Security Tools to MCP Format

Help transform existing security tools into modular, LangGraph-compatible **MCP (Modular Command Protocol) tools**.

- Wrap tools using the standard MCP interface (`stdio` or `streamable_http`)
- Ensure compatibility with `langgraph-mcp-adapter`
- Place them under the `src/tools/mcp/`

#### 2. Develop ReAct-style Red Team Agents

Design and refine ReAct-style agents for Red Team operations:

- Reconnaissance  
- Initial Access  
- Privilege Escalation  
- Persistence and more

Contribute by:

- Creating tailored prompts under `src/prompts/`
- Implementing new agents with specific capabilities
- Improving task planning and memory usage

#### 3. Architect Multi-Agent Flows

Contribute to the design and optimization of the multi-agent orchestration layer:

- Propose new workflows or agent roles
- Improve inter-agent communication and handoffs
- Extend state-driven logic using LangGraph

### How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes with clear messages
4. Push to your branch and open a **Pull Request**
5. Link the related issue (if any) and explain your solution

We encourage clean, well-tested code with documentation.  
Feel free to open issues to discuss ideas before jumping into a PR!

## Join the Community

Join our [Discord](https://discord.gg/XGytzHZU) to connect with other developers, share ideas, ask questions, and collaborate on building the future of AI-powered red teaming!

Whether you're looking for help with contributions, want to discuss new features, or just want to chat about cybersecurity and AI, our community is here to support you.



## 📝 License

This repository is licensed under the [Apache-2.0 License](LICENSE).

---

![main](./assets/main.png)
