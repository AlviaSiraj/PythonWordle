import tkinter as tk
from tkinter import ttk #modern themed widget set and API
from wordle import WordleGame

#Add the wordle game
game= WordleGame()

#initialize window
root=tk.Tk()
root.geometry("600x400")
root.configure(bg="#FCDEEC")

root.title("Wordle Game")
root.iconbitmap("wordleIcon.ico")

#track rows
currentRow=0

def submitGuess():
    global currentRow

    # clear the message label
    messageLabel.config(text="")
    guess=entry.get().lower()
    entry.delete(0,tk.END)

    if(len(guess)!= game.wordLength):
        messageLabel.config(text=f"word must be {game.wordLength} letters long")
        return
    
    results = game.checkGuess(guess)  # [(letter, color), ...]
    attemptsMessage.config(text=f"attempts: {game.attempts}")

    # Display letter boxes with correct colors
    for i, (letter,color) in enumerate(results):
        label = tk.Label(centerFrame, text=letter.upper(), width=4, height=2, font=("Consolas", 20, "bold"), bg=color, relief="ridge")
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
        currentRow += 1

centerFrame = tk.Frame(root, bg="#FCDEEC")  # Light blue-ish background
centerFrame.config()
centerFrame.pack(expand=True) #Center a frame in the window
# framework.grid()
#input fields
tk.Label(centerFrame, text=f"The word is {game.wordLength} Letters Long",bg="#FCDEEC").grid(row=11, column=0, columnspan=game.wordLength)
message = tk.Label(centerFrame, text=f"Enter word to guess",bg='#FCDEEC',  font=("Calibri", 12))
message.grid(row=12,column=0, columnspan=game.wordLength)
#entry
entry = tk.Entry(centerFrame,font=("Helvetica", 16))
entry.grid(row=13,column=0, columnspan=game.wordLength, pady=10)
#Submit button
submitButton = tk.Button(centerFrame, text="Submit guess", command=submitGuess)
submitButton.grid(row=14,column=0, columnspan=game.wordLength)
#message label for win/lose
messageLabel = tk.Label(centerFrame, text="",  font=("Helvetica", 12),bg='#FCDEEC')
messageLabel.grid(row=15, column=0, columnspan=game.wordLength, pady=10)

attemptsMessage = tk.Label(centerFrame, text="",  font=("Helvetica", 12),bg='#FCDEEC')
attemptsMessage.grid(row=15, column=5, columnspan=game.wordLength, pady=10)

#start GUI
root.mainloop()