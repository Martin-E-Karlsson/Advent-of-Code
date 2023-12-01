import sys
sys.path.append('C:/Code/Advent-of-Code/2023/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2023/day1/data.txt'))
TestData = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen]']
NumbersDict = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
NumberWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
Numbers = ['1','2','3','4','5','6','7','8','9']
AllNumbers = Numbers + NumberWords

def extract_number(line):
    numbers = [char for char in line if char in Numbers]
    return int(numbers[0] + numbers[-1])

def words_to_numbers(line):
        for i in range(1,10):
            line = line.replace(NumbersDict[str(i)], str(i))
        return line

def find_first_digit(line):
    for i in range(len(line)+1):
        for number in Numbers:
            if number in line[:i]:
                return(number)
        for word in NumberWords:
            if word in line[:i]:
                return(NumbersDict[word])

def find_last_digit(line):
    for i in range(-1, len(line)*-1-1, -1):
        for number in Numbers:
            if number in line[i:]:
                return(number)
        for word in NumberWords:
            if word in line[i:]:
                return(NumbersDict[word])

def find_digit_pair(line):
    firstDigit = find_first_digit(line)
    lastDigit = find_last_digit(line)
    print(line, firstDigit, lastDigit)
    return int(firstDigit + lastDigit)

def calculate_calibration_sum(data):
    data = [find_digit_pair(line) for line in data]
    return sum(data)

if __name__=="__main__":
    print(calculate_calibration_sum(Data.copy()))
    # print(calculate_calibration_sum(TestData.copy()))
    # line = Data[3]
    # print(line)
    # line = words_to_numbers(line)
    # print(line)
    # print(extract_number(line))
    # for i in range(-1, 10*-1-1, -1):
    #     print(i)