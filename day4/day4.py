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

    sumOfPoints = 0

    for card in matchingNumbers:
        if(len(card) > 0):
            sumOfPoints += 2**(len(card)-1)

    print(sumOfPoints)