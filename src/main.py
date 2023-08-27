
import random
import os
import sys
import gettext
from game_words import word_list
from game_art import stages, logo
DEBUG=1;


def choose_word():
    chosen_word = random.choice(word_list)  
    return chosen_word


def guess_a_letter():
    print()
    guess = ""

    #os.system("clear")
    guess = input(_("GIVE A LETTER: "))
    # quit if "." entered
    if guess == ".":
        print(_("BYE!"))
        sys.exit();

    # translate some common typing conventions for IPA characters
    # I didn't translate ? to ʔ because we might want to use it for help

    trans_dict = {'7':'ʔ','3':'ə','E':'ə','X':'x\u0323', 'H':'ʰ', 'L':'ɬ'}
    mytable = guess.maketrans(trans_dict)
    guess = guess.translate(mytable).casefold()
    print(_("GUESSED LETTER: "), guess)

    valid_alphabet_list = [".", "'", "a", "b", "ch", "c'h", "d", "dj", "dz", "e", "ə", "f", "g", "h", "ʰ", "i", "k", "kʰ", "kʰw", "kw", "k'", "k'w", "l", "ɬ", "m", "n", "o", "p", "pʰ", "p'", "q", "qw", "qʰ", "qʰw", "q'", "q'w", "s", "sh", "t", "tʰ", "t'", "tɬ", "t'ɬ", "ts", "t's", "u", "v", "w", "x", "x\u0323", "x\u0323w", "y", "zh", "á", "ú", "í", "ʔ", "?"]
    #if "x̣" in valid_alphabet_list:
    #    print("It's in the freaking list")
    while not (guess in valid_alphabet_list):
        print(_("NOT A LETTER. TRY AGAIN.\n"))
        guess = input(_("GIVE A LETTER: "))   # um....does this do anything weird?
        guess = guess.translate(mytable).casefold()   # just needs the processing again
    
    return guess 

# now works for letters and the strings that make up cw t'səm-bit
def letter_check(word, letter, display_list, lives):

    location=word.find(letter);
    if location == -1:
        # not found
        print(_("MISSED!"), "\n")
        lives -= 1
    else:
        while location != -1:
            for i in range(len(letter)):
                display_list[(location+i)] = letter[i]
            location=word.find(letter, location+1);
   
    
    return display_list, lives


def create_display(word):
    display_list = []
    number_of_spaces = len(word); 
 
    for x in range(number_of_spaces):
        # replace the extra character for back-x with a backspace so it doesn't show up
        # but we still have room for it
        if word[x] == "\u0323":
            display_list.append("\b")
        else:
            display_list.append("_")
    
   
    return display_list


os.system("clear")
lang1 = gettext.translation('rocket', localedir='../locale', languages=['en'])
lang2 = gettext.translation('rocket', localedir='../locale', languages=['chn'])
lang2.install()
print(logo)

lives = 6

chosen_word = choose_word()

if DEBUG:
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
        print( _("USED ALREADY. TRY AGAIN."))
        guess = guess_a_letter()
    used.append(guess)    

    #clear
    
    result = letter_check(chosen_word, guess, display_list, lives)
    lives = result[1]
    print(f"{stages[lives]}\n")

    # i18n hell - replace is not utf-8 safe and join assumes only non-joining characters
    # trans doesn't like escape strings
    output_dl = ' '.join(display_list)
    if output_dl.count(' \u0323'):
        output_dl = '\u0323'.join(output_dl.split(' \u0323'))
        

    print(f"{output_dl}\n")
    print( _("GUESSES LEFT: "),"{lives}\n")
  
if not "_" in display_list:
    print(_("GREAT! YOU WIN!"))
elif lives == 0:
    print( _("THE WORD WAS: {chosen_word}\n"))
    print(_("DIDN'T WIN"))
    


