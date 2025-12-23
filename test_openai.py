from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # 👈 THIS is the missing piece

client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(resp.choices[0].message.content)
