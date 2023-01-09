def read_txt_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def remove_line_breaks(bingoData):
    return [row.replace('\n','') for row in bingoData if row!='\n']


def string_to_int(stringList):
    return [int(string) for string in stringList]


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