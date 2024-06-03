import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2023/day2/data.txt'))
TestData = remove_line_breaks(read_txt_file('2023/day2/testdata.txt'))




if __name__=="__main__":
    print(Data)