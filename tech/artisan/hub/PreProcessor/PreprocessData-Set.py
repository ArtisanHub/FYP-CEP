import datetime

pathToCompleteDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/full-game.txt'
pathToPreProcessedDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/proccesed-full-game.txt'

completeDAtaSet = open(pathToCompleteDataSet,"r")
preProcessedDataSet = open(pathToPreProcessedDataSet,"w")

tempRowArr = None
averageValueDict = dict()
tempAverageValueRow = None

count =0;
startTime = datetime.datetime.now()

for line in completeDAtaSet:
    count += 1
    tempRowArr = line.split(",")
    key = tempRowArr[0]
    if key in averageValueDict:
        # if sensor id is processed already required data will be retreived from the dict
        tempAverageValueRow = averageValueDict[key]
        sidCount = int(tempAverageValueRow[0])
        sidCount += 1
        tempAverageValueRow[0] = sidCount
        for index in range(len(tempRowArr)):
            # Skipping the 1st two columns assuming sensor id and time stamp are always available
            if index == 0 or index == 1:
                continue
            if tempRowArr[index]:
                # Calculating and saving the average
                tempAverageValueRow[index] = (int(tempAverageValueRow[index]) + int(tempRowArr[index])) / sidCount
            else:
                tempRowArr[index] = tempAverageValueRow[index]
        preProcessedDataSet.write(",".join(tempRowArr))
    else:
        # if sensor id is a new one
        preProcessedDataSet.write(",".join(tempRowArr))
        tempRowArr[0] = 0
        averageValueDict[key] = tempRowArr;

endTime = datetime.datetime.now()
print("Pre processing has been completed.")
print("Preprocessed row count: "+str(count))
print("Time taken for preprocessing:" + str(endTime - startTime))