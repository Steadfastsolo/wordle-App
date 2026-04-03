from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from app.services.wordService import loadWords, getDailyWord, isValidWord
from app.services.gameLogic import Game

app = FastAPI()
game = None  # global game instance

WORDS = loadWords()

@app.get("/")
def root():
    return {"message": "Wordle API running"}

@app.get("/daily-word")
def daily_word():
    return {
        "word": getDailyWord(WORDS)
    }

@app.post("/start")
def start_game():
    global game
    word = getDailyWord()
    game = Game(word)

    return {
        "message": "Game started",
        "attemptsLeft": game.numAttempts
    }

class GuessRequest(BaseModel):
    guess: str

@app.post("/guess")
def make_guess(request: GuessRequest):
    global game

    # makes sure the game was initialized with the word of the day
    if game is None:
        raise HTTPException(status_code=400, detail="Game not started")

    try:
        result = game.guess(request.guess)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    isWin = result == ["green"] * 5
    isGameOver = isWin or game.numAttempts == 0

    return {
        "result": result,
        "attemptsLeft": game.numAttempts,
        "isWin": isWin,
        "isGameOver": isGameOver
    }

@app.get("/state")
def get_state():
    global game

    if game is None:
        raise HTTPException(status_code=400, detail="Game not started")

    return {
        "attemptsLeft": game.numAttempts
    }

@app.post("/validate-guess")
def validate_guess(request: GuessRequest):
    guess = request.guess.lower()

    if len(guess) != 5:
        return {"valid": False, "reason": "Must be 5 letters"}

    if not guess.isalpha():
        return {"valid": False, "reason": "Must be alphabetic"}

    if not isValidWord(guess):
        return {"valid": False, "reason": "Word not in dictionary"}

    return {"valid": True}
