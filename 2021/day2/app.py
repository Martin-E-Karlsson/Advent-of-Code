from turtle import forward
from data import moveData

def split_string(string):
    return [value for value in string.rsplit('\n')]


def count_movment_data(moveList):
    moveDict = {'forward':0, 'down':0, 'up':0}
    for move in moveList:
        if 'forward' in move:
            moveDict['forward'] += int(move[-1:])
        elif 'down' in move:
            moveDict['down'] += int(move[-1:])
        elif 'up' in move:
            moveDict['up'] += int(move[-1:])
        else:
            print(f'Error move \"{move}\" not recognized.')
    return moveDict


class Submarine:
    def __init__(self) -> None:
        self.aim = 0
        self.hPos = 0
        self.depth = 0

    def execute_move(self, command):
        moveValue = int(command[-1:])
        if 'forward' in command:
            self.hPos += moveValue
            self.depth += moveValue * self.aim
        elif 'down' in command:
            self.aim += moveValue
        elif 'up' in command:
            self.aim -= moveValue
        else:
            print(f'Error command \"{command}\" not recognized.')
    
    @property
    def final_value(self):
        return self.hPos * self.depth

    def __str__(self) -> str:
        return f"Current submarine position is:\nHorizontal Postion: {self.hPos}\nDepth: {self.depth}\nThe final score is: {self.final_value}"

    



def execute_move_list(moveList, submarine):
    for command in moveList:
        submarine.execute_move(command)

if __name__ == "__main__":
    moveList = split_string(moveData)
    # moveDict = count_movment_data(moveList)
    # distance = moveDict['forward']
    # depth = moveDict['down'] - moveDict['up']
    # print(f"New position is:\nDistance: {distance}\nDepth: {depth}")
    # print(f'The product of these values are: {distance * depth}')

    submarine = Submarine()
    execute_move_list(moveList, submarine)
    print(submarine)
    