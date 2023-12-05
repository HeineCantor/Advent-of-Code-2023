from tqdm import tqdm

def mapSeed(seedValue, mapStart, seedStart, limit):
    if(seedValue < seedStart or seedValue > seedStart+limit-1):
        return seedValue
    
    return mapStart + (seedValue - seedStart)

def elaborateSeedList(filePath):
    file = open(filePath)

    seedsChains = []
    processingSteps = []

    seedsLine = file.readline().strip().split(':')[1].split(' ')
    seedsLine = [x for x in seedsLine if not x == '']

    newFile = [x.strip() for x in file if not x.isspace()]

    processingIndex = -1

    for line in newFile:
        if "map" in line:
            processingIndex+=1
            processingSteps.append([])
        else:
            ruleTuple = tuple(int(x) for x in line.split(' '))
            processingSteps[processingIndex].append(ruleTuple)

    totalMinimum = 1e100

    for i in range(0, len(seedsLine), 2):
        start = int(seedsLine[i])
        length = int(seedsLine[i+1])

        for j in tqdm(range(start, start+length)):
            initialValue = j
            for step in processingSteps:
                for rule in step:
                    converted = mapSeed(initialValue, rule[0], rule[1], rule[2])
                    if(converted != initialValue):
                        initialValue = converted
                        break
            if initialValue < totalMinimum:
                totalMinimum = initialValue
                

    return totalMinimum

if __name__ == "__main__":
    minimum = elaborateSeedList("/home/heinecantor/Desktop/git/Advent-of-Code-2023/day5/input.txt")

    print(minimum)