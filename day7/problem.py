import sys
import math
from collections import deque

class Formula:
    def __init__(self,result,variables):
        self.variables = variables
        self.result = result
        self.variables.reverse()
    def __str__(self):
        return str(self.result) + ' = ' + str(self.variables)

operations = [lambda x,y: x - y, lambda x,y: x // y,lambda x,y : int(str(x)[:-len(str(y))])]
check = [lambda x,y: x > y, lambda x,y: x % y == 0,lambda x,y : str(x).endswith(str(y),1)]


def checkOperations(currentRes,variables):
    if len(variables) == 0:
        raise Exception("No variables")
    if len(variables) == 1:
        return  currentRes == variables[0]
    if currentRes < variables[0] or currentRes < 0 or len(str(currentRes)) < len(str(variables[0])):
        return False
    correctOps = []
    if check[0](currentRes,variables[0]):
        correctOps.append(operations[0](currentRes,variables[0]))
    if check[1](currentRes,variables[0]):
        correctOps.append(operations[1](currentRes,variables[0]))
    if check[2](currentRes,variables[0]):
        correctOps.append(operations[2](currentRes,variables[0]))
    return any([checkOperations(x,variables[1:]) for x in correctOps]) if len(correctOps)> 0 else False


def main1(fileInput):
    formulas = []
    result = 0
    with open(fileInput, 'r') as file:
        #Process until the end of the first part
        for line in file:
            l = line.strip('\n').split(':')
            formulas.append(Formula(int(l[0]),[int(x) for x in filter(lambda x: x != '',l[1].split(' '))]))
    for f in formulas:
        if checkOperations(f.result,f.variables):
            result += f.result
    print(result)

                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
