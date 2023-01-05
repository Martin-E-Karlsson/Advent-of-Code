import numpy as np

possibleBingoRows = [[]]

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
                        # print(bingoNumber, boardNumber, boardIndex)
                        checkBoards[boardIndex][y][x] = 1
        bingoFound, winningBoardIndex = check_for_bingo(checkBoards)
        if bingoFound:
            break
    print(checkBoards[0])
    return winningBoardIndex

def check_for_bingo(checkBoards):
    for boardIndex, board in enumerate(checkBoards):
        pass
    return 0, 0




if __name__=="__main__":
    bingoData = read_txt_file('2021/day4/data.txt')
    bingoData = remove_line_breaks(bingoData)
    bingoNumbers, bingoBoards = separate_bingo_data(bingoData)
    # print(bingoNumbers)
    # print(len(bingoBoards))
    winningBoardIndex = check_bingo_numbers(bingoNumbers, bingoBoards)
