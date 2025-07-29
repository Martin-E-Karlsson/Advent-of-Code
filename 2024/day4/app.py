import sys
sys.path.append('C:/Code/Advent-of-Code/2024/utils')
from utils import read_txt_file_as_string

Data = read_txt_file_as_string('2024/day4/data.txt').split('\n')
TestData = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''.split('\n')


def find_number_of_xmas(matrix):
    xmasTotal = 0
    for y, row in enumerate(matrix):
            for x, letter in enumerate(row):
                if letter == 'X':
                    #Check north
                    if y >= 3:
                        if matrix[y-1][x] + matrix[y-2][x] + matrix[y-3][x] == 'MAS':
                            xmasTotal += 1
                            print('N:', letter + matrix[y-1][x] + matrix[y-2][x] + matrix[y-3][x])
                    #Check north east
                    if y >= 3 and len(row)-x > 3:
                        if matrix[y-1][x+1] + matrix[y-2][x+2] + matrix[y-3][x+3] == 'MAS':
                            xmasTotal += 1
                            print('NE', letter + matrix[y-1][x+1] + matrix[y-2][x+2] + matrix[y-3][x+3])
                    #Check east
                    if len(row)-x > 3:
                        if matrix[y][x+1] + matrix[y][x+2] + matrix[y][x+3] == 'MAS':
                            xmasTotal += 1
                            print('E', letter + matrix[y][x+1] + matrix[y][x+2] + matrix[y][x+3])
                    #Check south east
                    if len(matrix)-y > 3 and len(row)-x > 3:
                        if matrix[y+1][x+1] + matrix[y+2][x+2] + matrix[y+3][x+3] == 'MAS':
                            xmasTotal += 1
                            print('SE', letter + matrix[y+1][x+1] + matrix[y+2][x+2] + matrix[y+3][x+3])
                    #Check south
                    if len(matrix)-y > 3:
                        if matrix[y+1][x] + matrix[y+2][x] + matrix[y+3][x] == 'MAS':
                            xmasTotal += 1
                            print('S', letter + matrix[y+1][x] + matrix[y+2][x] + matrix[y+3][x])
                    #Check south west
                    if len(matrix)-y > 3 and x >= 3:
                        if matrix[y+1][x-1] + matrix[y+2][x-2] + matrix[y+3][x-3] == 'MAS':
                            xmasTotal += 1
                            print('SW', letter + matrix[y+1][x-1] + matrix[y+2][x-2] + matrix[y+3][x-3])
                    #Check west
                    if x >= 3:
                        if matrix[y][x-1] + matrix[y][x-2] + matrix[y][x-3] == 'MAS':
                            xmasTotal += 1
                            print('W', letter + matrix[y][x-1] + matrix[y][x-2] + matrix[y][x-3])
                    #Check north west
                    if y >= 3 and x >= 3:
                        if matrix[y-1][x-1] + matrix[y-2][x-2] + matrix[y-3][x-3] == 'MAS':
                            xmasTotal += 1
                            print('NW', letter + matrix[y-1][x-1] + matrix[y-2][x-2] + matrix[y-3][x-3])
    return xmasTotal

def find_number_of_xMas(matrix):
    xMasTotal = 0
    for y, row in enumerate(matrix):
            for x, letter in enumerate(row):
                if letter == 'A':
                    if y>0 and y+1<len(matrix) and x>0 and x+1<len(row):
                        seDiagonal = ''.join(sorted(matrix[y-1][x-1] + matrix[y+1][x+1]))
                        neDiagonal = ''.join(sorted(matrix[y+1][x-1] + matrix[y-1][x+1]))
                        if seDiagonal == 'MS' and neDiagonal == 'MS':
                            xMasTotal += 1
    return xMasTotal             


if __name__ == "__main__":
    data = Data
    print(find_number_of_xMas(data))