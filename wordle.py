import random

wordsList= ['canada','grape', 'doctor','bingo','create','could']

class WordleGame:
    def __init__(self):
        self.word= random.choice(wordsList)
        self.wordLength=len(self.word)
        self.maxAttempts=10
        self.attempts=0
        self.isOver = False
        self.isWon = False
    
    #Check if the letter is in the correct spot it is green, wrong spot correct letter yellow and wrong eveyrthing grey
    def checkGuess(self, guess):
        result=[]
        for i in range(self.wordLength):
            if guess[i]==self.word[i]:
                result.append((guess[i],'green'))
            elif guess[i] in self.word:
                result.append((guess[i],'yellow'))
            else:
                result.append((guess[i], 'gray'))
       
        self.attempts+=1
        
        if guess==self.word:
            self.isWon = True
            self.isOver = True
        elif self.attempts >= self.maxAttempts:
            self.isOver = True

        return result