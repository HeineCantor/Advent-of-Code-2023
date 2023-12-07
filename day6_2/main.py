from tqdm import tqdm

def getTimeAndTarget(filePath):
    file = open(filePath)

    timeLine = file.readline().strip().split(':')[1]
    distanceLine = file.readline().strip().split(':')[1]

    times = [x for x in timeLine.split(' ') if not x=='']
    distances = [x for x in distanceLine.split(' ') if not x=='']

    time = int(''.join(times))
    distance = int(''.join(distances))

    return time, distance

def getNumOfWins(time, targetDistance):
    numOfWins = 0

    for i in tqdm(range(time+1)):
        distance = (time-i)*i
        if(distance > targetDistance):
            numOfWins+=1

    return numOfWins

if __name__ == "__main__":
    time, distance = getTimeAndTarget("input.txt")

    print(time)
    print(distance)

    numOfWins = getNumOfWins(time, distance)

    print(numOfWins)