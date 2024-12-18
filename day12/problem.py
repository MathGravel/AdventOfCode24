import sys
import numpy as np
import re
from functools import reduce
from collections import deque

positions = [[-1,0],[0,-1],[0,1],[1,0]]

def main1(inputFile):
    data = []
    blinks = []
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        for line in file:
            l = line.strip('\n')
            data.append([x for x in l])
    visited = [[False for x in range(len(data[y]))]for y in range(len(data))]
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if not visited[i][j]:
                #We start the iteration
                queue = deque()
                queue.append([i,j])
                letter = data[i][j]
                perimeters = []
                while queue:
                    loc = queue.popleft()
                    #print(loc)
                    if not visited[loc[0]][loc[1]] and letter == data[loc[0]][loc[1]]:
                        visited[loc[0]][loc[1]] = True
                        perimeters.append([loc[0],loc[1]])
                        if  loc[1]+1 < len(data[i]):
                            queue.append([loc[0],loc[1]+1])
                        if loc[1]-1 >= 0:
                            queue.append([loc[0],loc[1]-1])
                        if  loc[0]+1 < len(data):
                            queue.append([loc[0]+1,loc[1]])
                        if loc[0]-1 >= 0:
                            queue.append([loc[0]-1,loc[1]])
                aire = 0
                perimetre = 0
                for loc in perimeters:
                    aire+=1
                    add = 4
                    for pos in [[0,1],[0,-1],[-1,0],[1,0]]:
                        if [loc[0] + pos[0],loc[1]+pos[1]] in perimeters:
                            add -= 1
                    perimetre += add
                total = total+ (aire * perimetre)
                
    print(total)


def main2(inputFile):
    data = []
    blinks = []
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        for line in file:
            l = line.strip('\n')
            data.append([x for x in l])
    visited = [[False for x in range(len(data[y]))]for y in range(len(data))]
    #print(visited)
    #perimeters = {}
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if not visited[i][j]:
                #We start the iteration
                queue = deque()
                queue.append([i,j])
                letter = data[i][j]
                perimeters = []
                while queue:
                    loc = queue.popleft()
                    #print(loc)
                    if not visited[loc[0]][loc[1]] and letter == data[loc[0]][loc[1]]:
                        visited[loc[0]][loc[1]] = True
                        perimeters.append([loc[0],loc[1]])
                        if  loc[1]+1 < len(data[i]):
                            queue.append([loc[0],loc[1]+1])
                        if loc[1]-1 >= 0:
                            queue.append([loc[0],loc[1]-1])
                        if  loc[0]+1 < len(data):
                            queue.append([loc[0]+1,loc[1]])
                        if loc[0]-1 >= 0:
                            queue.append([loc[0]-1,loc[1]])
                aire = 0
                perimetre = 0
                fourSides = [[[False,False,False,False] for x in range(len(data[y]))] for y in range(len(data))]
                m = -1
                for loc in perimeters:
                    aire+=1
                    m+= 1
                    i = loc[0]
                    j = loc[1]
                    add = 0
                    if not fourSides[i][j][0] :
                        add+=1
                        while i < len(data):
                            fourSides[i][j][0] = True
                            i+=1
                    i = loc[0]
                    j = loc[1]
                    if not fourSides[i][j][1] :
                        add+=1
                        while i >= 0:
                            fourSides[i][j][1] = True
                            i-=1
                    i = loc[0]
                    j = loc[1]
                    if not fourSides[i][j][2] :
                        add+=1
                        while j < len(data):
                            fourSides[i][j][2] = True
                            j+=1
                    i = loc[0]
                    j = loc[1]
                    if not fourSides[i][j][3] :
                        add+=1
                        while j < len(data):
                            fourSides[i][j][3] = True
                            j+=1
                    perimetre += add
                total = total + ( aire * perimetre)
                print("Pour {} tu as le perimetre {} et l'aire {}".format(letter,perimetre,aire))
                
    print(total)




if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
        main2(sys.argv[1])
