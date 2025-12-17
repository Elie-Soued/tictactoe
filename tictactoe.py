"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def player(board):

    # Initialization
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


def actions(board):

    actions = set()

    for j in range(len(board)):
        for i in range(len(board[j])):
            if (board[j][i] == None):
                actions.add((j, i))

    if (len(actions) == 0):
        return "Game is Over"

    return actions


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


def terminal(board):

    if (winner(board) or all_options_exhausted(board)):
        return True
    else:
        return False


def utility(board):

    if (terminal(board)):
        if (winner(board)):
            if (winner(board) == "X"):
                return 1
            elif (winner(board) == "O"):
                return -1
        else:
            return 0


def minimax(board):

    player_value = player(board)

    actions_list = []

    for action in (actions(board)):
        actions_list.append(action)

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


def max_value(board):
    if (terminal(board)):
        return utility(board)

    else:
        v = float('-inf')
        actions_list = []

        for action in (actions(board)):
            actions_list.append(action)

        for action in range(len(actions_list)):
            v = max(v, min_value(result(board, actions_list[action])))
        return v


def min_value(board):
    if (terminal(board)):
        return utility(board)

    else:
        v = float('inf')

        actions_list = []

        for action in (actions(board)):
            actions_list.append(action)

        for action in range(len(actions_list)):
            v = min(v, max_value(result(board, actions_list[action])))
        return v


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


def check_winner_vertically(board):

    lists = []

    for i in range(len(board)):
        list = []
        for j in range(len(board[i])):
            list.append(board[j][i])
        lists.append(list)

    return check_winner_horizontally(lists)


def check_winner_diagonals(board):

    first_diagonal = [board[0][0], board[1][1], board[2][2]]
    second_diagonal = [board[2][0], board[1][1], board[0][2]]

    lists = [first_diagonal, second_diagonal]

    return check_winner_horizontally(lists)


def all_options_exhausted(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == None):
                return False

    return True
