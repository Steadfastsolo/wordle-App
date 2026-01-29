import pytest
from app.services.wordService import getDailyWord

# tests to make sure the daily word given will be the same 
def testDailyWordService():
    word1 = getDailyWord()
    word2 = getDailyWord()
    assert word1 == word2
