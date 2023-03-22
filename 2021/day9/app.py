import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_list_to_int_matrix

Data = string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day9/data.txt')))
TestData = string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day9/testdata.txt')))

def get_risk_level_sum(heightMap):
    riskLevelSum = 0
    for y, row in enumerate(heightMap):
        for x, location in enumerate(row):
            neighbors = []
            if y > 0:
                neighbors.append(heightMap[y-1][x])
            
            if x < len(row)-1:
                neighbors.append(heightMap[y][x+1])
            
            if y < len(heightMap)-1:
                neighbors.append(heightMap[y+1][x])
            
            if x > 0:
                neighbors.append(heightMap[y][x-1])
            
            if location < sorted(neighbors)[0]:
                riskLevelSum += location + 1
    
    return riskLevelSum





if __name__=="__main__":
    print('The sum of all low point risk levels are:', get_risk_level_sum(Data))