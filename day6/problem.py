import sys


def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, sx, sy, ex, ey,orientation):
        self.start = Point(sx,sy)
        self.end = Point(ex,ey)
        self.orientation = orientation
        match self.orientation:
            case 0:
                self.situation = [-1,0]
            case 1:
                self.situation = [0,1]
            case 2:
                self.situation = [1,0]
            case 3:
                self.situation = [0,-1]
    def intersect(self, line):
        if self.orientation != line.orientation:
            return False
        return (self.start.x == line.start.x == self.end.x and (self.start.y <= line.start.y <= self.end.y or self.start.y <= self.end.y <= self.end.y) ) \
            or (self.start.y == line.start.y == self.end.y and (self.start.x <= line.start.x <= self.end.x or self.start.x <= self.end.x <= self.end.x))
    def __str__(self):
        return f"Line(sx={self.start.x}, sy={self.start.y}, ex={self.end.x}, ey={self.end.y}, orientation={self.orientation})"

def main(fileInput):
    matrix = [['.' for _ in range(130)] for _ in range(130)]
    
    visited = [[False for _ in range(130)] for _ in range(130)]
    lines = []

    loc = [0,0]
    case = 0
    situation = [-1,0]
    with open(fileInput, 'r') as file:
        i = 0
        for line in file:
            line = line.strip('\n')
            elems = [x for x in line]
            if '^' in elems:
                loc = [i,elems.index('^')]
            matrix[i] = elems
            i += 1
    print(loc)
    start = loc
    while (130 > loc[0] + situation[0] > -1 and 130 > loc[1] + situation[1] > -1):
        visited[loc[0]][loc[1]] = True
        next = matrix[loc[0]+situation[0]][loc[1]+situation[1]]
        if next == '#':
            lines.append(Line(start[0],start[1],loc[0],loc[1],case))
            start = loc
            case += 1
            case %= 4
            match case:
                case 0:
                    situation = [-1,0]
                case 1:
                    situation = [0,1]
                case 2:
                    situation = [1,0]
                case 3:
                    situation = [0,-1]
        else:
            loc = [loc[0]+situation[0],loc[1]+situation[1]]
    print(start)
    lines.append(Line(start[0],start[1],loc[0],loc[1],case))
    result = 'PART 1 : ' + str(sum(map(sum,visited))+1)
    #Part 2
    foundOne = 0
    for x in range(len(lines)):
        currentLine = lines[x]
        newOrientation = (currentLine.orientation + 1) % 4
        situation = [0,0]
        pointsx = [x for x in range(currentLine.start.x,currentLine.end.x,currentLine.situation[0])] if currentLine.situation[0] != 0 else [currentLine.start.x]
        pointsy = [y for y in range(currentLine.start.y,currentLine.end.y,currentLine.situation[1])] if currentLine.situation[1] != 0 else [currentLine.start.y]
        points = [(x,y) for x in pointsx for y in pointsy]
        match newOrientation:
            case 0:
                situation = [-1,0]
            case 1:
                situation = [0,1]
            case 2:
                situation = [1,0]
            case 3:
                situation = [0,-1]
        for point in points:
            #We create the new line
            loc = point
            while (130 > loc[0] + situation[0] > -1 and 130 > loc[1] + situation[1] > -1 and matrix[loc[0]+situation[0]][loc[1]+situation[1]] != '#'):
                loc = [loc[0]+situation[0],loc[1]+situation[1]]
            if loc[0] < 0 or loc[0] > 130 or loc[1] < 0 or loc[1] > 130:
                continue
            newLine = Line(point[0],point[1],loc[0],loc[1],newOrientation)
            print(newLine)
            for y in range(len(lines)):
                if x != y and (newLine.intersect(lines[y]) or lines[y].intersect(newLine)):
                    foundOne +=1
        
    result += '\nPART 2 : ' + str(foundOne)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
