
#val1 = 10753295594424116
#val2 = 14879639146403495
#val3 = ((val2 - val1)/8)

count1 = 0
count2 = 0

#obtaining the analysis time frame - forth octet of the match = 7.5 minutes

strt1 = 11473*10**12    #Goal in the 13.22 minute
end1 = 11593*10**12

strt2 = 11113*10**12   #Goal in the 7.08 minute
end2 = 11233*10**12

#strt = 12373*10**12   #Goal in the 28.17 minute
#end = 12493*10**12

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/full-game/full-game.csv', 'rU' ) #open train data

r1 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'w')
r2 = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'w')

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
    else:
        continue

r1.close()
r2.close()
f.close()




