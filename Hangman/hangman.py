import random
from shlex import join

words = ['horror', 'fiction', 'romance', 'comedy', 'action', 'drama', 'thriller']

choosen_word = random.choice(words)
word_display = ['_' for _ in choosen_word]
attempts = 8

print("Welcome to hangman!")

while attempts >0 and '_' in word_display:
    print("\n", join(word_display))
    guess = input("guess a letter: ").lower()
    if not guess.isalpha():
        print("only letters are allowed")
    else:
        if len(guess)>1:
            print("on;ly one letter allowed at a time")
        else:
            if guess in choosen_word:
                for index, letter in enumerate(choosen_word):
                    if letter == guess:
                        word_display[index] = guess
            else:
                print("letter is not in the word")
                attempts-=1

if '_' not in word_display:
    print("you guessed the word")
    print(' '.join(word_display))
else:
    print("you ran out of attempts, you lost")
    print("the word was " , choosen_word)