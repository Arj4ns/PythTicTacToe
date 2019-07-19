# -*- coding: utf-8 -*-
"""
Tic Tac Toe Test
Created on Sun Jun 30 10:36:34 2019

@author: Arjan
"""
tictactoe = [" ", " ", " ",     # 0, 1, 2
             " ", " ", " ",     # 3, 4, 5
             " ", " ", " ", ]   # 6, 7, 8

turn = False
letterX = "x"
letterO = "o"
running = True


def isListEmpty(array):
    for i in range(len(array)):
        if array[i] == " ":
            return True
    return False

def remainingEmpty(a):
    count = 0
    for i in range(len(a)):
        if a[i] == " ":
            count = count + 1
    return count

def winCon(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
            (bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
            (bo[0] == le and bo[3] == le and bo[6] == le) or # down the left side
            (bo[1] == le and bo[4] == le and bo[7] == le) or # down the middle
            (bo[2] == le and bo[5] == le and bo[8] == le) or # down the right side
            (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
            (bo[0] == le and bo[4] == le and bo[8] == le)) # diagonal
    

    
def minimax(a, depth, maximum):
    if winCon(a, "o"):
        return 10
    elif winCon(a, "x"):
        return -10
    elif isListEmpty(a) == False:
        return 0
    
    if maximum:
        best = -1000
        for i in range(len(a)):
            if a[i] == " ":
                a[i] = "o"
                maximum = False
                best = max(best, minimax(a, depth + 1, maximum))
                a[i] = " "
        return best + depth
    else:
        worst = 1000
        for i in range(len(a)):
            if a[i] == " ":
                a[i] = "x"
                maximum = True
                worst = min(worst, minimax(a, depth + 1, maximum))
                a[i] = " "
        return worst - depth

def aiControl(a):
    bestScore = -1000
    winningMove = 0
    for i in range(len(a)):
        if a[i] == " ":
            a[i] = "o"
            moveScore = minimax(a, 0, False)
            a[i] = " "
            if moveScore > bestScore:
                winningMove = i
                bestScore = moveScore
    return winningMove
        
    
        
def drawBoard(tictactoe):
    print(" ")
    print(tictactoe[0] + " | " + tictactoe[1] + " | " + tictactoe[2])
    print("---------")
    print(tictactoe[3] + " | " + tictactoe[4] + " | " + tictactoe[5])
    print("---------")
    print(tictactoe[6] + " | " + tictactoe[7] + " | " + tictactoe[8])
    print(" ")
    
    

print("To play, enter the index of the board position you want to mark.")
print(" ")
drawBoard(tictactoe)

while isListEmpty(tictactoe) == True and running == True:
    if turn == False:
        position = int(input("Enter the x coordinate of the position you want to mark (0 - 8)"))
        if tictactoe[position]  == " ":
            tictactoe[position] = letterX
            turn = True
        else:
            print("That spot is taken already!")
    else:
        choice = aiControl(tictactoe)
        tictactoe[choice] = letterO
        turn = False     
        
    drawBoard(tictactoe)
    
    if winCon(tictactoe, letterX) == True:
        print("You win!")
        running = False
    elif winCon(tictactoe, letterO) == True:
        print("The AI wins!")
        running = False
    elif winCon(tictactoe, letterX) == False and winCon(tictactoe, letterO) == False and isListEmpty(tictactoe) == False:
        print("It's a Tie")
        running = False


