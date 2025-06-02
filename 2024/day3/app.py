import sys, re
sys.path.append('C:/Code/Advent-of-Code/2024/utils')
from utils import read_txt_file_as_string

Data = read_txt_file_as_string('2024/day3/data.txt')
TestData = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

def remove_disabled_instructions(dataString):
    while "don't()" in dataString:
        dontIndex = dataString.find("don't()")
        if "do()" in dataString[dontIndex:]:
            doIndex = dontIndex + dataString[dontIndex:].find("do()")+ len("do()")
            dataString = dataString[:dontIndex] + dataString[doIndex:]
        else:
            dataString = dataString[:dontIndex]
    return dataString

def get_all_mul(dataString):
    return re.findall(r"mul\([0-9]+,[0-9]+\)",dataString)

def calculate_instructions(dataString):
    result = 0
    for instruction in get_all_mul(dataString):
        numbers = instruction[4:-1].split(',')
        result += int(numbers[0]) * int(numbers[1])
    return result
    
if __name__=="__main__":
    data = remove_disabled_instructions(Data)
    print(calculate_instructions(data))

