import sys

def main1(fileInput):
    j,count = 0,0
    with open(fileInput,'r') as file:
        for line in file:
            numbers = [int(s) for s in line.split()]
            direction = numbers[0] - numbers[1]
            check = True
            for i,j in zip(numbers,numbers[1:]):
                absDiff = abs(i-j)
                if (((i-j) * direction) < 0) or (absDiff > 3 or absDiff < 1):
                    check = False
                    break
            if check:
                count+=1
    print(count)

def main2(fileInput):
    j,count = 0,0
    with open(fileInput,'r') as file:
        for line in file:
            numbers = [int(s) for s in line.split()]
            breakLevel = 0
            while breakLevel < len(numbers):
                i,j = 0,1
                if i == breakLevel:
                    i+=1
                    j+=1
                if j == breakLevel:
                    j+=1
                direction = numbers[i] - numbers[j]
                while (j < len(numbers)):
                    absDiff = abs(numbers[i]-numbers[j])
                    if (((numbers[i]-numbers[j]) * direction) < 0) or (absDiff > 3 or absDiff < 1):
                        break
                    i+=1 
                    j+=1
                    if i == breakLevel:
                        i+=1
                    if j == breakLevel:
                        j+=1
                if j >= len(numbers):
                    count+=1
                    break
                breakLevel+=1

    print(count)

if __name__ == "__main__":
    if len(sys.argv) ==2 :
        main2(sys.argv[1])
