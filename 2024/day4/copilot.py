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
    directions = [
        (-1, 0),  # N
        (-1, 1),  # NE
        (0, 1),   # E
        (1, 1),   # SE
        (1, 0),   # S
        (1, -1),  # SW
        (0, -1),  # W
        (-1, -1), # NW
    ]
    xmasTotal = 0
    for y, row in enumerate(matrix):
        for x, letter in enumerate(row):
            if letter == 'X':
                for dy, dx in directions:
                    try:
                        if all(
                            0 <= y + dy * i < len(matrix) and
                            0 <= x + dx * i < len(row)
                            for i in range(1, 4)
                        ):
                            if (
                                matrix[y + dy * 1][x + dx * 1] +
                                matrix[y + dy * 2][x + dx * 2] +
                                matrix[y + dy * 3][x + dx * 3]
                            ) == 'MAS':
                                xmasTotal += 1
                    except IndexError:
                        continue
    return xmasTotal

def find_number_of_xMas(matrix):
    xMasTotal = 0
    for y, row in enumerate(matrix):
        for x, letter in enumerate(row):
            if letter == 'A':
                if (
                    0 < y < len(matrix) - 1 and
                    0 < x < len(row) - 1
                ):
                    se = {matrix[y-1][x-1], matrix[y+1][x+1]}
                    ne = {matrix[y+1][x-1], matrix[y-1][x+1]}
                    if se == {'M', 'S'} and ne == {'M', 'S'}:
                        xMasTotal += 1
    return xMasTotal

if __name__ == "__main__":
    data = Data
    print(find_number_of_xMas(data))