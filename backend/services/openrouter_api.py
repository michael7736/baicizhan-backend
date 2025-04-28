import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# 支持的模型
MODEL_MAP = {
    "qwen2.5": "qwen2.5-72b-chat",
    "deepseek": "deepseek-chat-v3-32k"
}

async def call_openrouter(prompt, model="qwen2.5"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_MAP.get(model, MODEL_MAP["qwen2.5"]),
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

async def get_word_card(word=None, model="qwen2.5"):
    # 如果没有指定单词，可以让大模型随机出一个常见单词
    if word is None:
        prompt = "请随机给我一个常见的英语单词，返回格式为：单词|中文释义|英文例句。"
        result = await call_openrouter(prompt, model)
        try:
            word, definition, example = result.strip().split("|")
        except Exception:
            word, definition, example = "apple", "苹果", "I eat an apple."
    else:
        prompt = f"请给出单词 {word} 的中文释义和一个英文例句，返回格式为：{word}|中文释义|英文例句。"
        result = await call_openrouter(prompt, model)
        try:
            _, definition, example = result.strip().split("|")
        except Exception:
            definition, example = "苹果", "I eat an apple."
    return {"word": word, "definition": definition, "example": example}

async def get_quiz(word, model="qwen2.5"):
    prompt = f"请为单词 {word} 生成一个四选一英文选择题，题干用英文，四个选项用中文，正确答案必须是{word}的中文释义，返回格式为：题干|选项A|选项B|选项C|选项D|正确答案（A/B/C/D）|正确答案内容。"
    result = await call_openrouter(prompt, model)
    try:
        parts = result.strip().split("|")
        question = parts[0]
        options = parts[1:5]
        answer_letter = parts[5]
        answer_content = parts[6]
    except Exception:
        question = f"What is the meaning of '{word}'?"
        options = ["苹果", "香蕉", "橙子", "葡萄"]
        answer_letter = "A"
        answer_content = "苹果"
    return {
        "question": question,
        "options": options,
        "answer_letter": answer_letter,
        "answer_content": answer_content
    }

async def check_answer(user_answer, correct_answer):
    # 本地比对
    return {"correct": user_answer == correct_answer} 