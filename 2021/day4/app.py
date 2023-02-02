import numpy as np
import sys
sys.path.append('/C:/Code/advent_of_code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_to_int, separate_bingo_data

BingoData = remove_line_breaks(read_txt_file('2021/day4/data.txt'))
BingoNumbers, BingoBoards = separate_bingo_data(BingoData)
CheckBoards = [np.zeros((5, 5)) for board in range(100)]

def check_bingo_numbers():
    winnerFound = False
    numberOfBoards = len(BingoBoards)
    for bingoNumber in BingoNumbers:
        for boardIndex, board in enumerate(BingoBoards):
            for y, row in enumerate(board):
                for x, boardNumber in enumerate(row):
                    if bingoNumber == boardNumber:
                        CheckBoards[boardIndex][y][x] = 1
        bingoFound, winningBoardIndexes = check_for_bingo(CheckBoards)
        for index in sorted(winningBoardIndexes, reverse=True):
            if bingoFound:
                if not winnerFound:
                    print("Winning check board")
                    print_matrix(CheckBoards[index])
                    print("Winning bingo board")
                    print_matrix(BingoBoards[index])
                    winningBoard =  BingoBoards[index]
                    winningCheckBoard = CheckBoards[index]
                    winningNumber = bingoNumber
                    winnerFound = True
                if len(BingoBoards) > 1:
                    del BingoBoards[index]
                    del CheckBoards[index]
                else:
                    print("Losing check board")
                    print_matrix(CheckBoards[0])
                    print("Losing bingo board")
                    print_matrix(BingoBoards[0])
                    return bingoNumber, winningBoard, winningCheckBoard, winningNumber
            

def check_for_bingo(checkBoards):
    WinningBoardIndexes = []
    bingoFound = False
    for boardIndex, board in enumerate(checkBoards):
        #Check rows
        for row in board:
            if sum(row) >= 5:
                WinningBoardIndexes.append(boardIndex)
                bingoFound = True
        #Check columns
        columnSumList = [sum(x) for x in zip(*board)]
        for columnSum in columnSumList:
            if columnSum >= 5:
                WinningBoardIndexes.append(boardIndex)
                bingoFound = True
        #Check diagonals (APPARENTLY YOU'RE NOT SUPPOSED TO COUNT DIAGONAL LINES)
        # mainDiagonalSum = sum([board[i][i] for i in range(5)])
        # antiDiagonalSum = sum([board[4-i][0+i] for i in range(5)])
        # if mainDiagonalSum >= 5 or antiDiagonalSum >= 5:
        #     WinningBoardIndexes.append(boardIndex)
        #     bingoFound = True
    return bingoFound, WinningBoardIndexes


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
    lastBingoNumber, winningBoard, winningCheckBoard, winningNumber = check_bingo_numbers()
    unmarkedWinningSum = get_unmarked_sum(winningBoard, winningCheckBoard)
    print("Winning Board Score:", unmarkedWinningSum * winningNumber)
    unmarkedLosingSum = get_unmarked_sum(BingoBoards[0], CheckBoards[0])
    print("Losing Board Score:", unmarkedLosingSum * lastBingoNumber)