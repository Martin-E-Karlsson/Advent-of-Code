import numpy as np
import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, string_to_int

Data = string_to_int(read_txt_file('2021/day6/data.txt')[0].split(','))
TestData = string_to_int(read_txt_file('2021/day6/testdata.txt')[0].split(','))

def update_fish_population(fishList):
    for index in range(len(fishList)):
        if fishList[index] == 0:
            fishList[index] = 6
            fishList.append(8)
        else:
            fishList[index] -= 1
        

if __name__=="__main__":
    for _ in range(80):
        update_fish_population(Data)
    print(len(Data))