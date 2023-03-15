import numpy as np
import sys
sys.path.append('C:/Code/advent_of_code/2021/utils')
from utils import read_txt_file, string_to_int

Data = string_to_int(read_txt_file('2021/day7/data.txt')[0].split(','))
TestData = string_to_int(read_txt_file('2021/day7/testdata.txt')[0].split(','))


def calculate_total_difference(numberList, target):
    # print(sum([abs(number-target) for number in numberList]))
    return sum([abs(number-target) for number in numberList])


if __name__=="__main__":
    positionList = sorted(Data)
    # print(positionLicst)
    diffTotalList = [calculate_total_difference(positionList, target) for target in range(positionList[0], positionList[-1]+1)]
    # print(diffTotalList)
    print(sorted(diffTotalList)[0])