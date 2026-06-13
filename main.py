import random
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def randomizeWord():
    words = [
        "lion",
        "tiger",
        "elephant",
        "giraffe",
        "zebra",
        "kangaroo",
        "panda",
        "dolphin",
        "penguin",
        "eagle"
    ]
    word = random.choice(words)
    return word


def guessIsTrue(word, guess):
    return guess.lower() in word.lower()


def updateProgress(word, guesses):
    wordProgress = []
    for letter in word:
        if letter.lower() in guesses:
            wordProgress.append(letter)
        else:
            wordProgress.append("_")
    return " ".join(wordProgress)


def listToStringWithSpaces(myList):
    output = ""
    for item in myList:
        output += (item + " ")
    return output


def checkWin(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True


def main():
    running = True
    win = False
    attempts = 6
    word = randomizeWord()
    correctGuesses = []
    wrongGuesses = []
    progress = updateProgress(word, "`")
    while running:
        print("H A N G M A N")
        print(progress, f"({attempts})")
        print("x :", listToStringWithSpaces(wrongGuesses))

        if win:
            break
        if attempts == 0:
            break

        guess = input("> ").lower()

        if guessIsTrue(word, guess):
            correctGuesses.append(guess)
            progress = updateProgress(word, correctGuesses)
            win = checkWin(word, correctGuesses)
        else:
            wrongGuesses.append(guess)
            attempts -= 1

        clear_terminal()

    print(f"The word is '{word.capitalize()}'.")

    if win:
        print("You win!")
    else:
        print("You lose.")


main()
