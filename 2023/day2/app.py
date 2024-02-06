import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2023/day2/data.txt'))
TestData = remove_line_breaks(read_txt_file('2023/day2/testdata.txt'))
CubeDict = {'red': 12, 'green': 13, 'blue': 14}

def examine_game(gameString):
    game, results = gameString.split(':')
    gameNumber = [int(i) for i in game.split() if i.isdigit()][0]
    splitResults = results.split((';'))
    resultDict = {}
    for i, result in enumerate(splitResults):
        resultDict[i] = result.split(',')
    for key in resultDict.keys():
        for cubeNumber in resultDict[key]:
            if [int(i) for i in cubeNumber.split() if i.isdigit()][0] > CubeDict[cubeNumber.split()[1]]:
                return 0
    return gameNumber

def calculate_power(game):
    results = game.split(':')[1:][0].split(';')
    rgbList = [1, 1, 1]
    for set in results:
        for cubes in set.split(','):
            number = int(cubes[:3].strip())
            color = cubes[3:].strip()
            if color == 'red':
                if number > rgbList[0]:
                    rgbList[0] = number
            elif color == 'green':
                if number > rgbList[1]:
                    rgbList[1] = number
            elif color == 'blue':
                if number > rgbList[2]:
                    rgbList[2] = number
            else:
                print('COLOR ERROR:', [color])     
    return rgbList[0] * rgbList[1] * rgbList[2]

def summarize_all_games(data):
    total = 0
    for game in data:
        total += calculate_power(game)
    return total

if __name__=="__main__":
    # answer = sum([examine_game(game) for game in Data])
    # print(answer)
    print(summarize_all_games(Data))