import random
import sys
from random_word import RandomWords

w = RandomWords()
word = w.get_random_word()
guess_word = []
secretWord = word
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def reset():
    global w
    global word
    global guess_word
    global secretWord
    global length_word
    global alphabet
    global letter_storage
    
    w = RandomWords()
    word = w.get_random_word()
    guess_word = []
    secretWord = word
    length_word = len(secretWord)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []
    
def playGame():
    while True:
        gameChoice = input("Would You like to play some Hangman?\n")
        gameChoice = gameChoice.upper()
        if gameChoice == "YES":
            break
        elif gameChoice == "NO":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer with a Yes or No")
            continue
playGame()
def change():
    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")
    print("Ok, so the word You need to guess has", length_word, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print(guess_word)

def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): 
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")                    
                    while True:
                        continues = input ("Would you like to play Hangman again? ").upper()
                        if continues == "YES":
                            reset()
                            change()
                            guessing()
                        elif continues == "NO":
                            sys.exit("Have a nice day!")
                        else:
                            print("Please answer with yes or no.")
                            continue
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry. You lost :( The secret word was",secretWord)
                    while True:
                        continues = input ("Would you like to play Hangman again? ").upper()
                        if continues == "YES":
                            reset()
                            change()
                            guessing()
                        elif continues == "NO":
                            sys.exit("Have a nice day!")
                        else:
                            print("Please answer with a yes or no")
                            continue
    
change()
guessing()
print("Game Over!")
