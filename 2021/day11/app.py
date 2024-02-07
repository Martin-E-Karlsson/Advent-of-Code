import numpy as np
import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_list_to_int_matrix

Data = np.array(string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day11/data.txt'))))
TestData = np.array(string_list_to_int_matrix(remove_line_breaks(read_txt_file('2021/day11/testdata.txt'))))

class Octopi:
    def __init__(self, eMatrix):
        self.eMatrix = eMatrix
        self.flashes = 0 

    def increase_energy_levels_repeatedly(self, repeats):
        for _ in range(repeats):
            self.increase_energy_levels()

    def increase_energy_levels(self):
        flashedPositions = []

        for y, row in enumerate(self.eMatrix):
            for x, pos in enumerate(row):
                self.eMatrix[y][x] += 1
        
        # print('------------------------------------------------------------------------------------------------------------')
        # print('After +1 increase')
        # print(self.eMatrix)
        
        flashFound = True
        while flashFound:
            flashFound = False
            for y, row in enumerate(self.eMatrix):
                for x, pos in enumerate(row):
                    if self.eMatrix[y][x] > 9 and [x, y] not in flashedPositions:
                        self.flashPosition(x,y)
                        flashedPositions.append([x, y])
                        self.flashes += 1
                        flashFound = True
        
        # print('------------------------------------------------------------------------------------------------------------')
        # print('After flash check')
        # print(self.eMatrix)

        for y, row in enumerate(self.eMatrix):
            for x, pos in enumerate(row):
                if self.eMatrix[y][x] > 9:
                    self.eMatrix[y][x] = 0
    
    def flashPosition(self, x, y):

        if y+1 <= 9: 
            self.eMatrix[y+1][x] += 1
            if x-1 >= 0:
                self.eMatrix[y+1][x-1] += 1
            if x+1 <= 9: 
                self.eMatrix[y+1][x+1] += 1

        if x-1 >= 0: 
            self.eMatrix[y][x-1] += 1
        if x+1 <= 9:
            self.eMatrix[y][x+1] += 1
        
        if y-1 >= 0:
            self.eMatrix[y-1][x] += 1
            if x-1 >= 0:
                self.eMatrix[y-1][x-1] += 1
            if x+1 <= 9: 
                self.eMatrix[y-1][x+1] += 1
        
        



if __name__=='__main__':
    octopi = Octopi(Data)
    octopi.increase_energy_levels_repeatedly(100)
    print(octopi.flashes)