if __name__ == "__main__":
    inputFile = open("input.txt")

    line = inputFile.readline().strip()

    sum = 0

    while line:
        numList = [x for x in line if '0' <= x <= '9']
        
        first = int(numList[0])
        last = int(numList[-1])

        value = first*10 + last
        sum += value

        line = inputFile.readline().strip()

    print(sum)