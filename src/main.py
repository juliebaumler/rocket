
import random
import os
from game_words import word_list
from game_art import stages, logo


def choose_word():
    chosen_word = random.choice(word_list)    
    return chosen_word


def guess_a_letter():
    print()
    guess = ""

    #os.system("clear")
    guess = input("mayka palach t'səm-bit: ").lower()
    print("Guess: ", guess)

    # while not isalpha or in ".", "ʔ", "ʰ", "'", "x̣"
    alt_char_list = [".", "ʔ", "ʰ", "'", "x̣"]
    #print(alt_char_list)
    #if "x̣" in alt_char_list:
    #    print("It's in the freaking list")
    while not (guess.isalpha() or (guess in alt_char_list)):
        print("wik t'səm-bit ukuk. munk-kakwa wəx̣t.\n")
        guess = input("mayka palach t'səm-bit: ").lower()   # um....does this do anything weird?
    
    return guess 

# This does NOT work because x̣ is a string. So check for x̣ and adjust the display accordingly. 
def letter_check(word, letter, display_list, lives):
    result = [i for i in range(len(word)) if word.startswith(letter, i)]
   
    if not result:
        print("t'sipi!\n")
        lives -= 1
    else:
        for value in result:
            display_list[value] = letter
    
    return display_list, lives


def create_display(word):
    display_list = []
    #print('length of the original word: ', len(word))
    if "x̣" in word:
        number_of_spaces = len(word) - 1
        #print('Adjusted length: ', number_of_spaces)
    else: 
        number_of_spaces = len(word)
 
    for _ in range(number_of_spaces):
        display_list.append("_")
   
    return display_list


os.system("clear")
print(logo)

lives = 6

chosen_word = choose_word()

print("chosen_word: ", chosen_word)
print()

display_list = create_display(chosen_word)

print("\n\n\n==============")
print(f"\n\n\n{' '.join(display_list)}\n")


used = []
guess = ""

while "_" in display_list and not lives == 0: 
    
    guess = guess_a_letter()
    #print(f"Guess: {guess}\n")

    while guess in used:
        print(f"You used {guess} already. Try again.")
        guess = guess_a_letter()
    used.append(guess)    

    #clear
    
    result = letter_check(chosen_word, guess, display_list, lives)
    lives = result[1]
    print(f"{stages[lives]}\n")

    print(f"{' '.join(display_list)}\n")
    print(f"Remaining Lives: {lives}\n")
  
if not "_" in display_list:
    print("dret ɬush! mayka tulu!")
elif lives == 0:
    print(f"The word was: {chosen_word}\n")
    print("wik mayka tulu. :( ")


