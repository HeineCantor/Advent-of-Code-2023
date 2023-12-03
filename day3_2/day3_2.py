def buildValidNumbersList(filePath):
    validList = []

    file = open(filePath)

    previousLine = None
    nextLine = None

    line = file.readline().strip() + '.'
    lineCounter = 0

    while line:
        lineCounter += 1
        nextLine = file.readline().strip()
        if(nextLine != ''):
            nextLine += '.'

        startPtr = endPtr = 0

        for i in range(len(line)):
            endPtr = i

            if(not line[endPtr].isdigit()):
                if line[startPtr:endPtr].isnumeric():
                    plausibleValid = int(line[startPtr:endPtr])
                    anyOfNextLine = nextLine != "" and any([x for x in nextLine[max(startPtr-1, 0): min(endPtr+1, len(nextLine)-1)] if x != '.' and not x.isdigit()])
                    anyOfPreviousLine = previousLine is not None and any([x for x in previousLine[max(startPtr-1, 0): min(endPtr+1, len(nextLine)-1)] if x != '.' and not x.isdigit()])
                    indexOfStars = []
                    if(
                        line[startPtr-1] != '.' or (endPtr < len(line) and line[endPtr] != '.') or
                        anyOfNextLine or anyOfPreviousLine
                    ):
                        if(line[startPtr-1] == '*'):
                            indexOfStars.append((lineCounter, startPtr-1))
                        if(endPtr < len(line) and line[endPtr] == '*'):
                            indexOfStars.append((lineCounter, endPtr))
                        if anyOfNextLine and nextLine != '':
                            for i in range(max(startPtr-1, 0), min(endPtr+1, len(nextLine))):
                                if nextLine[i] == '*':
                                    indexOfStars.append((lineCounter+1, i))
                        if anyOfPreviousLine and previousLine is not None:
                            for j in range(max(startPtr-1, 0), min(endPtr+1, len(previousLine))):
                                if previousLine[j] == '*':
                                    indexOfStars.append((lineCounter-1, j))

                        validList.append((plausibleValid, indexOfStars))
                startPtr = endPtr+1

        previousLine = line
        line = nextLine

    return validList


if __name__ == "__main__":
    validList = buildValidNumbersList("/home/heinecantor/Desktop/git/Advent-of-Code-2023/day3_2/input.txt")

    dictOfGears = {}

    for element in validList:
        allGears = element[1]
        for gear in [x for x in allGears if x not in dictOfGears]:
            for peer in validList:
                if peer == element:
                    continue

                gearsOfPeer = peer[1]

                if(gear in gearsOfPeer):
                    dictOfGears[gear] = (element[0], peer[0])

    sumOfProducts = 0

    for gear in dictOfGears:
        parts = dictOfGears[gear]

        product = parts[0] * parts[1]
        sumOfProducts += product

    print(sumOfProducts)