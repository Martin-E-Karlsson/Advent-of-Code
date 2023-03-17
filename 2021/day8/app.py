import sys
sys.path.append('C:/Code/Advent-of-Code/2021/utils')
from utils import read_txt_file, remove_line_breaks

Data = remove_line_breaks(read_txt_file('2021/day8/data.txt'))
TestData = remove_line_breaks(read_txt_file('2021/day8/testdata.txt'))

def extract_output_signal(signalList):
    return [signal.split('|')[1] for signal in signalList]

def unpack_signals(signalList):
    return [signal for signalGroup in [signalGroup.split() for signalGroup in signalList] for signal in signalGroup]

def count_simple_signals(signalList):
    return len([signal for signal in signalList if len(signal) in [2, 3, 4, 7]])

if __name__=="__main__":
    outputSignals = unpack_signals(extract_output_signal(Data))
    print(count_simple_signals(outputSignals))
    