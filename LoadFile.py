import csv

pathToCompleteDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/full-game.txt'
pathToBallSeperatedDataSet = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/BallSeperated'

##Firstly, Run below code
########################################################################################

completeDataSet = open(pathToCompleteDataSet,'r')
fout4 = open(pathToBallSeperatedDataSet+'/ball-4.csv', 'w')
fout8 = open(pathToBallSeperatedDataSet+'/ball-8.csv', 'w')
fout10 = open(pathToBallSeperatedDataSet+'/ball-10.csv', 'w')
fout12 = open(pathToBallSeperatedDataSet+'/ball-12.csv', 'w')

line = None

def fout4Write():
    fout4.write(line)

def fout8Write():
    fout8.write(line)

def fout10Write():
    fout10.write(line)

def fout12Write():
    fout12.write(line)

# map the inputs to the function blocks
foutOptions = {4: fout4Write,
               8: fout8Write,
               10: fout10Write,
               12: fout12Write,
               }

for line in completeDataSet:
        try:
            foutOptions[int(line.split(",")[0])]()
        except:
            continue

print("Training dataset has been successfully divided into 4 balls")



#################################################################################################
# Comment out above code and run following as the second step
#####################################################################################################



# import csv
#
# with open("E:/FYP/BallSeperated/ball-4.csv", "r") as source:
#     rdr = csv.reader(source)
#     with open("E:/FYP/BallSeperated/filer/ball-4.csv", "w", newline='') as result:
#         wtr = csv.writer(result)
#         for r in rdr:
#             wtr.writerow((r[1], r[2], r[3], r[4]))
#
# with open("E:/FYP/BallSeperated/ball-8.csv", "r") as source:
#     rdr = csv.reader(source)
#     with open("E:/FYP/BallSeperated/filer/ball-8.csv", "w", newline='') as result:
#         wtr = csv.writer(result)
#         for r in rdr:
#             wtr.writerow((r[1], r[2], r[3], r[4]))
#
# with open("E:/FYP/BallSeperated/ball-10.csv", "r") as source:
#     rdr = csv.reader(source)
#     with open("E:/FYP/BallSeperated/filer/ball-10.csv", "w", newline='') as result:
#         wtr = csv.writer(result)
#         for r in rdr:
#             wtr.writerow((r[1], r[2], r[3], r[4]))
#
# with open("E:/FYP/BallSeperated/ball-12.csv", "r") as source:
#     rdr = csv.reader(source)
#     with open("E:/FYP/BallSeperated/filer/ball-12.csv", "w", newline='') as result:
#         wtr = csv.writer(result)
#         for r in rdr:
#             wtr.writerow((r[1], r[2], r[3], r[4]))
#
#
#
# print("Done")
