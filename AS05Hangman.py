def check():
    guess = input("Input your guess: ")
    return guess.isalpha() and len(guess) == 1, guess

def displayWord(word):
    display = ""
    notEmpty = True
    for i in word:
        if i not in guessedLetters:
            notEmpty = False
            display += "_"
        else:
            display += i
    return display, notEmpty

wordlist = ["minnow", "computer science", "tetris", "cats"]

for word in wordlist:
    guessedLetters = []  
    guessed = False
    lives = 10
    while lives != 0 and not guessed:
        char = False
        while not char:
            char, guess = check()
        if guess in guessedLetters:
            print("You have already guessed this letter")

        elif guess in word:
            guessedLetters.append(guess)
            print("It is in the word")
        else:
            lives -= 1
            guessedLetters.append(guess)
            print("This letter is not in the word")
        display, guessed = displayWord(word)
        print(display)
    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you've run out of lives. The word was: {word}")
