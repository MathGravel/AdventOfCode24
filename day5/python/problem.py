import sys
import math
from collections import deque
def main1(fileInput):
    total = 0
    reverseOrder = {}
    with open(fileInput, 'r') as file:
        #Process until the end of the first part
        for line in file:
            if len(line) < 2:
                break
            elems = [int(x) for x in line.strip('\n').split('|')]
            if elems[0] not in reverseOrder:
                reverseOrder[elems[0]] = []
            reverseOrder[elems[0]].append(elems[1])
            
        #Processing the rest of the document
        for line in file:
            refusals = []
            check = True
            elems = [int(x) for x in line.strip('\n').split(',')]
            for i in range(len(elems)-1,-1,-1):
                if elems[i] not in refusals and elems[i] in reverseOrder:
                    refusals += reverseOrder[elems[i]]
                elif elems[i] in refusals:
                    check = False
                    break
            if check:
                total+= elems[math.ceil(len(elems)/2)-1]
    print(total)
                
                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
