import sys
import numpy as np
import re 
directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
directions2 = [((-1,-1),(1,-1))]

def check_cases(matrix,x,y,xx,yy):
    return matrix[x + xx][y+yy] == 'M' and matrix[x + (xx*2)][y+(yy*2)] == 'A' and matrix[x + (xx*3)][y+(yy*3)] == 'S'

def check_cases2(matrix,x,y,xx,yy):
    return( matrix[x + xx][y+yy] == 'M' and matrix[x +(xx*-1)][y+(yy*-1)] == 'S') or (matrix[x + xx][y+yy] == 'S' and  matrix[x +(xx*-1)][y+(yy*-1)] == 'M')


def main1(fileInput):
    matrix = []
    i = 0
    correct  = 0
    with open(fileInput,'r') as file:
        for line in file:
            row = [*line.split()[0]]
            matrix.append(row)
            i += 1
    for x in range(0,140):
        for y in range(0,140):
            if matrix[x][y] == 'X':
                corrects = map(lambda a : check_cases(matrix,x,y,a[0],a[1]),[x for x in filter(lambda b : (140 >(b[0]*3 + x) > -1) and (140 > (b[1]*3 + y) > -1),directions)])
                for elem in corrects:
                    if elem:
                        correct+=1
                    
    print(correct)


def main2(fileInput):
    matrix = []
    i = 0
    correct  = 0
    with open(fileInput,'r') as file:
        for line in file:
            row = [*line.split()[0]]
            matrix.append(row)
            i += 1
    for x in range(1,139):
        for y in range(1,139):
            if matrix[x][y] == 'A':
                corrects = map(lambda a : (check_cases2(matrix,x,y,a[0][0],a[0][1]) and check_cases2(matrix,x,y,a[1][0],a[1][1])),directions2)
                for elem in corrects:
                    if elem:
                        correct+=1
                    
    print(correct)


if __name__ == "__main__":
    if len(sys.argv) ==2 :
        main2(sys.argv[1])
