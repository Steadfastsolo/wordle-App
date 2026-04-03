from datetime import date
from pathlib import Path


# Cache the solution word list so it only loads once
_WORDS: list[str] | None = None


def loadWords() -> list[str]:
    
    # Load and return all valid 5-letter words.
    
    global _WORDS
    if _WORDS is not None:
        return _WORDS

    words_path = Path(__file__).resolve().parents[2] / "words" / "solutions.txt"

    with open(words_path, "r") as f:
        words = [
            line.strip().lower()
            for line in f
            if line.strip().isalpha() and len(line.strip()) == 5
        ]

    if not words:
        raise RuntimeError("No valid 5-letter words found")

    _WORDS = words
    return words

def getDailyWord() -> str:
    words = loadWords()
    index = date.today().toordinal() % len(words)
    return words[index]


# Cache the allowed word list so it only loads once
_ALLOWED_WORDS: set[str] | None = None


def loadAllowedWords() -> set[str]:
    global _ALLOWED_WORDS
    if _ALLOWED_WORDS is not None:
        return _ALLOWED_WORDS

    path = Path(__file__).resolve().parents[2] / "words" / "allowed.txt"

    with open(path, "r") as f:
        words = {
            line.strip().lower()
            for line in f
            if line.strip().isalpha() and len(line.strip()) == 5
        }

    _ALLOWED_WORDS = words
    return words


def isValidWord(word: str) -> bool:
    words = loadAllowedWords()
    return word.lower() in words