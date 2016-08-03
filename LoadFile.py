import csv
import os

pathToCompleteDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/full-game.txt'
pathToBallSeperatedDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/BallSeperated'

pathofSAlih = '/home/jawadhsr/Desktop/FYP/full-game'
pathtoSeparateSalih = '/home/jawadhsr/Desktop/FYP/Separated'
if not os.path.isdir(pathtoSeparateSalih):
   os.makedirs(pathtoSeparateSalih)

completeDataSet = open(pathofSAlih,'r')
fout4 = open(pathtoSeparateSalih+'/ball-4.csv', 'w')
fout8 = open(pathtoSeparateSalih+'/ball-8.csv', 'w')
fout10 = open(pathtoSeparateSalih+'/ball-10.csv', 'w')
fout12 = open(pathtoSeparateSalih+'/ball-12.csv', 'w')

row =None
csvWriter = None

def fout4Write():
    csvWriter = csv.writer(fout4)
    csvWriter.writerow((row[1],row[2],row[3],row[4]))

def fout8Write():
    csvWriter = csv.writer(fout8)
    csvWriter.writerow((row[1],row[2],row[3],row[4]))

def fout10Write():
    csvWriter = csv.writer(fout10)
    csvWriter.writerow((row[1],row[2],row[3],row[4]))

def fout12Write():
    csvWriter = csv.writer(fout12)
    csvWriter.writerow((row[1],row[2],row[3],row[4]))

foutOptions = {4: fout4Write,
               8: fout8Write,
               10: fout10Write,
               12: fout12Write,
               }

for line in completeDataSet:
        try:
            row = line.split(",")
            foutOptions[int(row[0])]()
        except:
            continue

print("Training dataset has been successfully divided into 4 balls")
