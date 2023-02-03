import sys
sys.path.append('/C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks, string_to_int, separate_bingo_data

TestData = remove_line_breaks(read_txt_file('2021/day4/testdata.txt'))
LineData = remove_line_breaks(read_txt_file('2021/day5/data.txt'))

if __name__=="__main__":
    print(TestData)