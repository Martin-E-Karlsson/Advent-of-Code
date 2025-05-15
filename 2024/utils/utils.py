def read_txt_file_as_list(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def read_txt_file_as_string(filename):
    with open(filename) as f:
        str = f.read()
    return str

def remove_line_breaks(dataString):
    return [row.replace('\n','') for row in dataString if row!='\n']

def string_to_int(stringList):
    return [int(string) for string in stringList]

def string_to_int_list(string:str):
    return [int(number) for number in string]

def string_list_to_int_matrix(stringList):
    return [string_to_int_list(string) for string in stringList]


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