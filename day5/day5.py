def mapSeed(seedValue, mapStart, seedStart, limit):
    if(seedValue > seedStart+limit-1 or seedValue < seedStart):
        return seedValue
    
    return mapStart + (seedValue - seedStart)

def elaborateSeedList(filePath):
    file = open(filePath)

    seedsChains = []
    processingSteps = []

    seedsLine = file.readline().strip().split(':')[1]

    for seedSplit in seedsLine.split(' '):
        if(not seedSplit.isnumeric()):
            continue
        seed = int(seedSplit)
        seedsChains.append([seed])

    newFile = [x.strip() for x in file if not x.isspace()]

    processingIndex = -1

    for line in newFile:
        if "map" in line:
            processingIndex+=1
            processingSteps.append([])
        else:
            ruleTuple = tuple(int(x) for x in line.split(' '))
            processingSteps[processingIndex].append(ruleTuple)

    lastProcessedStep = [x[0] for x in seedsChains]

    for i in range(len(processingSteps)):
        step = processingSteps[i]
        lastProcessedStep = [x[-1] for x in seedsChains]
        for j in range(len(lastProcessedStep)):
            processedStep = lastProcessedStep[j]
            initialValue = processedStep
            for rule in step:
                converted = mapSeed(processedStep, rule[0], rule[1], rule[2])
                if(converted != initialValue):
                    initialValue = converted
                    break
            seedsChains[j].append(initialValue)

    return seedsChains

if __name__ == "__main__":
    seedsChains = elaborateSeedList("input.txt")

    listOfLocations = [x[-1] for x in seedsChains]

    print(min(listOfLocations))