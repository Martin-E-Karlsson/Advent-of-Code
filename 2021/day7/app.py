import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, string_to_int
import timeit

Data = string_to_int(read_txt_file('2021/day7/data.txt')[0].split(','))
TestData = string_to_int(read_txt_file('2021/day7/testdata.txt')[0].split(','))


def calculate_total_difference(numberList, target):
    # print(sum([abs(number-target) for number in numberList]))
    return sum([abs(number-target) for number in numberList])


def calculate_total_acceleration_difference_fast(numberList, target):
    return sum([quick_number_sum(number, target) for number in numberList])

def calculate_total_acceleration_difference_slow(numberList, target):
    return sum([slow_number_sum(number, target) for number in numberList])

def slow_number_sum(number1, number2):
    difference = abs(number1 - number2)
    return sum([x for x in range(1, difference+1)])

def quick_number_sum(number1, number2):
    diff = abs(number1 - number2)
    return int(diff*(diff+1)/2)


if __name__=="__main__":
    positionList = sorted(Data)
    # # print(positionLicst)
    # diffTotalList = [calculate_total_difference(positionList, target) for target in range(positionList[0], positionList[-1]+1)]
    start = timeit.default_timer()
    diffTotalList = [calculate_total_acceleration_difference_fast(positionList, target) for target in range(positionList[0], positionList[-1]+1)]    
    stop = timeit.default_timer()
    print(sorted(diffTotalList)[0])
    print('Time: ', stop - start)
    # start = timeit.default_timer() 
    # diffTotalList = [calculate_total_acceleration_difference_slow(positionList, target) for target in range(positionList[0], positionList[-1]+1)]    
    # stop = timeit.default_timer()
    # print(sorted(diffTotalList)[0])
    # print('Time: ', stop - start)