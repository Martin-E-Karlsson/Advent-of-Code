import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2021/day8/data.txt'))
TestData = remove_line_breaks(read_txt_file('2021/day8/testdata.txt'))


def extract_input_and_output_signal(signalList):
    return [signal.split('|')[0] for signal in signalList], [signal.split('|')[1] for signal in signalList]

def create_signal_dict(inputSignalList, outputSignalList):
    signalDict = {}
    for index in range(len(inputSignalList)):
        signalDict[f'signal{index+1}'] = {
            'Input Signal': [''.join(sorted(digit)) for digit in inputSignalList[index].split()],
            'Output Signal': [''.join(sorted(digit)) for digit in outputSignalList[index].split()]
            }
    return signalDict

def decrypt_input_signal(inputSignal):
    decrypKey = ['' for _ in range(10)]

    # Find the simple digits
    for digit in inputSignal.copy():
        if len(digit) == 2:
            decrypKey[1] = digit
            inputSignal.remove(digit)
        elif len(digit) == 3:
            decrypKey[7] = digit
            inputSignal.remove(digit)
        elif len(digit) == 4:
            decrypKey[4] = digit
            inputSignal.remove(digit)
        elif len(digit) == 7:
            decrypKey[8] = digit
            inputSignal.remove(digit)

    # Find 3 and 6
    for digit in inputSignal.copy():
        if len(digit) == 5:
            if decrypKey[1][0] in digit and decrypKey[1][1] in digit:
                decrypKey[3] = digit
                inputSignal.remove(digit)
        elif len(digit) == 6:
            if not decrypKey[1][0] in digit or not decrypKey[1][1] in digit:
                decrypKey[6] = digit
                inputSignal.remove(digit)

    # Find 9
    for digit in inputSignal.copy():
        if  decrypKey[3][0] in digit and decrypKey[3][1] in digit and decrypKey[3][2] in digit and decrypKey[3][3] in digit and decrypKey[3][4] in digit:
            decrypKey[9] = digit
            inputSignal.remove(digit)

    # Find 0 and 5
    for digit in inputSignal.copy():
        if len(digit) == 6:
            decrypKey[0] = digit
            inputSignal.remove(digit)
        elif digit[0] in decrypKey[6] and digit[1] in decrypKey[6] and digit[2] in decrypKey[6] and digit[3] in decrypKey[6] and digit[4] in decrypKey[6]:
            decrypKey[5] = digit
            inputSignal.remove(digit)

    # Only 2 remains
    decrypKey[2] = inputSignal[0]
    return decrypKey

def unpack_digits(signalList):
    return [signal for signalGroup in [signalGroup.split() for signalGroup in signalList] for signal in signalGroup]

def count_simple_digits(signalList):
    return len([signal for signal in signalList if len(signal) in [2, 3, 4, 7]])

def get_output_value(decrypKey, outputSignal):
    return int(''.join([str(decrypKey.index(digit)) for digit in outputSignal]))

def get_output_sum(signalDict):
    outputSum = 0
    for signal in signalDict.values():
        decrypKey = decrypt_input_signal(signal['Input Signal'])
        outputSum += get_output_value(decrypKey, signal['Output Signal'])
    return outputSum

if __name__=="__main__":
    inputSignals, outputSignals = extract_input_and_output_signal(Data)
    # unpackedOutputDigits = unpack_digits(outputSignals)
    # simpleDigitSum = count_simple_digits(unpackedOutputDigits)
    signalDict = create_signal_dict(inputSignals, outputSignals)
    # for value in signalDict.values():
    #     print(value)
    print(get_output_sum(signalDict))
   

    