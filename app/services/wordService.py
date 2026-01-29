from datetime import date
from pathlib import Path


# Cache the word list so it only loads once
_WORDS: list[str] | None = None


def _load_words() -> list[str]:
    
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
    words = _load_words()
    index = date.today().toordinal() % len(words)
    return words[index]