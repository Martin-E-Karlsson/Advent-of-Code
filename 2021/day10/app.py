import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2021/day10/data.txt'))
TestData = remove_line_breaks(read_txt_file('2021/day10/testdata.txt'))

LeftList = ['(', '[', '{', '<']
RightList = [')', ']', '}', '>']
PairList = ['()', '[]', '{}', '<>']
PairingDict = {')': '(', ']': '[', '}': '{', '>': '<'}
SyntaxErrorScoringDict = {')': 3, ']': 57, '}': 1197, '>': 25137}
AutoCompleteScoringDict = {'(': 1, '[': 2, '{': 3, '<': 4}


def get_syntax_error_score(subsystemLines):
    illegalCharList = []
    for line in subsystemLines:
        illegalChar = find_illegal_chacters(line)
        if illegalChar:
            illegalCharList.append(illegalChar)
    return sum([SyntaxErrorScoringDict[char] for char in illegalCharList])


def find_illegal_chacters(line):
    for index, char in enumerate(line):
        if char in RightList:
            slice = line[:index+1]
            pairFound = True
            while pairFound:
                pairFound = False
                for pair in PairList:
                    if pair in slice:
                        slice = slice.replace(pair, '')
                        pairFound = True
            if slice and slice[-1] in RightList:
                return char
    return ''


def find_the_middle_completion_score(subsystemLines):
    autocompleteScores = []
    for line in subsystemLines.copy():
        if not find_illegal_chacters(line):
            incompleteChars = remove_complete_pairs(line)
            autocompleteScores.append(calculate_autocomplete_score(incompleteChars))
    return sorted(autocompleteScores)[int(len(autocompleteScores)/2)]


def remove_complete_pairs(line):
    oldLineLength = len(line) + 1
    while len(line) < oldLineLength:
        oldLineLength = len(line)
        for pair in PairList:
            line = line.replace(pair, '')
    return line
    


def calculate_autocomplete_score(incompleteChars):
    score = 0
    for char in incompleteChars[::-1]:
        score *= 5
        score += AutoCompleteScoringDict[char]
    return score



if __name__=="__main__":
    # print(get_syntax_error_score(Data))
    print(find_the_middle_completion_score(Data))