from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


# Return the player's turn
def player(board):
    X = []
    O = []
    EMPTY = []

    # X is always the first player
    if (board == initial_state()):
        return "X"

    # Flatten the 2D list into a 1D list
    flatList = []
    for rows in range(len(board)):
        row = board[rows]
        for cell in range(len(row)):
            flatList.append(row[cell])

    # Loop through the flat list and check the amount of X , O and None
    for element in range(len(flatList)):
        el = flatList[element]
        if (el == "X"):
            X.append(el)
        elif (el == "O"):
            O.append(el)
        elif (el == None):
            EMPTY.append(el)
    if (len(EMPTY) == 0):
        return "Game is Over"
    elif (len(X) > len(O)):
        return "O"
    elif (len(X) == len(O)):
        return "X"


# Returns a set of all possile actions for a specific board
def actions(board):
    actions = set()
    no_actions_avaiable = set()
    for j in range(len(board)):
        for i in range(len(board[j])):
            if (board[j][i] == None):
                actions.add((j, i))

    if (len(actions) == 0):
        return no_actions_avaiable
    return actions


# Returns a new board after a specific action
def result(board, action):
    list = []
    for item in (action):
        list.append(item)
    i = list[0]
    j = list[1]
    getActions = actions(board)
    if (board[i][j] != None or action not in getActions):
        raise NameError('This action is not possible')
    newBoard = deepcopy(board)
    turn = player(board)
    newBoard[i][j] = turn
    return newBoard


# Return the winner of the game
def winner(board):
    horizontal_winner = check_winner_horizontally(board)
    verical_winner = check_winner_vertically(board)
    diagonal_winner = check_winner_diagonals(board)
    if (horizontal_winner):
        return horizontal_winner
    elif (verical_winner):
        return verical_winner
    elif (diagonal_winner):
        return diagonal_winner


# Checks if the game is over or not
def terminal(board):
    if (winner(board) or all_options_exhausted(board)):
        return True
    else:
        return False


# Determine the value of a board
def utility(board):
    if (terminal(board)):
        if (winner(board)):
            if (winner(board) == "X"):
                return 1
            elif (winner(board) == "O"):
                return -1
        else:
            return 0


# Minimax algorithm : https://en.wikipedia.org/wiki/Minimax
# Great explanation in the CS50 Course https://www.youtube.com/watch?v=WbzNRTTrX0g&t=4322s
def minimax(board):
    player_value = player(board)

    actions_list = set_into_list(board)

    if (player_value == "X"):
        max_result_obj = {-1: [], 0: [], 1: []}
        for action in range(len(actions_list)):
            v = min_value(result(board, actions_list[action]))
            max_result_obj[v].append(actions_list[action])
        if max_result_obj[1]:
            return max_result_obj[1][0]
        elif max_result_obj[0]:
            return max_result_obj[0][0]

    elif (player_value == "O"):
        min_result_obj = {-1: [], 0: [], 1: []}
        for action in range(len(actions_list)):
            v = max_value(result(board, actions_list[action]))
            min_result_obj[v].append(actions_list[action])
        if min_result_obj[-1]:
            return min_result_obj[-1][0]
        elif min_result_obj[0]:
            return min_result_obj[0][0]


# Function that the "O" Player will be using to determine the maximum value that the "X" player will choose
def max_value(board):
    if (terminal(board)):
        return utility(board)

    else:
        v = float('-inf')
        actions_list = set_into_list(board)
        for action in range(len(actions_list)):
            v = max(v, min_value(result(board, actions_list[action])))
        return v


# Function that the "X" Player will be using to determine the minimum value that the "O" player will choose
def min_value(board):
    if (terminal(board)):
        return utility(board)

    else:
        v = float('inf')
        actions_list = set_into_list(board)
        for action in range(len(actions_list)):
            v = min(v, max_value(result(board, actions_list[action])))
        return v


# Helper function that checks if there is a winner by checking the grid horizontally
def check_winner_horizontally(board):
    for list in range(len(board)):
        if (len(board[list]) != 3 or None in board[list]):
            continue
        else:
            values = set()
            for element in range(len(board[list])):
                values.add(board[list][element])
            if (len(values) == 1):
                return board[list][0]


# Helper function that checks if there is a winner by checking the grid vertically
def check_winner_vertically(board):
    lists = []
    for i in range(len(board)):
        list = []
        for j in range(len(board[i])):
            list.append(board[j][i])
        lists.append(list)
    return check_winner_horizontally(lists)


# Helper function that checks if there is a winner by checking the diagonals of the grid
def check_winner_diagonals(board):
    first_diagonal = [board[0][0], board[1][1], board[2][2]]
    second_diagonal = [board[2][0], board[1][1], board[0][2]]
    lists = [first_diagonal, second_diagonal]
    return check_winner_horizontally(lists)


# Helper function that checks if all the squares have been checked
def all_options_exhausted(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == None):
                return False
    return True


# Helper function that turns a set into a list
def set_into_list(board):
    actions_list = []
    for action in (actions(board)):
        actions_list.append(action)
    return actions_list
