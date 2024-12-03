import sys
import re
def mainNonRegexVersion(fileInput):
    count = 0
    formulaCase = 0
    formStruct= ['m','u','l','(',',',')']
    num1,num2 = '',''
    with open(fileInput,'r') as file:
        contents = file.read()
        for ch in contents:
            if formulaCase == 4 and ch.isdigit():
                num1+=ch
            elif formulaCase == 5 and ch.isdigit():
                num2+=ch
            elif ch == formStruct[formulaCase] :
                formulaCase+=1
            else:
                formulaCase = 0
            if formulaCase == 3:
                num1 = num2 = ''
            elif formulaCase == 6  :
                if num1.isnumeric() and num2.isnumeric():
                    count+= int(num1) * int(num2)
                formulaCase = 0
                    
    print(count)

def mainRegexVersion(fileInput):
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'

    with open(fileInput,'r') as file:
        contents = file.read()
        validData = list(re.finditer(pattern, contents))
        counter = sum(map(lambda a : int(a[0]) * int(a[1]), [m.groups() for m in validData]))

    print(counter)

def mainNonRegexVersion2(fileInput):
    count = 0
    formulaCase = 0
    enablerCase = 0
    disablerCase = 0
    enabled = True
    doStruct = ['d','o','(',')']
    dontStruct = ['d','o','n','\'','t','(',')']
    formStruct= ['m','u','l','(',',',')']
    num1,num2 = '',''
    with open(fileInput,'r') as file:
        contents = file.read()
        for ch in contents:
            if enabled:
                if formulaCase == 4 and ch.isdigit():
                    num1+=ch
                elif formulaCase == 5 and ch.isdigit():
                    num2+=ch
                elif ch == formStruct[formulaCase] :
                    formulaCase+=1
                else:
                    formulaCase = 0
                if formulaCase == 3:
                    num1 = num2 = ''
                elif formulaCase == 6  :
                    if num1.isnumeric() and num2.isnumeric():
                        count+= int(num1) * int(num2)
                    formulaCase = 0
            if (ch == doStruct[enablerCase] or ch == dontStruct[disablerCase]):
                if ch == doStruct[enablerCase]:
                    enablerCase+=1
                else:
                    enablerCase = 0
                if ch == dontStruct[disablerCase]:
                    disablerCase+=1
                else:
                    disablerCase = 0
            if enablerCase == 4:
                enabled = True
                enablerCase = disablerCase = 0
                formulaCase = 0
            elif disablerCase == 7:
                enabled = False
                enablerCase = disablerCase = 0
                formulaCase = 0
                    
    print(count)


def mainRegexVersion2(fileInput):
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    pattern_do = r'do\(\)'
    pattern_dont = r'don\'t\(\)'
    enabledRanges = []
    with open(fileInput,'r') as file:
        contents = file.read()
        validData = list(re.finditer(pattern, contents))
        starts = [m.end() for m in re.finditer(pattern_do, contents)]
        ends= [m.end() for m in re.finditer(pattern_dont,contents)]
        i = 0
        dontI = 0
        doI = 0
        pos = 0
        while i < len(contents) and dontI < len(ends) and doI < len(starts):
            itDo = enumerate(starts)
            itDont = enumerate(ends)
            dontI = next((x[0] for x in itDont if x[1] > pos),len(ends))
            if dontI == len(ends):
                break
            currentDont = ends[dontI]
            enabledRanges.append(range(pos,currentDont))
            doI = next((x[0] for x in itDo if x[1] > currentDont),len(starts))
            if doI == len(starts):
                break
            pos = starts[doI]
        if doI < len(starts) and dontI == len(ends):
            enabledRanges.append(range(pos,len(contents)))            
        count = sum(map(lambda a : int(a[0]) * int(a[1]), [m.groups() for m in validData if any(m.end() in r for r in enabledRanges)]))
        print(count)


if __name__ == "__main__":
    if len(sys.argv) ==2 :
        mainRegexVersion2(sys.argv[1])
