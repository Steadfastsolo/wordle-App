
class Game:

    numAttempts = 0
    wordArray = None
    greenArray = None
    yellowArray = None
    
    # Method for starting the game by setting the amount of attempts and wordArray
    def __init__(self, word: str):
        # Makes sure game is not initialized with empty word
        if(word == None):
            raise ValueError("Word can not be none")

        # make sure word has exactly 5 characters 
        if(len(word) != 5):
            raise ValueError("Guessed Word must be 5 letters!")
        
        # make sure word has only alphabet characters
        if(word.isalpha() != True):
            raise ValueError("Guess must contain only letters!")

        self.wordArray = list(word)
        self.numAttempts = 6
        self.greenArray = []
        self.yellowArray = []

    # Method for returning greenArray
    def getGreenArray(self):
        print("Green Array:")
        print(self.greenArray)
        return self.greenArray

    # Method for returning yellowArray
    def getYellowArray(self):
        print("Yellow Array:")
        print(self.yellowArray)
        return self.yellowArray

    # Method for geussing the word. Checks to see if the user still has attempts remaining.
    def guess(self, guessWord: str):

        # INPUT VALIDATION
        # make sure user still has attempts
        if(self.numAttempts == 0):
            print("No Attempts Left!")
            raise ValueError("No Attempts Remaining!")
        
        # make sure the guessWord has exactly 5 characters 
        if(len(guessWord) != 5):
            raise ValueError("Guessed Word must be 5 letters!")
        
        # make sure the guessWord has only alphabet characters
        if(guessWord.isalpha() != True):
            raise ValueError("Guess must contain only letters!")

        # GAME LOGIC
        # temp array to store the letters from the wordArray
        tempArray = self.wordArray.copy()

        # result array to return the status of the letters (green, yellow, gray)
        resultArray = ["gray","gray","gray","gray","gray"]

        # turns the guess into a list of characters
        guessArray = list(guessWord)

        # first pass to see if any letters are in the right position.
        for i in range(len(guessArray)):
            if (guessArray[i] == tempArray[i]):
                resultArray[i] = "green"
                # removes letters that are in the correct posistion from the temp array
                tempArray[i] = None
                # if the correct letter is guessed for the first time, add it to the greenArray
                if (self.greenArray.count(guessArray[i]) == 0):
                    self.greenArray.append(guessArray[i]) 
            
        # second pass to see if any letters are in the word but at the wrong position
        for i in range(len(guessArray)):
            if (guessArray[i] in tempArray):
                resultArray[i] = "yellow"
                # if the letter is guessed for the first time, add it to the yellowArray
                if (self.yellowArray.count(guessArray[i]) == 0):
                    self.yellowArray.append(guessArray[i])

        # remove one attempt from the counter
        self.numAttempts = self.numAttempts - 1

        # print resultArray, greenArray, yellowArray for bug testing 
        print("\nResult Array:")
        print(resultArray)
        print("Green Array:")
        print(self.greenArray)
        print("Yellow Array:")
        print(self.yellowArray)

        # return resultArray
        return resultArray 

                
            



            


