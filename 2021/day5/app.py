import numpy as np
import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_to_int

TestData = remove_line_breaks(read_txt_file('2021/day5/testdata.txt'))
LineData = remove_line_breaks(read_txt_file('2021/day5/data.txt'))

def line_list_to_dict(lineList):
    lineDictList = []
    for line in lineList:
        coordList = line.split(' -> ')
        coordPair1 = string_to_int(coordList[0].split(','))
        coordPair2 = string_to_int(coordList[1].split(','))
        lineDictList.append({'x1':coordPair1[0], 'y1':coordPair1[1], 'x2':coordPair2[0], 'y2':coordPair2[1]})
    return lineDictList


def remove_diagonal_lines(lineDictList):
    filteredList = []
    for dict in lineDictList:
        if dict['x1'] == dict['x2'] or dict['y1'] == dict['y2']:
            filteredList.append(dict)
    return filteredList

def create_line_matrix(filteredList):
    lineMatrix = np.zeros((1000, 1000))
    for dict in filteredList:
        x1, y1, x2, y2 = dict['x1'], dict['y1'], dict['x2'], dict['y2']
        # print(x1, y1, '->', x2, y2)

        # Horizontal Lines
        if x1 == x2:
            if y1 > y2:
                for y in range(y2, y1+1):
                    lineMatrix[y][x1] += 1
                    
            elif y1 < y2:
                for y in range(y1, y2+1):
                    lineMatrix[y][x1] += 1
        # Vertical Lines            
        elif y1 == y2:
            if x1 > x2:
                for x in range(x2, x1+1):
                    lineMatrix[y1][x] += 1

            elif x1 < x2:
                for x in range(x1, x2+1):
                    lineMatrix[y1][x] += 1
        
        # Diagonal Lines
        elif abs(x1-x2) == abs(y1-y2):
            # Vertically decreasing line
            if y1 > y2:
                # Horizontally decreasing line
                if x1 > x2:
                    for i in range(x1-x2+1):
                        lineMatrix[y1-i][x1-i] += 1

                # Horizontally increasing line
                elif x1 < x2:
                    for i in range(x2-x1+1):
                        lineMatrix[y1-i][x1+i] += 1
            
            # Vertically increasing line
            elif y1 < y2:
                # Horizontally decreasing line
                if x1 > x2:
                    for i in range(x1-x2+1):
                        lineMatrix[y1+i][x1-i] += 1
                
                # Horizontally increasing line
                elif x1 < x2:
                    for i in range(x2-x1+1):
                        lineMatrix[y1+i][x1+i] += 1
            # print(x1, y1, '->', x2, y2)
    return lineMatrix


def count_danger_zones(lineMatrix):
    dangerZones = 0
    for row in lineMatrix:
        for coordinate in row:
            if coordinate > 1:
                dangerZones += 1
    return dangerZones


if __name__=="__main__":
    lineDictList = line_list_to_dict(LineData)
    # print(lineDictList)
    # filteredList = remove_diagonal_lines(lineDictList)
    # print(filteredList)
    lineMatrix = create_line_matrix(lineDictList)
    # print(lineMatrix)
    numberOfDangerZones = count_danger_zones(lineMatrix)
    print(f"There are {numberOfDangerZones} dangerous areas!")
