import tkinter as tk
from tkinter import ttk #modern themed widget set and API
from wordle import WordleGame

#Add the wordle game
game= WordleGame()

#initialize window
root=tk.Tk()
root.title="Wordle Game"

#track rows
currentRow=0

def submitGuess():
    global currentRow

    guess=entry.get().lower()
    entry.delete(0,tk.END)

    if(len(guess)!= game.wordLength):
        messageLabel.config(f"word must be {game.wordLength} letters long")
        return
    
    results = game.checkGuess(guess)  # [(letter, color), ...]
    attemptsMessage.config(text=game.attempts)

    # Display letter boxes with correct colors
    for i, (letter,color) in enumerate(results):
        label = tk.Label(root, text=letter.upper(), width=4, height=2, font=("Helvetica", 16), bg=color, relief="solid")
        label.grid(row=currentRow, column=i, padx=2, pady=2)

    if game.isWon:
        messageLabel.config(text="🎉 You guessed the word!")
        entry.config(state="disabled")
        submitButton.config(state="disabled")
    elif game.isOver:
        messageLabel.config(text=f"Game Over! The word was: {game.word.upper()}")
        entry.config(state="disabled")
        submitButton.config(state="disabled")
    else:
        current_row += 1

# framework = ttk.Frame(root,padding=30)
# framework.grid()
#input fields
message = tk.Label(root, text="Enter word to guess",  font=("Helvetica", 12))
message.grid(row=9,column=0, columnspan=game.wordLength)
entry = tk.Entry(root,font=("Helvetica", 16))
entry.grid(row=10,column=0, columnspan=game.wordLength, pady=10)
#Submit button
submitButton = tk.Button(root, text="Submit guess", command=submitGuess)
submitButton.grid(row=11,column=0, columnspan=game.wordLength)
#message label for win/lose
messageLabel = tk.Label(root, text="",  font=("Helvetica", 12))
messageLabel.grid(row=12, column=0, columnspan=game.wordLength, pady=10)

attemptsMessage = tk.Label(root, text="",  font=("Helvetica", 12))
attemptsMessage.grid(row=12, column=5, columnspan=game.wordLength, pady=10)

#start GUI
root.mainloop()

