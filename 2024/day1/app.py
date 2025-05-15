import sys
sys.path.append('C:/Code/Advent-of-Code/2024/utils')
from utils import read_txt_file_as_string

Data = read_txt_file_as_string('2024/day1/data.txt')
TestData = '''3   4
4   3
2   5
1   3
3   9
3   3'''

def calc_distance(doubleList):
    totalDistance = 0
    for index in range(len(doubleList[0])):
        totalDistance += (abs(doubleList[0][index]-doubleList[1][index]))
    return totalDistance

def calc_similiraity_score(doubleList):
    similiratyScore = 0
    for firstNumber in doubleList[0]:
        multiplier = 0
        for secondNumber in doubleList[1]:
            if firstNumber == secondNumber:
                multiplier += 1
        similiratyScore += firstNumber * multiplier
    return similiratyScore

def split_string_to_double_int_list(str):
    firstHalf, secondHalf = [], []
    for pair in str.split('\n'):
        firstHalf.append(int(pair.split()[0]))
        secondHalf.append(int(pair.split()[1]))
    firstHalf.sort()
    secondHalf.sort()
    return [firstHalf, secondHalf]  


if __name__=="__main__":
    data = Data
    print(data)
    data = split_string_to_double_int_list(data)
    # totalDistance = calc_distance(data)
    # print(totalDistance)
    print(calc_similiraity_score(data))
