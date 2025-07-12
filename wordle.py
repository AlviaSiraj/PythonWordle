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
        result = [None] * self.wordLength  # Initialize with None
        wordFrequency={}           
          # Count frequency of each letter in the actual word
        for letter in self.word:
            wordFrequency[letter] = wordFrequency.get(letter, 0) + 1

      # First pass: mark correct letters (green)
        for i in range(self.wordLength):
            if guess[i] == self.word[i]:
                result[i] = (guess[i], '#7EBF7A')  # green
                wordFrequency[guess[i]] -= 1  # consume this letter

    # Second pass: mark wrong position (yellow) or not in word (pink)
        for i in range(self.wordLength):
            if result[i] is None:  # not already marked green
                if guess[i] in self.word and wordFrequency.get(guess[i], 0) > 0:
                    result[i] = (guess[i], '#E8C97E')  # yellow
                    wordFrequency[guess[i]] -= 1
                else:
                    result[i] = (guess[i], '#F7DCDA')  # pink

       
        self.attempts+=1
        
        if guess==self.word:
            self.isWon = True
            self.isOver = True
        elif self.attempts >= self.maxAttempts:
            self.isOver = True

        return result