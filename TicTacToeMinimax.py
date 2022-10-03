#Tic Tac to game

from turtle import pos


board = {1:' ', 2:' ', 3:' ',
        4:' ', 5:' ', 6:' ',
        7:' ', 8:' ', 9:' '}
player = 'O'
computer = 'X'

def printBoard(board):
    """_summary_ Prints board for tic tac toe game

    Args:
        board (Dictonary): 
    """
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    """Checks availability of space on the board

    Args:
        position (int): Position on the board in range 1 to 9

    Returns:
        boolean: true or false for the availability of position
    """
    if(board[position] == ' '):
        return True
    return False

def insertLetter(letter, position):
    """Inserts letter into the board

    Args:
        letter (String): O for player and X for computer
        position (int): Int value  in range 1 to 9
    """
    if(spaceIsFree(position)):
        board[position] = letter
        printBoard(board)
        if(checkDraw()):
            print("Draw")
            exit()
        if checkWin():
            if letter == "X":
                print("Bot Wins")
                exit()
            else:
                print("Player Wins")
                exit()
        return
    else:
        print("Invalid Move")
        position = int(input("Please enter a new Position:"))
        insertLetter(letter, position)
        return


def checkWin():
    """Checks who won the game

    Returns:
        boolean_: True if game is won by any of the player else false
    """
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def whichWon(mark):
    """Checks who won X or O

    Args:
        mark (String): O or X for player and computer respectively

    Returns:
        boolean: True or false
    """
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    """Checks whether game is draw or not

    Returns:
        boolean_: true if game is draw else false_
    """
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove():
    """Takes position input form user (1-9)
    """
    position = int(input("Enter a postion for O (1-9): "))
    insertLetter(player, position)
    return

def compMove():
    """Determines computer move
    """
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score>bestScore:
                bestScore = score
                bestMove = key

    insertLetter(computer,bestMove)
    return

def minimax(board, isMaximizing):
    """Determines optimum postion for computer

    Args:
        board (dictionary_): position of the board
        isMaximizing (bool): whether to maximize for minimize the algorithem

    Returns:
        _type_: _description_
    """
    if whichWon(computer):
        return 1
    elif whichWon(player):
        return -1
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score>bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score<bestScore:
                    bestScore = score
        return bestScore        



printBoard(board)
while not checkWin():
    playerMove()
    compMove()