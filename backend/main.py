from fastapi import FastAPI, Request, Query
from services.openrouter_api import get_word_card, get_quiz, check_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许跨域，便于本地小程序/前端调试
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_word_card")
async def word_card(word: str = Query(None), model: str = Query("qwen2.5")):
    return await get_word_card(word, model)

@app.get("/get_quiz")
async def quiz(word: str = Query(...), model: str = Query("qwen2.5")):
    return await get_quiz(word, model)

@app.post("/check_answer")
async def check(request: Request):
    data = await request.json()
    user_answer = data.get("user_answer")
    correct_answer = data.get("correct_answer")
    return await check_answer(user_answer, correct_answer) 