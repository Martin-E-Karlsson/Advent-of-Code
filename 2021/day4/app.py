import numpy as np

def read_txt_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def remove_line_breaks(bingoData):
    return [row.replace('\n','') for row in bingoData if row!='\n']

def separate_bingo_data(bingoData):
    bingoNumbers = string_to_int(bingoData[0].split(','))
    bingoBoards = []
    currentBoard = []
    for row in bingoData[1:]:
        currentBoard.append(string_to_int(row.split()))
        if len(currentBoard) >= 5:
            bingoBoards.append(currentBoard)
            currentBoard = []
    return bingoNumbers, bingoBoards


def string_to_int(stringList):
    return [int(string) for string in stringList]


def check_bingo_numbers(bingoNumbers, bingoBoards):
    numberOfBoards = len(bingoBoards)
    checkBoards = [np.zeros((5, 5)) for board in range(numberOfBoards)]
    for bingoNumber in bingoNumbers:
        for boardIndex, board in enumerate(bingoBoards):
            for y, row in enumerate(board):
                for x, boardNumber in enumerate(row):
                    if bingoNumber == boardNumber:
                        checkBoards[boardIndex][y][x] = 1
        bingoFound, winningBoardIndex = check_for_bingo(checkBoards)
        if bingoFound:
            print("Winning check board")
            print_matrix(checkBoards[winningBoardIndex])
            print("Winning bingo board")
            print_matrix(bingoBoards[winningBoardIndex])
            return bingoBoards[winningBoardIndex], checkBoards[winningBoardIndex], bingoNumber

def check_for_bingo(checkBoards):
    for boardIndex, board in enumerate(checkBoards):
        #Check rows
        for row in board:
            if sum(row) >= 5:
                return True, boardIndex
        #Check columns
        columnSumList = [sum(x) for x in zip(*board)]
        for columnSum in columnSumList:
            if columnSum >= 5:
                return True, boardIndex
        #Check diagonals
        mainDiagonalSum = sum([board[i][i] for i in range(5)])
        antiDiagonalSum = sum([board[4-i][0+i] for i in range(5)])
        if mainDiagonalSum >= 5 or antiDiagonalSum >= 5:
            return True, boardIndex
    return False, boardIndex


def print_matrix(matrix):
    for row in matrix:
        print(row)


def get_unmarked_sum(bingoBoard, checkBoard):
    boardSum = 0
    for x in range(5):
        for y in range(5):
            if checkBoard[x][y] == 0:
                boardSum += bingoBoard[x][y]
    return boardSum


if __name__=="__main__":
    bingoData = read_txt_file('2021/day4/data.txt')
    bingoData = remove_line_breaks(bingoData)
    bingoNumbers, bingoBoards = separate_bingo_data(bingoData)
    # print(bingoNumbers)
    # print(len(bingoBoards))
    winningBoard, checkBoard, lastCalledNumber = check_bingo_numbers(bingoNumbers, bingoBoards)
    unmarkedSum = get_unmarked_sum(winningBoard, checkBoard)
    print("Final Score:", unmarkedSum * lastCalledNumber)
