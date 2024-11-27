#11/12/2024
import random
import os
import time
from askii_hangman import *
from word_dict import hangman_words

word_to_guess = hangman_words
char_dict = []
guessed_let = ["0"]
ans = []
wrong_guess = []
life = 6
chosen_word = random.choice(word_to_guess)

def word_chosen():
    for letter in chosen_word:
        char_dict.append(letter)

def ask_guess(char):
    print("\nguess the word: ", end = "")
    for letter in char_dict:
        if letter == char:
            for l in guessed_let:
                if char not in guessed_let:
                    guessed_let.append(char)
        if letter in guessed_let:
            print(f"{letter} ", end='')
        else: 
            print("_ ", end='')

print(logo)
word_chosen()
char = ""
ask_guess(char)

while True:
    print(HANGMANPICS[life])
    char = input("\ninput a letter: ").lower()
    os.system("cls")
    if char in guessed_let:
        print(f'"{char}" already listed')
    elif char in char_dict:
        print(f'"{char}" is in the word')
        ans.append(char)
    elif char in wrong_guess:
        print(f'you\'ve already entered "{char}"')
    elif char == chosen_word:
        print("you have guessed the word. You Won!")
        break
    else:
        life-=1
        wrong_guess.append(char)
        print(f'"{char}" is not in the word, life left {life}/6')
    if life == 0:
        print(HANGMANPICS[life])
        life-=1
        time.sleep(3)
        os.system("cls")
        print(HANGMANPICS[life])
        print(f'the word is "{chosen_word}"')
        print("\nthe character died, you lose")
        break
    ask_guess(char)
    if len(ans) == len(set(char_dict)):
        print("\nyou won, you get to live")
        break
