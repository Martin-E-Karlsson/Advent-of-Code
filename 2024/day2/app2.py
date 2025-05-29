#This code is based on the code I wrote in app.py but has been effectiveized by Copilot.
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

    for currentLevel, nextLevel in zip(report, report[1:]):
        diff = currentLevel - nextLevel
        if 0 < abs(diff) < 4:
            if (diff > 0 and increasing) or (diff < 0 and decreasing):
                return check_report_variants(report)
        else:
            return check_report_variants(report)
    return 1

def check_report_variants(report):
    for i in range(len(report)):
        variant = report[:i] + report[i+1:]
        increasing = variant[0] < variant[1]
        decreasing = variant[0] > variant[1]

        for currentLevel, nextLevel in zip(variant, variant[1:]):
            diff = currentLevel - nextLevel
            if 0 < abs(diff) < 4:
                if (diff > 0 and increasing) or (diff < 0 and decreasing):
                    break
            else:
                break
        else:
            return 1  # Safe variant found
    return 0

def summarize_reports(data):
    numberOfSafeLevels = 0
    for report in data:
        numberOfSafeLevels += check_report(report)
    return numberOfSafeLevels



if __name__=="__main__":
    dataString = Data
    dataList = [[int(number) for number in row.split()] for row in dataString.split('\n')]
    print(dataList)
    print(summarize_reports(dataList))