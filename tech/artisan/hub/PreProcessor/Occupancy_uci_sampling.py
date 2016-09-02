
row_count = 0;
zero_count = 0;
one_count = 0;

sep = ","


input = open('D:/FYP-Developments/occupancy_data/datatraining.txt', 'rU') #open train data
output = open('D:/FYP-Developments/occupancy_data/result.csv', 'w')


for line in input:


    if row_count != 0:
        cells = line.split(",")
        print(line)

        if (int)(cells[7]) == 0:
            zero_count = zero_count + 1
            if zero_count <= 800:
                e_data_row = str(cells[0]) + sep + str(cells[1]) + sep + str(cells[2]) + sep + str(
                    cells[3]) + sep + str(
                    cells[4]) + sep + str(cells[5]) + sep + str(cells[6]) \
                             + sep + str(cells[7])
                output.write(e_data_row)

        if (int)(cells[7]) == 1:
            one_count = one_count + 1
            if one_count <= 200:
                e_data_row = str(cells[0]) + sep + str(cells[1]) + sep + str(cells[2]) + sep + str(
                    cells[3]) + sep + str(
                    cells[4]) + sep + str(cells[5]) + sep + str(cells[6]) \
                             + sep + str(cells[7])
                output.write(e_data_row)

    row_count = row_count + 1

output.close()
input.close()

print(zero_count)
print(one_count)