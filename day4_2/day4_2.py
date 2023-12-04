def getWinningNumbers(filePath):
    file = open(filePath)

    allMatchingNumbers = []

    line = file.readline().strip()

    while line:
        allNumbers = line.split(':')[1]

        winningNumbers = allNumbers.split('|')[0]
        userNumbers = allNumbers.split('|')[1]

        winningNumbers = [int(x) for x in winningNumbers.split(' ') if x.isnumeric()]
        userNumbers = [int(x) for x in userNumbers.split(' ') if x.isnumeric()]

        matchingNumbers = [x for x in winningNumbers if x in userNumbers]

        allMatchingNumbers.append(matchingNumbers)

        line = file.readline().strip()

    return allMatchingNumbers

if __name__ == "__main__":
    matchingNumbers = getWinningNumbers("input.txt")

    cardsDict = {key:1 for key in range(1, len(matchingNumbers)+1)}

    for i in range(len(matchingNumbers)):
        card = matchingNumbers[i]
        if(len(card) > 0):
            numberOfCards = len(card)
            for j in range(numberOfCards):
                cardsDict[i+2+j] += cardsDict[i+1]
        
    print(sum(cardsDict.values()))