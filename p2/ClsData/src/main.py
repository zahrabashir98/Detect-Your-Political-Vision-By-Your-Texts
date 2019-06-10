import time
import os
import fileinput
import sys
import random

# horoofe ezafaro hazf konnn
def calculate_total_len():

    with open('../../ProcessedData/ImamKhomeini/tagged_data_1.txt') as outfile1:
        len1 = len(outfile1.readlines())
    with open('../../ProcessedData/MohammadRezaPahlavi/tagged_data_2.txt') as outfile2:
        len2 = len(outfile2.readlines())
    return len1 + len2

# only run for the first time
# for line in fileinput.input(["../ProcessedData/ImamKhomeini/tagged_data_1.txt"], inplace=True):
#     sys.stdout.write('Imam {l}'.format(l=line))
with open('../../ProcessedData/ImamKhomeini/tagged_data_1.txt') as outfile1:
    string1 = outfile1.read()


# only run for the first time
# for line in fileinput.input(["../ProcessedData/MohammadRezaPahlavi/tagged_data_2.txt"], inplace=True):
#     sys.stdout.write('Shah {l}'.format(l=line))
with open('../../ProcessedData/MohammadRezaPahlavi/tagged_data_2.txt') as outfile2:
    string2 = outfile2.read()

with open("../merged_file.txt", "w") as file1:
    file1.write(string1+"\n"+string2)

total_len = calculate_total_len()
train_len  = int(0.8 * total_len)
test_len = total_len - train_len

train_index = []
total_index = []
for i in range(total_len):
    total_index.append(i)
test_index  = random.sample(total_index, test_len)

for index in test_index:
    total_index.remove(index)
train_index = total_index

array = []
with open('../merged_file.txt') as fille:
    a = fille.read()
    b = a.split("\n")
    for data in b :
        array.append(data)
array.pop()
# print(len(array))

# array now has each line of concat data
with open("../train.txt", "w")as train_file:
    for train_ind in train_index:
        train_file.write(array[train_ind]+"\n")

with open("../test.txt", "w")as test_file:
    for test_ind in test_index:
        test_file.write(array[test_ind]+"\n")
