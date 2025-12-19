import pytest
from app.services.gameLogic import Game

# tests if the game can be initialized correctly
def testInitialize():
    game = Game("place")
    assert game.numAttempts == 6
    assert game.wordArray == ["p", "l", "a", "c", "e"]

# tests invalid game initilization with not 5 characters
def testInvalidInitFiveCharacters():
    with pytest.raises(ValueError):
        game = Game("placeeeeeeeee")
    with pytest.raises(ValueError):
        game = Game("pl")

# tests invalid game initilization with not alphabetical characters
def testInvalidInitAlpha():
    with pytest.raises(ValueError):
        game = Game("pl#ce")

# tests invalid game initilization with empty word
def testInvalidInitEmpty():
    with pytest.raises(ValueError):
        game = Game("")

# tests valid guess
def testValidGuess():
    game = Game("place")
    result = game.guess("crane")

    assert isinstance(result, list)
    assert len(result) == 5
    assert game.numAttempts == 5

# tests invalid guess after 6 attempts
def testSevenAttempts():
    game = Game("place")
    for i in range(6):
        result = game.guess("crane")
    with pytest.raises(ValueError):
        game.guess("crane")

# tests invalid guess with not alphabetical characters
def testAlpha():
    game = Game("place")
    with pytest.raises(ValueError):
        game.guess("He$%o")

# tests invalid guess with not 5 characters
def testGuessLen():
    game = Game("place")
    with pytest.raises(ValueError):
        game.guess("Hellllo")

# test getGreenArray function
def testGetGreen():
    game = Game("place")
    result = game.guess("crane")
    greenArray = game.getGreenArray() 
    assert greenArray == ["a","e"]
    result = game.guess("plate")
    greenArray = game.getGreenArray() 
    assert greenArray == ["a","e","p","l"]

# test getYellowArray function
def testGetYellowArray():
    game = Game("place")
    result = game.guess("angry")
    yellowArray = game.getYellowArray() 
    assert yellowArray == ["a"]
    result = game.guess("rates")
    yellowArray = game.getYellowArray() 
    assert yellowArray == ["a","e"]
    result = game.guess("plate")
    yellowArray = game.getYellowArray() 
    assert yellowArray == ["a","e"]

# test win
def testWin():
    game = Game("place")
    result = game.guess("place")
    assert result == ["green","green","green","green","green"]











