
def totalDatasetAnalysis():
    row_count = 0;
    zero_count = 0;
    one_count = 0;
    shapelet_zero_event_count = 0;
    x0 = 0;
    x1 = 0;
    shapelet_one_event_count = 0;
    y0= 0;
    y1 = 0;
    for line in input:
        #print(line)
        if row_count != 0:
            cells = line.split(",")
            #print(row_count)

            if (int)(cells[7]) == 0:
                zero_count = zero_count + 1

            if (int)(cells[7]) == 1:
                one_count = one_count + 1

            if ((20 <= (float)(cells[3]) <= 40) and ((float)(cells[4]) <= 10) and (420 <= (float)(cells[5]) <= 450)):
                shapelet_zero_event_count = shapelet_zero_event_count + 1
                if (int)(cells[7]) == 1:
                    x1 = x1 + 1
                else:
                    x0 = x0 + 1

            if ((400 <= (float)(cells[5]) <= 1050) and ((float)(cells[6]) <= 10)):
                shapelet_one_event_count = shapelet_one_event_count + 1
                if (int)(cells[7]) == 1:
                    y1 = y1 + 1
                else:
                    y0 = y0 + 1

        row_count = row_count + 1


    return row_count, zero_count, one_count, shapelet_zero_event_count, x0, x1, shapelet_one_event_count, y0, y1


input = open('D:/FYP-Developments/occupancy_data/datatraining.txt', 'rU') #open train data

row_count, zero_count, one_count, shapelet_zero_event_count, x0, x1, shapelet_one_event_count, y0, y1 = totalDatasetAnalysis()

input.close()

print("Total Row count: %d" %row_count)
print("Total non occupied events (Occupancy = 0): %d" %zero_count)
print("Total occupied events (Occupancy = 1): %d" %one_count)

print("###################################")

print("Total non occupied events (Occupancy = 0) detected using CEP query generated: %d" %shapelet_zero_event_count)
print("xxxxxxxxxxxxxxx 0: %d" %x0)
print("xxxxxxxxxxxxxxx 1: %d" %x1)
print("#####################################")
print("Total occupied events (Occupancy = 1) detected using CEP query generated: %d" %shapelet_one_event_count)
print("yyyyyyyyyyyyyyy 0: %d" %y0)
print("yyyyyyyyyyyyyyy 1: %d" %y1)
