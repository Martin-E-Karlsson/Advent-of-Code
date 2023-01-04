from data import depthData,testData

def get_number_of_increases(data):
    previousMeasurement = 0
    numberOfIncreases = 0
    for measurement in data:
        if previousMeasurement == measurement: print("Error: ", previousMeasurement, measurement)
        if previousMeasurement and measurement > previousMeasurement:
            numberOfIncreases += 1
        # print(f"M={measurement}, PM={previousMeasurement}, #{numberOfIncreases}")
        previousMeasurement = measurement
    return numberOfIncreases

def get_number_of_decreases(data):
    previousMeasurement = 0
    numberOfDecreases = 0
    for measurement in data:
        if previousMeasurement and measurement < previousMeasurement:
            numberOfDecreases += 1
        # print(f"M={measurement}, PM={previousMeasurement}, #{numberOfIncreases}")
        previousMeasurement = measurement
    return numberOfDecreases

def create_list_of_sums(numList):
    listOfSums = []
    for i in range(len(numList)):
        if i in range(1, len(numList)-1):
            listOfSums.append(numList[i-1] + numList[i] + numList[i+1])
    return listOfSums


def split_string(string):
    return [int(value) for value in string.split()]

if __name__=="__main__":
    # print(depthData.split())
    # print(len(depthData.split()))
    splitData = split_string(depthData)
    # print(f"The depth has increased {get_number_of_increases(splitData)} times")
    # print(f"The depth has decreased {get_number_of_decreases(splitData)} times")
    sumList = create_list_of_sums(splitData)
    print(sumList)
    print(get_number_of_increases(sumList))