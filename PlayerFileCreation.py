import csv
import os
import math

pathToCompleteDataSet = "D:/FYP/DEBS2013/full-game/full-game.csv"
pathToBallSeperatedDataSet = 'D:/FYP/DEBS2013/PlayerStats'

if not os.path.isdir(pathToBallSeperatedDataSet):
   os.makedirs(pathToBallSeperatedDataSet)


completeDataSet = open(pathToCompleteDataSet,'r')
foutDennisTA = open(pathToBallSeperatedDataSet+'/DennisTA', 'w')


row =None
csvWriter = None

def foutPlayer1TA():
    csvWriter = csv.writer(foutDennisTA)
    csvWriter.writerow((int(math.fabs(int(row[0]))), row[1], int(math.fabs(int(row[5]))), int(math.fabs(int(row[7]))),
                        int(math.fabs(int(row[8]))), int(math.fabs(int(row[9])))))


foutOptions = {47: foutPlayer1TA,
               16: foutPlayer1TA,
               }

for line in completeDataSet:
        try:
            row = line.split(",")
            foutOptions[int(row[0])]()
        except:
            continue

print("Dennis Dotterweich Analysis")