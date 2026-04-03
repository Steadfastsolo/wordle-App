import pytest
from fastapi.testclient import TestClient
from app import main
from app.main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_game():
    main.game = None

# this tests the server is up and running 
def testRoot():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wordle API running"}

# this tests the actual game itself has initialized 
def testStartGame():
    response = client.post("/start")

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Game started"
    assert data["attemptsLeft"] == 6

# this tests the guess endpoint and makes sure the game is updating correctly 
def testGuessFlow():
    client.post("/start")

    response = client.post("/guess", json={"guess": "crane"})

    assert response.status_code == 200
    data = response.json()

    assert "result" in data
    assert len(data["result"]) == 5
    assert data["attemptsLeft"] == 5

# this test makes sure the player can not somehow start before the game has initialized 
def testGuessWithoutStart():
    response = client.post("/guess", json={"guess": "crane"})
    print(response.json())

    assert response.status_code == 400
    assert response.json()["detail"] == "Game not started"

# this test checks if the game counts valid guesses as actually valid guesses  
def testValidateGuessValid():
    response = client.post("/validate-guess", json={"guess": "crane"})

    assert response.status_code == 200
    assert "valid" in response.json()

# this test checks if the game counts invalid guesses as actually invalid guesses
def testValidateGuessInvalid():
    response = client.post("/validate-guess", json={"guess": "123!!"})

    assert response.status_code == 200
    assert response.json()["valid"] is False