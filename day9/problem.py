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
    k = KMP()
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
    #print(formattedLine)
    emptyCursor = formattedLine.index('.')
    loc = len(formattedLine)-1
    while loc > 0 and emptyCursor < loc:
        try :
            if formattedLine[loc] != '.':
                #We get the entire file
                endingPoint = loc
                startingPoint = loc
                while(formattedLine[startingPoint] == formattedLine[loc]):
                    startingPoint -= 1
                structSize = endingPoint - startingPoint
                emptyCursor = k.search( formattedLine,'.' * structSize)
                #print(emptyCursor)
                if len(emptyCursor) > 0 and emptyCursor[0] < loc:
                    emptyCursor = emptyCursor[0]
                    formattedLine[emptyCursor:emptyCursor+structSize] = formattedLine[startingPoint+1:endingPoint+1]
                    formattedLine[startingPoint+1:endingPoint+1] = ['.']* structSize
                    #print("ACTUELLEMENT {}".format(formattedLine))
                else:
                    emptyCursor = 0
                loc -= structSize
            else:
                loc -= 1
        except ValueError:
            print("HUH")
            break
    print(formattedLine)
    part1Value = sum([int(x) * y if x != '.' else 0 for x,y in zip(formattedLine,range(0,len(formattedLine)))])

    print(part1Value)
                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        #main1(sys.argv[1])
        main2(sys.argv[1])
