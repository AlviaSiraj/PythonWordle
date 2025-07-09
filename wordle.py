import random

words_list= ['canada','grape', 'doctor','bingo','create','could']
word=random.choice(words_list)

answer = ['-' for _ in word]
print('_ '*len(word))
print(f"this word is {len(word)} letters")

    #game loop
while True:
    guess = input('Enter word to guess: ')

    while len(guess)!= len(word):
        print("Guess must be the same length as the word")
        guess = input('Enter another guess: ')

    for i in range(len(answer)):
        if(guess[i]==word[i]):
            answer[i]=guess[i]
        
    solution = "".join(answer)
    print(solution)

    if solution==word:
        print("You guessed the word!")
        break