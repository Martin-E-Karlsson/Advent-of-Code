import numpy as np
import sys
sys.path.append('C:/Code/advent_of_code/2021/utils')
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

def create_fish_dict(fishList):
    fishDict = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    for fish in fishList:
        fishDict[str(fish)] += 1
    return fishDict


def update_fish_dict(fishDict):
    return {
        '0':fishDict['1'],
        '1':fishDict['2'],
        '2':fishDict['3'],
        '3':fishDict['4'],
        '4':fishDict['5'],
        '5':fishDict['6'],
        '6':fishDict['7'] + fishDict['0'],
        '7':fishDict['8'],
        '8':fishDict['0']
        }   


if __name__=="__main__":
    fishDict = create_fish_dict(Data)
    for i in range(256):
        # update_fish_population(Data)
        fishDict = update_fish_dict(fishDict)
    # print(len(Data))
    print(sum([fishDict[fishKey] for fishKey in fishDict.keys()]))