import random
import time


def generate_empty_board(x,y):
    """
    generates matrix x rows y columns filled with zeros
    :param x: n of rows
    :param y: n of columns
    :return: lists of lists of zeros
    """
    board = [[0]*y for i in range(x)]  #we create board that contains x lists containing y 0s

    return board #we return board as a value of a function
def generate_initial_population(board, n):
    """
    replaces n random zeroes with ones in given table
    :param board: given table
    :param n: number of cells to replace
    :return: transformed matrix
    """
    if n > len(board)*len(board[0]): #if we want to put more cells on board than there is a space we break the program
        print("More living cells than space on this board")
        return board #in this case ive decided to return empty table
    i = 0                           # variable i that will store number of already assigned ones
    while i < n:                    # while i is smaller than number of cells to replace do this:
        x = random.randint(0, len(board)-1) # x is a integer randomly choosen from range (0 (which stands for 1 element), and width of a board
        y = random.randint(0, len(board[0])-1) # y is an integer randomly choosen from range 0 to the last element of height
        if board[x][y] == 0: # if randomly choosen position is 0
            board[x][y] = 1 #change it to one
            i = i + 1 #and add 1 to i, so theres only n minus i iterations left

    return board # returns value of a function as transformed board "generated random population"
def count_population(Tab):
    """
    counts number of alive cells
    Args:
        Tab - board of given frame
    Return:
        number of alive cells
    """
    n = 0 #number of alive cells
    for i in range(len(Tab)):
        for j in range(len(Tab[i])):
            if Tab[i][j] == 1:
                n = n + 1

    return n

def compare_generations(Tab1, Tab2):
    """
    Function which compare two given tables
    :param Tab1: first table
    :param Tab2: second table
    :return: True if tables are the same False if not
    """
    if Tab1 == Tab2:
        return True
    else:
        return False

def evolve_population(board):
    """
    Function which will apply rules to all board simultaneously
    :param board: board from present generation
    :return: new board after applying rules of game to each cell
    """
    new_board = board                           #creates new board that will be modified (i copied old one so i dont have to think about size
    for i in range(len(board)):                 #create i that iterates in range(0,lenght of list of lists)
        for j in range(len(board[i])):          #create j tat iterates in range(0, lenght of list inside lists of lists)
            if check_if_alive(i , j , board):   #your function check if alive takes the same arguments, buth different results
                new_board[i][j] = 1             #so if/else isnt necessary (just replace new_board with value of my function)
            else:
                new_board[i][j] = 0
    return new_board



def check_if_alive(x, y, Tab):
    """
    Function which determine if cell should stay alive
    :param x: x coordinate of checked cell
    :param y: y coordinate of checked cell
    :param Tab: table of current frame
    :return: True if cell will be alive in the next fram False if not
    """

    n = 0  # number of neibourghs
    for i in [x - 1, x, x + 1]:  # count number of neigh
        for j in [y - 1, y, y + 1]:
            if i < 0:
                continue
            if j < 0:
                continue
            if i > len(Tab) - 1:
                continue
            if j > len(Tab[i]) - 1:
                continue
            if (i == x and j == y):
                continue
            n += Tab[i][j]  # adding no of neigh

    if Tab[x][y] == 1:  # return state of cell taking conditions (rules)
        if n == 2 or n == 3:
            return True
        else:
            return False
    else:
        if n == 3:
            return True
        else:
            return False

def print_board(board, n):
    """
    Function that prints board and info about state of game
    :param board: board of current frame
    :param n: number of generation
    :return: None
    """
    print("Game of Life | Generation: ", n ," | Alive cells : ", count_population(board)," |")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                print("#", end=" ")
            else:
                print("-", end=" ")
        print('')
    return
x = int(input("what is the width"))
y = int(input("what is the height"))
board = generate_empty_board(x,y)
initial = int(input("what is initial population"))
board = generate_initial_population(board,initial)
generation = 1
while True:
    print_board(board,generation)
    board = evolve_population(board)
    generation += 1
    time.sleep(1)
# while True:
#     board = evolve_population(board)
#     print(*board, sep='\n', end='\n \n')
#     time.sleep(1)

