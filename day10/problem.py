import sys
import numpy as np
import re
from functools import reduce
from collections import deque

positions = [[-1,0],[0,-1],[0,1],[1,0]]

def main1(inputFile):
    data = []
    startingPositions = []
    totalRoads = 0
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        i = 0
        for line in file:
            l = line.strip('\n')
            data.append([int(x) for x in l])
            posY = reduce(lambda x, y: x + [y.start()], re.finditer('0', line) , [])
            startingPositions.extend(zip([i] * len(posY), posY)) 
            i += 1

    for pos in startingPositions:
        cur = parcoursProfondeurIteratif(data,pos,0)
        print(cur)
        totalRoads += cur
    print(totalRoads)


def parcoursProfondeurIteratif(data, currentPos,id ):
    queue = deque()
    queue.append(currentPos)
    n = len(data)
    count = 0
    visited = []
    while (queue):
        posi = queue.pop()
        if  (posi not in visited ) and data[posi[0]][posi[1]] == 9:
            count+=1
            visited.append(posi)
            continue
        id = data[posi[0]][posi[1]]
        id+=1
        for pos in positions:
            if  (-1 < posi[0]+pos[0] < n) and (-1 < posi[1]+pos[1] < n) and (id  == (data[posi[0]+pos[0]][posi[1]+pos[1]])):
                queue.append([posi[0]+pos[0],posi[1]+pos[1]])
    print(visited)
    return count

def main2(inputFile):
    data = []
    startingPositions = []
    totalRoads = 0
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        i = 0
        for line in file:
            l = line.strip('\n')
            data.append([int(x) for x in l])
            posY = reduce(lambda x, y: x + [y.start()], re.finditer('0', line) , [])
            startingPositions.extend(zip([i] * len(posY), posY)) 
            i += 1

    for pos in startingPositions:
        cur = parcoursProfondeurIteratif2(data,pos,0)
        print(cur)
        totalRoads += cur
    print(totalRoads)


def parcoursProfondeurIteratif2(data, currentPos,id ):
    queue = deque()
    queue.append(currentPos)
    n = len(data)
    count = 0
    visited = []
    while (queue):
        posi = queue.pop()
        if  data[posi[0]][posi[1]] == 9:
            count+=1
            visited.append(posi)
            continue
        id = data[posi[0]][posi[1]]
        id+=1
        for pos in positions:
            if  (-1 < posi[0]+pos[0] < n) and (-1 < posi[1]+pos[1] < n) and (id  == (data[posi[0]+pos[0]][posi[1]+pos[1]])):
                queue.append([posi[0]+pos[0],posi[1]+pos[1]])
    print(visited)
    return count


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
        main2(sys.argv[1])
