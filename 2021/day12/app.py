import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2021/day12/data.txt'))
TestData = remove_line_breaks(read_txt_file('2021/day12/testdata.txt'))

def separate_connections(data):
    conectionList = []
    for connection in data:
        conectionList.append(connection.split('-'))
    return conectionList

def find_path(connectionList, path):
    # recursively find a path through the caves
    return find_path(connectionList, path)

def find_number_of_paths(data):
    connectionList = separate_connections(data)
    uniqueCaves = []
    pathList = []
    startConnections = []
    endConnections = []
    for connection in connectionList:
        for cave in connection:
            if cave not in uniqueCaves:
                uniqueCaves.append(cave)
        if 'start' in connection:
            startConnections.append(connection)
        if 'end' in connection:
            endConnections.append(connection)
            

    pathList.append(find_path(connectionList, ['start']))

    
    
    # for connection in connectionList:
    #     for cave in connection:
    #         if cave=='start':
    #             connectedCave = connection.pop('start')
    #             endFound = False
    #             while not endFound:
    #                 for conection in connectionList:
    #                     if connectedCave in connection:
    #                         pass

    return connectionList, uniqueCaves, startConnections, endConnections
    

if __name__=='__main__':
    cL, uC, sC, eC = find_number_of_paths(TestData)
    print('connectionList:', cL)
    print('uniqueCaves:', uC)
    print('startConnections:', sC)
    print('endConnections:', eC)