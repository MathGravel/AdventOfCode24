import sys
import numpy as np

class Matrix:
    def __init__(self,dArray,part2=False):
        self.matrix = np.array([[x for x in y] for y in dArray])
        self.uniqueCases = np.array([[False for x in y] for y in dArray])
        self.locations = self.parseLocations() if not part2 else self.parseLocationsAndAntinodes()

    def parseLocations(self):
        dic = {}
        for iy, ix in np.ndindex(self.matrix.shape):
            if self.matrix[iy,ix] != '.':
                if self.matrix[iy,ix] not in dic:
                    dic[self.matrix[iy,ix]] = []
                dic[self.matrix[iy,ix]].append([iy,ix])
        return dic

    def parseLocationsAndAntinodes(self):
        dic = {}
        for iy, ix in np.ndindex(self.matrix.shape):
            if self.matrix[iy,ix] != '.':
                self.uniqueCases[iy,ix] = True
                if self.matrix[iy,ix] not in dic:
                    dic[self.matrix[iy,ix]] = []
                dic[self.matrix[iy,ix]].append([iy,ix])
        return dic



    def get(self,x,y):
        return self.matrix[x,y] if 0 <= x < self.matrix.shape[0] and 0 <= y < self.matrix.shape[1] else None
    
    def markAntinode(self,x,y,letter):
        if 0 <= x < self.matrix.shape[0] and 0 <= y < self.matrix.shape[1] and self.matrix[x,y] != letter:
            self.uniqueCases[x,y] = True

    def __str__(self):
        return str(self.matrix)

    def check2(self):
        return str(self.uniqueCases)

def main1(fileInput):
    temp = []
    with open(fileInput, 'r') as file:
        for line in file:
            l = line.strip('\n')
            elems = [x for x in l]
            temp.append(elems)
    matrix = Matrix(temp)
    for letter in matrix.locations:
        print("Pour la lettre {} on a les spots {}".format(letter,matrix.locations[letter]))
        temp = matrix.locations[letter]
        for i  in range(0,len(temp)):
            for j in range(i+1,len(temp)):
                diffX = (temp[i][0] - temp[j][0]) * 2
                diffY = (temp[i][1] - temp[j][1]) * 2
                print("Antinode entre {} et {} avec la difference de {} qui sont {}".format(temp[i],temp[j],[diffX,diffY],letter))
                print("Tu check alors les cases {}, et {}".format([temp[i][0]-diffX,temp[i][1]-diffY],[temp[j][0]+diffX,temp[j][1]+diffY]))
                matrix.markAntinode(temp[i][0]-diffX,temp[i][1]-diffY,letter)
                matrix.markAntinode(temp[j][0]+diffX,temp[j][1]+diffY,letter)
    print(matrix.check2())

    print(sum(map(sum,matrix.uniqueCases)))


def main2(fileInput):
    temp = []
    with open(fileInput, 'r') as file:
        for line in file:
            l = line.strip('\n')
            elems = [x for x in l]
            temp.append(elems)
    matrix = Matrix(temp,True)
    print(sum(map(sum,matrix.uniqueCases)))

    for letter in matrix.locations:
        print("Pour la lettre {} on a les spots {}".format(letter,matrix.locations[letter]))
        temp = matrix.locations[letter]
        for i  in range(0,len(temp)):
            for j in range(i+1,len(temp)):
                diffX = (temp[i][0] - temp[j][0]) 
                diffY = (temp[i][1] - temp[j][1]) 
                print("Antinode entre {} et {} avec la difference de {} qui sont {}".format(temp[i],temp[j],[diffX,diffY],letter))
                #print("Tu check alors les cases {}, et {}".format([temp[i][0]-diffX,temp[i][1]-diffY],[temp[j][0]+diffX,temp[j][1]+diffY]))
                case1 = temp[i]
                case2 = temp[j]
                while (matrix.get(case1[0]-diffX,case1[1]-diffY) is not None):
                    print("Spot {} est {}".format([case1[0]-diffX,case1[1]-diffY],matrix.get(case1[0]-diffX,case1[1]-diffY)))
                    matrix.markAntinode(case1[0]-diffX,case1[1]-diffY,letter)
                    case1 = [case1[0]-diffX,case1[1]-diffY]
                while (matrix.get(case2[0]+diffX,case2[1]+diffY) is not None):
                    matrix.markAntinode(case2[0]+diffX,case2[1]+diffY,letter)
                    case2 = [case2[0]+diffX,case2[1]+diffY]

    print(matrix.uniqueCases[3,2])

    print(sum(map(sum,matrix.uniqueCases)))
         
                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        #main1(sys.argv[1])
        main2(sys.argv[1])
