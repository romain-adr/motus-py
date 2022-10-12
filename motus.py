# MODULE OF INTEGRATED LIBRARY IMPORT
import random
import os

# COLOR VARIABLE
PLACE = '\033[93m' #YELLOW
PERFECT = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR

# CLEAR TERMINAL
def clear_console():
    os.system('cls')

# GLOBAL GRAPHIC INTERFACE
def affichage_top(all_try,word_lenght):
    print('x'*80)
    print('x' + ' '*32 + 'MOTUS GAME' + ' '*32 + 'x')
    print('x'*80)
    print('x'+' '*78+'x')
    if all_try != []:
        for i in range(len(all_try)):
            print('x' + ' '*(39-int(word_lenght/2)) + all_try[i] + ' '*(39-int(word_lenght/2)) + 'x')
        for i in range(1, 8-len(all_try)):                                                                              
            print('x'+' '*78+'x')
    else:
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
        print('x'+' '*78+'x')
    print('x'+' '*78+'x')
    print('x'*80)

# QUESTION PART ON GRAPHIC INTERFACE
def affichage_bottom(question):
    print('x' + ' '*(39-int(len(question)/2)) + question + ' '*(39-int(len(question)/2)) + 'x')
    print('x'*80)

# CHECK IF WORD EXIST IN DICTIONNARY.TXT
def check_word(entry):
    with open('dictionnary.txt') as file:
        if entry in file.read():
            return True

# CHOOSE A RAMDOM WORD IN DICTIONNARY.TXT
def choose_word(word_lenght):
    lines = open('dictionnary.txt').read().splitlines()
    word_choosed = ''   
    while word_lenght != len(word_choosed):
        word_choosed = random.choice(lines)
    return word_choosed

# COMPARISON BETWEEN THE CHOSEN WORD AND THE USER INPUT AND COLOR IT ON CONDITIONS OF THE GAME
def verify_letter(word_choosed,entry,all_try):
    if entry == word_choosed:
        all_try.append(f'{PERFECT}{entry}{RESET}')
        return True
    duplicator = 1
    result_try = ''
    for a,b in zip(word_choosed,entry):
        if a == b:
            result_try += f'{PERFECT}{a}{RESET}'
        elif b in word_choosed:
            if entry.count(b) > word_choosed.count(b):
                if duplicator <= word_choosed.count(b):
                        result_try += f'{PLACE}{b}{RESET}'
                        duplicator += 1
                else:
                    result_try += '_'
            else:
                result_try += f'{PLACE}{b}{RESET}'               
        else:
            result_try += '_'
    all_try.append(result_try)

# START 
def main():
    clear_console()
    input(" < Tapez ENTREE pour commencer à jouer > ")
    clear_console()

    all_try = []
    word_lenght = 0
# USER CHOOSE WORD LENGHT
    affichage_top(all_try,word_lenght)
    affichage_bottom(f'Vous voulez jouer sur des mots de quelle longueur ?')
    word_lenght = int(input())
    clear_console()
# RAMDOM WORD IN DICTONNARY.TXT 
    word_choosed = choose_word(word_lenght)
# USER WRITE A WORD
    win = False
    try_left = 7 # NUMBER OF ATTEMPTS
    while not win:
        correct = False
        while correct == False:
            affichage_top(all_try,word_lenght)
            affichage_bottom(f'Quelle est votre proposition ? ({try_left}) ')
# WORD LENGHT INPUT ARE FALSE              
            entry = input()
            clear_console()
            if check_word(entry):
                if len(word_choosed) != len(entry):
                    print(f'Le nombre de caractères doit être égal à {len(word_choosed)}')
                else:
                    correct = True
                    try_left += -1
# NUMBER OF ATTEMPTS = 0 LEFT
                    if try_left == 0:
                        affichage_top(all_try,word_lenght)
                        affichage_bottom(f'IL fallait trouver {word_choosed} ! Appuyer sur ENTREE pour reessayer :')
                        input()
                        main()
# THE WORD CHOOSEN DONT EXIST IN DICTONNARY          
            else:
                print(f'{entry} n\'est pas un mot existant')
# SUCCESS DISPLAY
        win = verify_letter(word_choosed,entry,all_try)
    affichage_top(all_try,word_lenght)
    affichage_bottom(f'FELICITATIONS VOUS AVEZ TROUVE LE MOT {entry} !')
    input()
    main()

main()



