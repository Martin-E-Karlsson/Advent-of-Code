from contextlib import nullcontext
from data import diagnosticData
from numpy import zeros

def read_diagnostic_data(data):
    numberOfOnes, numberOfZeros = count_binary_numbers(data)
    gammaRate, epsilonRate = calculate_rates(numberOfOnes, numberOfZeros)
    return gammaRate, epsilonRate

def count_binary_numbers(data):
    numberOfZeros = zeros(12, int)
    numberOfOnes = zeros(12, int)
    for number in data.rsplit('\n'):
        for i in range(len(number)):
            if int(number[i]) == 1:
                numberOfOnes[i] += 1
            elif int(number[i]) == 0:
                numberOfZeros[i] += 1
            else:
                print('Error, unrecognized digit:', number[i])
    # print('numberOfOnes:', numberOfOnes)
    # print('numberOfZeros:', numberOfZeros)
    return numberOfOnes, numberOfZeros

def calculate_rates(numberOfOnes, numberOfZeros):
    numberOfBits = len(numberOfOnes)
    mostCommonBit = ''
    leastCommonBit = ''
    for i in range(numberOfBits):
        if numberOfOnes[i] > numberOfZeros[i]:
            mostCommonBit += '1'
            leastCommonBit += '0'
        elif numberOfOnes[i] < numberOfZeros[i]:
            mostCommonBit += '0'
            leastCommonBit += '1'
    return int(mostCommonBit, 2), int(leastCommonBit, 2)

def calculate_ratings(diagnosticData):
    data = diagnosticData.rsplit('\n')
    oxygenGeneratorRating = calculate_oxygen_generator_rating(data)
    co2ScrubberRating =  calculate_c02_scrubber_rating(data)
    lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating
    return oxygenGeneratorRating, co2ScrubberRating, lifeSupportRating

def calculate_oxygen_generator_rating(data):
    remainingNumbers = data.copy()
    for bitPosition in range(len(data[0])):
        oneBitNumbers = []
        zeroBitNumbers = []
        for number in remainingNumbers:
            if number[bitPosition] == '1':
                oneBitNumbers.append(number)
            elif number[bitPosition] == '0':
                zeroBitNumbers.append(number)
            else:
                print('Unidentified bit value')
        if len(oneBitNumbers) >= len(zeroBitNumbers):
            remainingNumbers = oneBitNumbers.copy()
        else:
            remainingNumbers = zeroBitNumbers.copy()
        if len(remainingNumbers) == 1:
            return int(remainingNumbers[0], 2)

def calculate_c02_scrubber_rating(data):
    remainingNumbers = data.copy()
    for bitPosition in range(len(data[0])):
        oneBitNumbers = []
        zeroBitNumbers = []
        for number in remainingNumbers:
            if number[bitPosition] == '1':
                oneBitNumbers.append(number)
            elif number[bitPosition] == '0':
                zeroBitNumbers.append(number)
            else:
                print('Unidentified bit value')
        if len(oneBitNumbers) >= len(zeroBitNumbers):
            remainingNumbers = zeroBitNumbers.copy()
        else:
            remainingNumbers = oneBitNumbers.copy()
        if len(remainingNumbers) == 1:
            return int(remainingNumbers[0], 2)


if __name__=="__main__":
    # gammaRate, epsilonRate = read_diagnostic_data(diagnosticData)
    # print('Gamma Rate:', gammaRate, '\nEpsilon Rate:', epsilonRate, '\nProduct Rate:', gammaRate * epsilonRate)
    oxygenGeneratorRating, co2ScrubberRating, lifeSupportRating = calculate_ratings(diagnosticData)
    print('Oxygen Generator Rating:', oxygenGeneratorRating, '\nCO2 Scrubber Rating:', co2ScrubberRating, '\nLife Support Rating:', lifeSupportRating)