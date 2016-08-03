
#val1 = 10753295594424116
#val2 = 14879639146403495
#val3 = ((val2 - val1)/8)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

#obtaining the analysis time frame - forth octet of the match = 7.5 minutes

strt1 = 11173*10**12   #Goal in the 7.08 minute
end1 = 11233*10**12

strt2 = 11533*10**12    #Goal in the 13.22 minute
end2 = 11593*10**12

strt3 = 12073*10**12   #Goal in the 22.12 minute
end3 = 12133*10**12

strt4 = 12433*10**12   #Goal in the 28.16 minute
end4 = 12493*10**12

strt5 = 11053*10**12   #Non goal period - 5th minute
end5 = 11113*10**12

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/full-game/full-game.csv', 'rU' ) #open train data

r1 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'w')
r2 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'w')
r3 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'w')
r4 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'w')
r5 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'w')

#preping the analysis file with the respective window data
for line in f:
    cells = line.split(",")

    if int(cells[1]) >= strt1 and int(cells[1]) <= end1:
        r1.write(str(count1))
        r1.write(str(","))
        r1.write(line)
        count1 = count1 + 1

    elif int(cells[1]) >= strt2 and int(cells[1]) <= end2:
        r2.write(str(count2))
        r2.write(str(","))
        r2.write(line)
        count2 = count2 + 1

    elif int(cells[1]) >= strt3 and int(cells[1]) <= end3:
        r3.write(str(count3))
        r3.write(str(","))
        r3.write(line)
        count3 = count3 + 1

    elif int(cells[1]) >= strt4 and int(cells[1]) <= end4:
        r4.write(str(count4))
        r4.write(str(","))
        r4.write(line)
        count4 = count4 + 1

    elif int(cells[1]) >= strt5 and int(cells[1]) <= end5:
        r5.write(str(count5))
        r5.write(str(","))
        r5.write(line)
        count5 = count5 + 1

    else:
        continue

r1.close()
r2.close()
r3.close()
r4.close()
r5.close()
f.close()




