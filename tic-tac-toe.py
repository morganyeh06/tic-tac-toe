# Morgan Yeh 
# 2025/01/10
# Tic-Tac-Toe program

import pygame
import random
import tkinter as tk
from tkinter import simpledialog

pygame.init()

# variable definitions
ROOT = tk.Tk()
ROOT.withdraw()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36, True)

run = True
current_turn = "X"
game_status = "playing"
board_full = False
board = [["empty", "empty", "empty"],
         ["empty", "empty", "empty"],
         ["empty", "empty", "empty"]]

player_sym = ""
cpu_sym = ""   
player_choice = ""      

#Get the user to choose what to play as (X or O)
while (player_choice != "1" and player_choice != "2"):
    player_choice = simpledialog.askstring(title="Choose Player",
                                  prompt="Choose an option (type 1 or 2):\n1. Play as X\n2. Play as O")
    if(player_choice == "1"):
        player_sym = "X"
        cpu_sym = "O"
    elif(player_choice == "2"):
        player_sym = "O"
        cpu_sym = "X"


# draw an X at a specified location
def drawX(x,y):
  pygame.draw.lines(screen, (255,255,255), True, [(x-50,y-50),(x+50,y+50)], 10)
  pygame.draw.lines(screen, (255,255,255), True, [(x-50,y+50),(x+50,y-50)], 10)

# draw an O at a specified location
def drawO(x, y):
    pygame.draw.circle(screen, (255,255,255), (x, y), 60, 10)


# handle user turn
def user_turn(mouseX, mouseY):
    
    # change value of element in array depending on space clicked
    if((25 < mouseX and mouseX < 215) and (25 < mouseY and mouseY < 215) and board[0][0] == "empty"):
        board[0][0] = player_sym
        
    elif((25 < mouseX and mouseX < 215) and (235 < mouseY and mouseY < 415) and board[1][0] == "empty"):
        board[1][0] = player_sym

    elif((25 < mouseX and mouseX < 215) and (435 < mouseY and mouseY < 625) and board[2][0] == "empty"):
        board[2][0] = player_sym 

    elif((235 < mouseX and mouseX < 415) and (25 < mouseY and mouseY < 215) and board[0][1] == "empty"):   
        board[0][1] = player_sym

    elif((235 < mouseX and mouseX < 415) and (235 < mouseY and mouseY < 415) and board[1][1] == "empty"):
        board[1][1] = player_sym  

    elif((235 < mouseX and mouseX < 415) and (435 < mouseY and mouseY < 625) and board[2][1] == "empty"):
        board[2][1] = player_sym  

    elif((435 < mouseX and mouseX < 625) and (25 < mouseY and mouseY < 215) and board[0][2] == "empty"):
        board[0][2] = player_sym
    
    elif((435 < mouseX and mouseX < 625) and (235 < mouseY and mouseY < 415) and board[1][2] == "empty"):
        board[1][2] = player_sym

    elif((435 < mouseX and mouseX < 625) and (435 < mouseY and mouseY < 625) and board[2][2] == "empty"):
        board[2][2] = player_sym

    # check game status
    is_board_full()
    update_game_status()


# handle cpu turn
def cpu_turn():
    end_turn = False

    while(not end_turn):
        # generate random space in board
        r_row = random.randint(0, 2)
        r_col = random.randint(0, 2)

        if (board[r_row][r_col] == "empty"):
            board[r_row][r_col] = cpu_sym
            end_turn = True

    # check game status
    is_board_full()
    update_game_status()

# check if game has been won  
def update_game_status():

    # check if any rows are complete
    for row in range(0,3):
        if(board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "empty"):
            global game_status
            game_status = board[row][0] + " wins!"
            return 1

    # check if any colums are complete
    for col in range(0,3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "empty"):
            game_status = board[0][col] + " wins!"
            return 1

    # check diagonals
    if(board[0][0] == board[1][1] and board[1][1] == board [2][2] and board[1][1] != "empty"):
        game_status = board[0][0] + " wins!"
        return 1
    elif(board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != "empty"):
        game_status = board[2][0] + " wins!"
        return 1
    elif(board_full):
        game_status = "Draw!"
        return 1
    

    return 1

# draw game board
def draw_board():
    border = pygame.Rect(25, 25, 600, 600)
    hor1 = pygame.Rect(25, 215, 600, 20)
    hor2 = pygame.Rect(25, 415, 600, 20)
    vert1 = pygame.Rect(215, 25, 20, 600)
    vert2 = pygame.Rect(415, 25, 20, 600)
    #pygame.draw.rect(screen, (255,255,255), border, 5)
    pygame.draw.rect(screen, (255, 255, 255), hor1)
    pygame.draw.rect(screen, (255, 255, 255), hor2)
    pygame.draw.rect(screen, (255, 255, 255), vert1)
    pygame.draw.rect(screen, (255, 255, 255), vert2)

    for row in range(0, 3):
        for col in range(0, 3):
            if (board[row][col] == "X"):
                drawX((col)*200 + 120, (row)*200 + 120)
            elif (board[row][col] == "O"):
                drawO((col)*200 + 120, (row)*200 + 120)


# checks if the board is full
def is_board_full():
    
    for row in range(0,3):
        for col in range(0,3):
            #check if space is empty
            if(board[row][col] == "empty"):
                global board_full
                board_full = False                
                return 1

    board_full = True
    return 1

while run:
    # refresh screen
    screen.fill((0,0,0))
    draw_board()

    # check if game has finished
    if(game_status != "playing"):
        # the input dialog
        USER_INP = simpledialog.askstring(title="Play again?",
                                  prompt=game_status + "\nPlay Again? (Y/N)")

        # exiting the game
        if(USER_INP == "N" or USER_INP == "n"):
            run = False
        elif(USER_INP == "Y" or USER_INP == "y"):
            # clear the board and play again
            current_turn = "X"
            game_status = "playing"
            board_full = False
            board = [["empty", "empty", "empty"],
                     ["empty", "empty", "empty"],
                     ["empty", "empty", "empty"]]
            
            player_sym = ""
            cpu_sym = ""   
            player_choice = ""      

            #Get the user to choose what to play as (X or O)
            while (player_choice != "1" and player_choice != "2"):
                player_choice = simpledialog.askstring(title="Choose Player",
                                  prompt="Choose an option:\n1. Play as X\n2. Play as O")
                if(player_choice == "1"):
                    player_sym = "X"
                    cpu_sym = "O"
                elif(player_choice == "2"):
                    player_sym = "O"
                    cpu_sym = "X"


    for event in pygame.event.get():
        # handle exiting program
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and current_turn == player_sym and game_status == "playing":
            x, y = pygame.mouse.get_pos() # Get click position
            user_turn(x, y)
            #change turn to cpu
            current_turn = cpu_sym
            draw_board()
            
    # check if it is the CPU's turn
    if (current_turn == cpu_sym and game_status == "playing"):
        cpu_turn()
        # change turns
        current_turn = player_sym
        draw_board()

    pygame.display.update()

pygame.quit()


