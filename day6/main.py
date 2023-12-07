def buildGoalDict(filePath):
    file = open(filePath)

    timeLine = file.readline().strip().split(':')[1]
    distanceLine = file.readline().strip().split(':')[1]

    times = [int(x) for x in timeLine.split(' ') if not x=='']
    distances = [int(x) for x in distanceLine.split(' ') if not x=='']

    goalDict = {key:value for key, value in zip(times, distances)}

    return goalDict

def getListOfWinningTimes(goalDict):
    winningTimes = {}

    for time in goalDict:
        winningTimes[time] = []
        for i in range(time+1):
            speed = i
            if((time-i)*speed > goalDict[time]):
                winningTimes[time].append(i)

    return winningTimes

if __name__ == "__main__":
    goalDict = buildGoalDict("input.txt")

    print(goalDict)

    winningTimes = getListOfWinningTimes(goalDict)
    print(winningTimes)

    productOfWaysToWin = 1

    for winningList in winningTimes.values():
        productOfWaysToWin *= len(winningList)

    print(productOfWaysToWin)