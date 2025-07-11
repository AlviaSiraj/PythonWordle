import random

wordsList= [ 'apple', 'brave', 'candy', 'dance', 'eagle',
    'flame', 'grape', 'honey', 'action', 'juice',
     'koala', 'lemon', 'mango', 'novel', 'ocean',
    'pearl', 'bring', 'radio', 'snail', 'tiger',
    'umbra', 'viola', 'wharf', 'freeze', 'yacht',
    'zebra', 'crisp', 'dozen', 'elbow', 'frost',
    'banana', 'camera', 'dragon', 'bingo', 'flower',
    'garden', 'hammer', 'island', 'jungle', 'kettle',
    'ladder', 'marble', 'crazy', 'orange', 'puzzle',
    'rabbit', 'silver', 'ticket', 'curly', 'window']

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
                result.append((guess[i],'#7EBF7A'))
            elif guess[i] in self.word:
                result.append((guess[i],'#E8C97E'))
            else:
                result.append((guess[i], "#F7DCDA"))
       
        self.attempts+=1
        
        if guess==self.word:
            self.isWon = True
            self.isOver = True
        elif self.attempts >= self.maxAttempts:
            self.isOver = True

        return result