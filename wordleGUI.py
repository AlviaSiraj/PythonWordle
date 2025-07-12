import tkinter as tk
import customtkinter as ctk
from tkinter import ttk #modern themed widget set and API
from wordle import WordleGame
import enchant

# Create dictionary object (English)
d = enchant.Dict("en_US")  # or "en_GB" for British English

ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue") 

#Add the wordle game
game= WordleGame()

# ---- INITIALIZE WINDOW ----
root=ctk.CTk()
root.geometry("600x650")
root.title("Wordle Game")
root.iconbitmap("wordleIcon.ico")
 
# ---- INITIALIZE FRAMES ----
mainFrame = ctk.CTkFrame(root, fg_color="#FFEDEE")  # ✅ use `fg_color` not `bg_color`
mainFrame.pack(expand=True, fill="both")

guessFrame = ctk.CTkFrame(mainFrame, fg_color="#FFEDEE")
guessFrame.pack(pady=20)

topFrame = ctk.CTkFrame(mainFrame, fg_color="#FFEDEE")
topFrame.pack()

# ---- TITLE ----
ctk.CTkLabel(guessFrame,text="WORDLE GAME", font=("Consolas", 28, "bold"), fg_color='#FFEDEE',text_color="#D39D96").grid(row=0, column=0, columnspan=game.wordLength, pady=(0, 10))

#track rows
currentRow=1

# show row of empty boxes
for i in range(10):  # 10 rows
    for j in range(game.wordLength):
        label = ctk.CTkLabel(guessFrame, text="", width=40, height=40, font=("Helvetica", 16), fg_color='#F7DCDA', corner_radius=6)
        label.grid(row=currentRow+i, column=j, padx=2, pady=2)
        
def submitGuess():
    global currentRow

    # clear the message label
    messageLabel.configure(text="")
    guess=entry.get().lower()
    entry.delete(0,ctk.END)

    if(len(guess)!= game.wordLength):
        messageLabel.configure(text=f"word must be {game.wordLength} letters long")
        return
    
    if d.check(guess)==False:
        messageLabel.configure(text="Word does not exist, try again")
        return
    else:
        results = game.checkGuess(guess)  # [(letter, color), ...]

    # Display letter boxes with correct colors
    for i, (letter,color) in enumerate(results):
        label = ctk.CTkLabel(guessFrame, text=letter.upper(), width=40, height=40, font=("Consolas", 20, "bold"), fg_color=color, corner_radius=6, text_color='#FFFFFF')
        label.grid(row=currentRow, column=i, padx=2, pady=2)
        

    if game.isWon:
        messageLabel.configure(text="🎉 You guessed the word!", font=("Helvetica", 20))
        entry.configure(state="disabled")
        submitButton.configure(state="disabled")
    elif game.isOver:
        messageLabel.configure(text=f"Game Over! The word was: {game.word.upper()}",font=("Helvetica", 20))
        entry.configure(state="disabled")
        submitButton.configure(state="disabled")
    else:
        currentRow += 1


#input fields
# ---- ENTRY FIELD ----
# Create a frame specifically for the entry/button row
input_frame = ctk.CTkFrame(topFrame, fg_color="#FFEDEE")
input_frame.pack(pady=(0, 20))

entry = ctk.CTkEntry(input_frame,font=("Helvetica", 16), text_color='#D39D96',width=200, placeholder_text='Enter Word to guess')
entry.grid(row=0, column=0, padx=(0, 10))
# ---- SUBMIT BUTTON ----
submitButton = ctk.CTkButton(input_frame, text="Submit guess", font=("Consolas", 14, "bold"), command=submitGuess,text_color="#F7F3F6", fg_color="#D39D96", hover_color="#755B64", )
submitButton.grid(row=0, column=1)
# Bind Enter key to submit
entry.bind("<Return>", lambda event: submitGuess())
# ---- MESSAGES ----
messageLabel = ctk.CTkLabel(topFrame, text="", font=("Helvetica", 12), 
                          fg_color="#FFEDEE", text_color='#D39D96')
messageLabel.pack(pady=(0, 0))

#start GUI
root.mainloop()