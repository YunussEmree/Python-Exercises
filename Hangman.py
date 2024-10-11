import random
from nltk.corpus import words
import numpy as np

english_words = words.words()

word = random.choice(english_words).lower()
original_word = word

remaining_attempt = 6

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



print(f"(DEBUG) WORD : {word}")


secret_word = np.full(len(word), "?")

while(remaining_attempt > -1) :
    
    if not np.any(secret_word == "?") : 
        print(f"\nCongratulations You Win! The Word Was : {original_word}\n")
        break
    
    if remaining_attempt == 0 :
        print(f"You Lose! The Word Was : {original_word} ")
        print(HANGMANPICS[6])
        break
    print(HANGMANPICS[np.abs(remaining_attempt-6)])
    
    letter = input(f"Input a letter (Remaining Attempts) : {remaining_attempt}) : ").lower()
    how_many_letters = word.count(letter)

    if how_many_letters == 0 : 
        remaining_attempt -= 1

    for i in range(how_many_letters) :
        print(f"ÖNEMLİ : (WORD) {word}" )
        print(f"ÖNEMLİ : (LETTER) {letter}" )
        index = int(word.index(letter))
        secret_word[index] = letter
        wordlist = list(word)
        wordlist[index] = "*"
        word = ''.join(wordlist)
    
        how_many_letters -= 1
    print(f"(DEBUG) WORD : {word}")
    print(secret_word)


input("\nPress Enter To Continue...\n")