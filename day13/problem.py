import sys
import numpy as np
import re
from functools import reduce
from collections import deque

positions = [[-1,0],[0,-1],[0,1],[1,0]]

class Problem():
    def __init__(self,xa,ya,xb,yb,prizex,prizey):
        self.xa = int(xa)
        self.ya = int(ya)
        self.xb = int(xb)
        self.yb = int(yb)
        self.prizex = int(prizex)+10000000000000
        self.prizey = int(prizey)+10000000000000
    def __str__(self):
        return f"{self.xa} {self.ya} {self.xb} {self.yb} {self.prizex} {self.prizey}"

def main1(inputFile):
    data = []
    startingPositions = []
    totalRoads = 0
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            first = lines[i].strip()
            first = first.replace(',','+').split('+')
            print(first)
            xa = first[1]
            ya = first[-1]
            second = lines[i+1].strip()
            second = second.replace(',','+').split('+')
            xb = second[1]
            yb = second[-1]
            third = lines[i+2].strip()
            third = third.replace(',','=').split('=')
            prizex = third[1]
            prizey = third[-1]
            data.append(Problem(xa,ya,xb,yb,prizex,prizey))
            i+= 4
    #Test for x 1
    total = 0
    for i in range(len(data)):
        print(f"{i} sur {len(data)-1}")
        x = data[i].prizex
        minCost = 100000000000000000000000
        y = data[i].prizey
        ac = 0
        bc = 0
        while (x > data[i].xb and y > data[i].yb):
            #Selection of the best heuristic
            x = x - data[i].xb
            y = y - data[i].yb
            bc+=1
            if (x // data[i].xa == x / data[i].xa == y // data[i].ya == y / data[i].ya):
                ac = x // data[i].xa
                minCost = min((ac * 3) + bc,minCost)
        if minCost < 100000000000000000000000:
            total+= minCost
    

    print(total)


def main2(inputFile):
    data = []
    startingPositions = []
    totalRoads = 0
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            first = lines[i].strip()
            first = first.replace(',','+').split('+')
            print(first)
            xa = first[1]
            ya = first[-1]
            second = lines[i+1].strip()
            second = second.replace(',','+').split('+')
            xb = second[1]
            yb = second[-1]
            third = lines[i+2].strip()
            third = third.replace(',','=').split('=')
            prizex = third[1]
            prizey = third[-1]
            data.append(Problem(xa,ya,xb,yb,prizex,prizey))
            i+= 4
    #Test for x 1
    total = 0
    for i in range(len(data)):
        print(f"{i} sur {len(data)-1}")
        p1 = data[i].prizex
        p2 = data[i].prizey
        ac = 0
        bc = 0
        a = (p1 * data[i].yb - p2 * data[i].xb)/(data[i].yb * data[i].xa - data[i].ya * data[i].xb)
        a = int(a)
        b = (data[i].prizex - (data[i].xa * a)) // (data[i].xb)
        b = int(b)
        print(f"{a} {b} {data[i].xa * a  + data[i].xb * b}")
        checkX = data[i].xa * a  + data[i].xb * b 
        checkY = data[i].ya * a  + data[i].yb * b 
        if checkX == data[i].prizex and checkY == data[i].prizey:
            total+= (a * 3) + b

    print(total)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        #main1(sys.argv[1])
        main2(sys.argv[1])
