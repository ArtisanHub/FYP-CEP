import shlex
total_accuracy_zero = 0;
total_accuracy_one = 0;

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

    start_time_1 = 5743
    end_time_1 = 6033

    start_time_2 = 7019
    end_time_2 = 7250

    for line in input:
        #print(line)
        if row_count != 0:
            cells = line.split(",")

            row_num = shlex.split(cells[0])


            if ((int)(cells[7]) == 0 and (start_time_1 <= int(row_num[0]) <= end_time_1)):
                zero_count = zero_count + 1

            if ((int)(cells[7]) == 1 and (start_time_2 <= int(row_num[0]) <= end_time_2)):
                one_count = one_count + 1



            if ((20 <= (float)(cells[3]) <= 40) and ((float)(cells[4]) <= 10) and (420 <= (float)(cells[5]) <= 450)
                and (int)(cells[7]) == 0 and (start_time_1 <= int(row_num[0]) <= end_time_1)):
                shapelet_zero_event_count = shapelet_zero_event_count + 1
                # print(str(row_num[0]))
                # print(cells[0])
                output.write(str(row_num[0]))
                output.write("\n")

            if ((400 <= (float)(cells[5]) <= 2050) and ((float)(cells[6]) <= 10) and (int)(cells[7]) == 1 and (start_time_2 <= int(row_num[0]) <= end_time_2)):
                shapelet_one_event_count = shapelet_one_event_count + 1


        row_count = row_count + 1


    return row_count, zero_count, one_count, shapelet_zero_event_count, x0, x1, shapelet_one_event_count, y0, y1


input = open('D:/FYP-Developments/occupancy_data/datatraining.txt', 'rU') #open train data
output = open('D:/FYP-Developments/occupancy_data/res.csv', 'w') #open train data

row_count, zero_count, one_count, shapelet_zero_event_count, x0, x1, shapelet_one_event_count, y0, y1 = totalDatasetAnalysis()

output.close()
input.close()

total_accuracy_zero = (shapelet_zero_event_count/(zero_count))*100
total_accuracy_one = (shapelet_one_event_count/one_count)*100

print("Total Row count: %d" %row_count)
print("Total non occupied events (Occupancy = 0): %d" %zero_count)
print("Total occupied events (Occupancy = 1): %d" %one_count)

print("###################################")

print("Total non occupied events (Occupancy = 0) detected using CEP query generated: %d" %shapelet_zero_event_count)
print("Accuracy of non occupied event detection (Occupancy = 0): %f" %total_accuracy_zero)
print("#####################################")
print("Total occupied events (Occupancy = 1) detected using CEP query generated: %d" %shapelet_one_event_count)
print("Accuracy of occupied event detection (Occupancy = 1): %f" %total_accuracy_one)

