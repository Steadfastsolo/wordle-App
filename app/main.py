from fastapi import FastAPI
from app.services.wordService import load_words, get_daily_word

app = FastAPI()

WORDS = load_words()

@app.get("/")
def root():
    return {"message": "Wordle API running"}

@app.get("/daily-word")
def daily_word():
    return {
        "word": get_daily_word(WORDS)
    }


