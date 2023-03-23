import numpy as np
import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_list_to_int_matrix

Data = string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day9/data.txt')))
TestData = string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day9/testdata.txt')))

def get_risk_level_sum(heightMap):
    riskLevelSum = 0
    for y, row in enumerate(heightMap):
        for x, position in enumerate(row):
            neighbors = []
            if y > 0:
                neighbors.append(heightMap[y-1][x])
            
            if x < len(row)-1:
                neighbors.append(heightMap[y][x+1])
            
            if y < len(heightMap)-1:
                neighbors.append(heightMap[y+1][x])
            
            if x > 0:
                neighbors.append(heightMap[y][x-1])
            
            if position < sorted(neighbors)[0]:
                riskLevelSum += position + 1
    
    return riskLevelSum


def get_top_3_basin_product(heightMap):
    basinPositions = find_basin_positions(heightMap)
    basinAreaPositions = find_basin_area_positions(basinPositions)
    basinAreas = sorted([len(area) for area in basinAreaPositions])
    return basinAreas[-1] * basinAreas[-2] * basinAreas[-3]


def find_basin_positions(heightMap):
    basinPositions = []
    for y, row in enumerate(heightMap):
        for x, position in enumerate(row):
            if position < 9:
                basinPositions.append([x, y])
    return basinPositions


def find_basin_area_positions(basinPositions):
    basinAreaPositions = []
    while len(basinPositions) > 0:
        area = [basinPositions.pop(0)]
        areaSize = 0
        while len(area) > areaSize:
            areaSize = len(area)
            for aPos in area:
                for bPosIndex, bPos in enumerate(basinPositions):
                    if aPos[0] == bPos[0] and abs(aPos[1]-bPos[1]) == 1:
                        area.append(basinPositions.pop(bPosIndex))
                    elif aPos[1] == bPos[1] and abs(aPos[0]-bPos[0]) == 1:
                        area.append(basinPositions.pop(bPosIndex))
        basinAreaPositions.append(area)
    return basinAreaPositions


if __name__=="__main__":
    # print('The sum of all low point risk levels are:', get_risk_level_sum(Data))
    print('The product of the three largest basin areas are:', get_top_3_basin_product(Data))