def buildValidNumbersList(filePath):
    validList = []

    file = open(filePath)

    previousLine = None
    nextLine = None

    line = file.readline().strip() + '.'

    while line:
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
                    if(
                        line[startPtr-1] != '.' or (endPtr < len(line) and line[endPtr] != '.') or
                        anyOfNextLine or anyOfPreviousLine
                    ):
                        validList.append(plausibleValid)
                startPtr = endPtr+1

        previousLine = line
        line = nextLine

    return validList


if __name__ == "__main__":
    validList = buildValidNumbersList("/home/heinecantor/Desktop/git/Advent-of-Code-2023/day3/input.txt")

    print(sum(validList))