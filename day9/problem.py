import sys
import numpy as np

class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret




def main1(fileInput):
    originalLine = ""
    formattedLine = []
    uniqueId = 0
    with open(fileInput, 'r') as file:
        originalLine = file.readline()
    for i in range(0,len(originalLine)):
        match i % 2:
            case 0:
                formattedLine.extend([str(uniqueId)] * int(originalLine[i]))
                uniqueId += 1
            case 1:
                formattedLine.extend('.' * int(originalLine[i]))
    #We fill the empty spaces
    print(formattedLine)
    emptyCursor = formattedLine.index('.')
    loc = len(formattedLine)-1
    while loc > 0 and emptyCursor < loc:
        try :
            if formattedLine[loc] != '.':
                formattedLine[emptyCursor] = formattedLine[loc]
                formattedLine[loc] = '.'
                while (emptyCursor < len(formattedLine) and formattedLine[emptyCursor] != '.'):
                    emptyCursor += 1
            loc -= 1
        except ValueError:
            print("HUH")
            break
    print(formattedLine)
    part1Value = sum([int(x) * y if x != '.' else 0 for x,y in zip(formattedLine,range(0,len(formattedLine)))])

    print(part1Value)


def main2(fileInput):
    numbers = []
    emptyBlocks = []
    originalLine = ""
    formattedLine = []
    ptrLoc = 0
    with open(fileInput, 'r') as file:
        originalLine = file.readline()
    for i in range(0,len(originalLine)):
        match i % 2:
            case 0:
                formattedLine.extend([len(numbers)] * int(originalLine[i]))
                numbers.append([ptrLoc,int(originalLine[i]),len(numbers)])
            case 1:
                if int(originalLine[i]) > 0:
                    emptyBlocks.append([ptrLoc,int(originalLine[i])])
                    formattedLine.extend('.' * int(originalLine[i]))

        ptrLoc += int(originalLine[i])
    #print(numbers)
    for j in range(len(numbers)-1,0,-1):
        currentFile = numbers[j]
        #print("WE ARE MOVING {} TO SOMEWHERE IN {} it needs {}".format(formattedLine[currentFile[0]],emptyBlocks,currentFile[1]))
        for k in range(0,len(emptyBlocks)):
            currentEmptyBlock = emptyBlocks[k]
            if currentFile[0] < currentEmptyBlock[0]:
                continue
            if currentEmptyBlock[1] >= currentFile[1]:
                formattedLine[currentEmptyBlock[0]:currentEmptyBlock[0]+currentFile[1]] = formattedLine[currentFile[0]:currentFile[0]+currentFile[1]]
                formattedLine[currentFile[0]:currentFile[0]+currentFile[1]] = ['.'] * currentFile[1]
                emptyBlocks[k][1] -= currentFile[1] 
                emptyBlocks[k][0] += currentFile[1]
                #print(formattedLine)
                break
    #print(formattedLine)
    part2Value = sum([int(x) * y if x != '.' else 0 for x,y in zip(formattedLine,range(0,len(formattedLine)))])

    print(part2Value)
                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main1(sys.argv[1])
        main2(sys.argv[1])
