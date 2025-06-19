# advance number guessing game
# -------------------------------------------------------------------------------------------------------
# The computer picks a number, and the user keeps guessing until they get it right. between 1 to 100 -> 2 player game
# easy -> computer choose one time
# medium -> computer choose after every 3 attempt
# hard -> computer change value every time

import random

def randomNumber():
    return random.randint(1, 5)

def gameMode(no, lstOfName, play, defPlay = 'Easy'):
    while play:
        for i in lstOfName:
            if no == int(input(f'{i} Guess No: ')):
                play = False; winner = i; lstOfName.remove(i); loose = lstOfName[0]
                return [winner, loose]
        global playerRound
        print(f'\nRound {playerRound} UnSuccessFull\n'); playerRound += 1

        if ((defPlay == 'Medium') or (defPlay == 'Hard')): play -= 1
    return True

def medGame(lstOfName, play, defPlay):
    no = randomNumber(); retn = gameMode(lstOfName=lstOfName, no=no, play=play, defPlay=defPlay)
    return retn

def easy(no, nameOne, nameTwo):
    lstOfName = [nameOne, nameTwo]; print(); retn = gameMode(lstOfName=lstOfName, no=no, play=True)
    return retn

def medium(nameOne, nameTwo):
    lstOfName = [nameOne, nameTwo]; print(); plays = True
    while plays:
        retn = medGame(lstOfName=lstOfName, play=3, defPlay='Medium')
        if retn != True: plays = False
    return retn

def hard(nameOne, nameTwo):
    lstOfName = [nameOne, nameTwo]; print(); plays = True
    while plays:
        retn = medGame(lstOfName=lstOfName, play=1, defPlay='Hard')
        if retn != True: plays = False
    return retn

def player(winner):
    print(f"\n'{winner[0]}' is the Winner🍾🍾\nlooser is the '{winner[1]}' 😂😂")

def GuessNumberAd():
    level = int(input('Enter Level:\n1.Easy\n2.Medium\n3.Hard\n\nSelect Any Option No:- '))
    playerOneName = input('Enter Player One Name: ') or 'Player One'; playerTwoName = input('Enter Player Two Name: ') or 'Player Two'
    if level == 1: rn = randomNumber(); win = easy(rn, playerOneName, playerTwoName); player(win)
    elif level == 2: win = medium(playerOneName, playerTwoName); player(win)
    elif level == 3: hard(playerOneName, playerTwoName)
    else:
        print(f'Option {level} is not found. if you want then play easy level.');checkNewOption = int(input('1. Yes\n2. No'))
        if checkNewOption == 1: easy()
        else: print('Thank you for playing, Number Guess Game Advance')

playerRound = 0

def RoundCheck():
    print(playerRound)

# -----------------------------------------------------------------------------------
GuessNumberAd()
RoundCheck()