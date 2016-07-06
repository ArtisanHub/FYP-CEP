##Firstly, Run below code
########################################################################################

import csv
with open('E:/FYP/full-game.csv', 'r') as fin, \
        open('E:/FYP/BallSeperated/ball-4.csv', 'w', newline='') as fout4:
    writer = csv.writer(fout4)
    for row in csv.reader(fin):
        if row[0] == '4':
            writer.writerow(row)

with open('E:/FYP/full-game.csv', 'r') as fin, \
        open('E:/FYP/BallSeperated/ball-8.csv', 'w', newline='') as fout8:
    writer = csv.writer(fout8)
    for row in csv.reader(fin):
        if row[0] == '8':
            writer.writerow(row)

with open('E:/FYP/full-game.csv', 'r') as fin, \
        open('E:/FYP/BallSeperated/ball-10.csv', 'w', newline='') as fout10:
    writer = csv.writer(fout10)
    for row in csv.reader(fin):
        if row[0] == '10':
            writer.writerow(row)

with open('E:/FYP/full-game.csv', 'r') as fin, \
        open('E:/FYP/BallSeperated/ball-12.csv', 'w', newline='') as fout12:
    writer = csv.writer(fout12)
    for row in csv.reader(fin):
        if row[0] == '12':
            writer.writerow(row)

print("Training dataset has been successfully divided into 4 balls")



#################################################################################################
#Comment out above code and run following as the second step
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