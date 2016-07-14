
val1 = 10753295594424116
val2 = 14879639146403495
val3 = ((val2 - val1)/8)
count = 0

#obtaining the analysis time frame - forth octet of the match = 7.5 minutes
strt = val1 + (3*val3)
end = val1 + (4*val3)

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/full-game/full-game.csv', 'rU' ) #open train data
r = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/result.csv', 'w')

#preping the analysis file with the respective window data
for line in f:
    cells = line.split(",")
    if int(cells[1]) >= strt and int(cells[1]) <= end:
        r.write(str(count))
        r.write(str(","))
        r.write(line)
        count = count + 1
    else:
        continue

r.close()
f.close()