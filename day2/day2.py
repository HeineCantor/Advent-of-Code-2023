def generateGamesDict(filePath):
    file = open(filePath)

    gamesDict = {}
    tmpList = [0, 0, 0]

    line = file.readline().strip()

    while line:
        gameID = int(line.split(' ')[1][:-1])
        gamesDict[gameID] = []
        line = line[line.index(':')+2:]

        splitLine = line.split(' ')

        value = 0

        for element in splitLine:
            if element.isnumeric():
                value = int(element)
            else:
                if element[0] == 'r':
                    tmpList[0] += value
                elif element[0] == 'g':
                    tmpList[1] += value
                else:
                    tmpList[2] += value
                value = 0
                if element[-1] == ';' or (element[-1] != ',' and element[-1] != ';'):
                    gamesDict[gameID].append(tmpList)
                    tmpList = [0, 0, 0]

        

        line = file.readline().strip()

    return gamesDict

CONSTRAINTS = (12, 13, 14)

if __name__ == "__main__":
    gamesDict = generateGamesDict("input.txt")

    sumOfPossibleIds = 0

    for game in gamesDict:
        rounds = gamesDict[game]
        
        reds = max([x[0] for x in rounds])
        greens = max([x[1] for x in rounds])
        blues = max([x[2] for x in rounds])

        if(reds <= CONSTRAINTS[0] and greens <= CONSTRAINTS[1] and blues <= CONSTRAINTS[2]):
            sumOfPossibleIds += game

    print(sumOfPossibleIds)