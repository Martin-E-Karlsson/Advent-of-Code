import sys
sys.path.append('C:/Code/Advent-of-Code/2024/utils')
from utils import read_txt_file_as_string

Data = read_txt_file_as_string('2024/day2/data.txt')
TestData = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

def check_report(report):
    increasing = report[0] < report[1]
    decreasing = report[0] > report[1]
    unsafe = False
    
    for index in range(len(report)-1):
        currentLevel, nextLevel = report[index], report[index+1]
        if 0 < abs(currentLevel-nextLevel) < 4:
            if currentLevel > nextLevel and increasing == True:
                unsafe = True
            elif currentLevel < nextLevel and decreasing == True:
                unsafe = True
        else: 
            unsafe = True

        if unsafe:
            return check_report_variants(report)
    return 1

def check_report_variants(report):
    for index in range(len(report)):
        variant = report[:index] + report[index+1:]

        unsafe = False
        increasing = variant[0] < variant[1]
        decreasing = variant[0] > variant[1]
        
        for index in range(len(variant)-1):
            currentLevel, nextLevel = variant[index], variant[index+1]
            if 0 < abs(currentLevel-nextLevel) < 4:
                if currentLevel > nextLevel and increasing == True:
                    unsafe = True
                elif currentLevel < nextLevel and decreasing == True:
                    unsafe = True
            else: 
                unsafe = True 
        if unsafe == False:
            return 1  
    return 0

def summarize_reports(data):
    numberOfSafeLevels = 0
    for report in data:
        numberOfSafeLevels += check_report(report)
        #print(report)
        #print("Check:", check_report(report))
    return numberOfSafeLevels



if __name__=="__main__":
    dataString = Data
    dataList = [[int(number) for number in row.split()] for row in dataString.split('\n')]
    print(dataList)
    print(summarize_reports(dataList))