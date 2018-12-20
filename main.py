import random
import time


def generate_empty_board(x,y):
    """
    generates matrix x rows y columns filled with zeros
    :param x: n of rows
    :param y: n of columns
    :return: lists of lists of zeros
    """
    board = [[0]*y for i in range(x)] 
    
    return board

def generate_initial_population(board, n):
    """
    replaces n random zeroes with ones in given table
    :param board: given table
    :param n: number of cells to replace
    :return: transformed matrix
    """
    if n > len(board)*len(board[0]): 
        print("More living cells than space on this board")
        return board 
    i = 0
    while i < n:
        x = random.randint(0, len(board)-1)
        y = random.randint(0, len(board[0])-1)
        if board[x][y] == 0:
            board[x][y] = 1
            i = i + 1
            print("{}/{} filled.".format(i,n))

    return board
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
    new_board = generate_empty_board(len(board),len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if check_if_alive(i , j , board):
                new_board[i][j] = 1
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
    length = len(Tab) - 1
    width = len(Tab[0]) - 1 
    n = 0  # number of neighbouring living cells
    for i in [x - 1, x, x + 1]:  # count number of neigh
        for j in [y - 1, y, y + 1]:

            if i < 0 or j < 0:
                continue
            if i > length or j > width:
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
    print("Game of Life | Generation: {} | Alive cells : {} | Dead cells: {} | Size: {} |".format(n, count_population(board), len(board)*len(board[0])- count_population(board),  len(board)*len(board[0])))

    print("+" +((len(board[0])*2)+1)*"-" + "+") #frame of board
    for i in range(len(board)):
        print("|", end=" ") #frame of board
        for j in range(len(board[0])):
            if board[i][j] == 1:
                print("%", end=" ")
            else:
                print("-", end=" ")
        print('|') #frame of board
    print("+" +((len(board[0])*2)+1)*"-" + "+") #frame of board
    return



x = int(input("Please insert width: "))
y = int(input("Please insert height: "))

board = generate_empty_board(x,y)
initial = int(input("Please insert n of alive cells: "))
board = generate_initial_population(board,initial)
#board = [[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,1,1,1,0,0,0]
#        ,[0,0,0,0,1,0,0,0,0,0]
#        ,[0,0,0,0,0,1,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]
#        ,[0,0,0,0,0,0,0,0,0,0]]   glider pattern



old_board = []
generation = 0

while not compare_generations(board,old_board):
    generation += 1
    print_board(board,generation)
    old_board = board
    board = evolve_population(board)
    time.sleep(0.8)

print("Game of Life ended after {} populations, with {} alive cells".format(generation, count_population(board)))

# while True:
#     board = evolve_population(board)
#     print(*board, sep='\n', end='\n \n')
#     time.sleep(1)
