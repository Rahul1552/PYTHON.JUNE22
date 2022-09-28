
#################################################
#  16.08.2022 
#################################################
# TOPICS TO BE COVERED  
# File  handling/operations  in Python
# CSV
#################################################


#################################################
# CSV | COMMA SEPARATED VALUES
#################################################
#  read and write CSV file

print("************ Reading  a CSV file ******************")

import csv

# with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\one.txt", mode="r" , encoding='utf-8') as f:
#     csv_reader = csv.reader(f)
#     print(list(csv_reader)) # converting the object into list
#     # we will use the properties of list


print("************ Reading  a CSV file using for loop ******************")

with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\one.txt", mode="r" , encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # print(line) # to print rows line by line
        print(line[0])  # to access the first columnn



print("************ writing in a CSV file ******************")

with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\one.txt", mode="r" , encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    with open(r"C:\Users\RAHUL\Documents\OnePython\2.JUNE_22\five.txt", mode="w" , encoding='utf-8') as nf:
        csv_writer = csv.writer(nf,delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)

# for exploring further optional
    csv.DictReader
    csv.DictWriter





