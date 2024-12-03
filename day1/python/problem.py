import sys
from collections import Counter
def main1(fileInput):
    with open(fileInput,'r') as file:
        list1, list2 = zip(*[[int(num) for num in cols.split()] for cols in file])
        list1 = sorted(list1)
        list2 = sorted(list2)
        somme = sum(abs(a-b) for a,b in zip(list1,list2))
        print(somme)


def main2(fileInput):
    with open(fileInput,'r') as file:
        list1, list2 = zip(*[[int(num) for num in cols.split()] for cols in file])
        dict2 = Counter(list2)
        somme = sum(number*dict2.get(number,0) for number in list1)
        print(somme)

if __name__ == "__main__":
    if len(sys.argv) ==2 :
        main2(sys.argv[1])
