
pathToCompleteDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/full-game.txt'
pathToPreProcessedDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/proccesed-full-game.txt'

completeDAtaSet = open(pathToCompleteDataSet,"r")
preProcessedDataSet = open(pathToPreProcessedDataSet,"w")

tempRowArr = None
averageValueDict = dict()
tempAverageValueRow = None
# averageValueDict['98'] = [1,2];
# print(averageValueDict['98'][0])

count =0;
for line in completeDAtaSet:
    count = count +1
    tempRowArr = line.split(",")
    key = tempRowArr[0]
    if key in averageValueDict:
        tempAverageValueRow = averageValueDict[key]
        sidCount = int(tempAverageValueRow[0])
        sidCount = sidCount + 1
        for index in range(len(tempRowArr)):
            if index == 0:
                continue
            if tempRowArr[index]:
                tempAverageValueRow[index] = (int(tempAverageValueRow[index]) + int(tempRowArr[index])) / sidCount
            else:
                tempRowArr[index] = tempAverageValueRow[index]
        preProcessedDataSet.write(",".join(tempRowArr))
    else:
        preProcessedDataSet.write(",".join(tempRowArr))
        tempRowArr[0] = 0
        averageValueDict[key] = tempRowArr;
    if count>100:
        break