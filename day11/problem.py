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
            data = [int(x) for x in l.split(' ')]
    #print(data)
    for i in range(25):
        j = 0
        newData = []
        while j < len(data):
            if data[j] == 0:
                newData.append(1)
            elif len(str(data[j])) % 2 == 0:
                middle = len(str(data[j]))//2
                
                newData.append(int(str(data[j])[:middle]))
                newData.append(int(str(data[j])[middle:]))
            else:
                newData.append(2024 * data[j])
            j+=1
        #print(newData)
        data = newData
    print(len(data))



def main2(inputFile):
    data = []
    ndict = {}
    blinks = []
    # using reduce() to get start indices of all occurrences 
    with open(inputFile, 'r') as file:
        for line in file:
            l = line.strip('\n')
            data = [int(x) for x in l.split(' ')]
            for x in data:
                ndict[x] = ndict.get(x,0) + 1
    print(ndict)
    for i in range(75):
        nDictMod = {}
        nDictLost = {}
        #print(i)
        for key,value in ndict.items():
            if value <= 0:
                continue
            size = len(str(key)) 
            if key == 0:
                nDictLost[0] = nDictLost.get(0,0) + value
                nDictMod[1] = nDictMod.get(1,0) + value
            elif size % 2 == 0:
                left = int(str(key)[size//2:])
                right = int(str(key)[:size//2])
                nDictMod[left] = nDictMod.get(left,0) +value
                nDictMod[right] = nDictMod.get(right,0) +value
                nDictLost[key] = nDictLost.get(key,0)+value
            else:
                nDictMod[key * 2024] = nDictMod.get(key * 2024,0) +value
                nDictLost[key] = nDictLost.get(key,0)+value
        
        for kkey,modifications in nDictMod.items():
            ndict[kkey] = ndict.get(kkey,0) + modifications
        for kkey,modifications in nDictLost.items():
            ndict[kkey] = ndict.get(kkey,0) - modifications
        #print(ndict)
    total = 0
    l = 0
    for values in ndict.values():
        l+=1
        total += values
    print(total)
    #print(l)
            
            





if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
        main2(sys.argv[1])
