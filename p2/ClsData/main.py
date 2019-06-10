import time
import os
import fileinput
import sys
import random

def calculate_total_len():

    with open('../ProcessedData/ImamKhomeini/concat_all_1 (copy).txt') as outfile1:
        len1 = len(outfile1.readlines())
    with open('../ProcessedData/MohammadRezaPahlavi/concat_all_2 (copy).txt') as outfile2:
        len2 = len(outfile2.readlines())
    return len1 + len2

# only run for the first time
# for line in fileinput.input(["../ProcessedData/ImamKhomeini/concat_all_1 (copy).txt"], inplace=True):
#     sys.stdout.write('Imam {l}'.format(l=line))
with open('../ProcessedData/ImamKhomeini/concat_all_1 (copy).txt') as outfile1:
    string1 = outfile1.read()


# only run for the first time
# for line in fileinput.input(["../ProcessedData/MohammadRezaPahlavi/concat_all_2 (copy).txt"], inplace=True):
#     sys.stdout.write('Shah {l}'.format(l=line))
with open('../ProcessedData/MohammadRezaPahlavi/concat_all_2 (copy).txt') as outfile2:
    string2 = outfile2.read()

with open("concat_2_files.txt", "w") as file1:
    file1.write(string1+"\n"+string2)

total_len = calculate_total_len()
print(total_len)
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

print(len(train_index))
# print(train_index)
print(len(test_index))
# print(test_index)

array = []
with open('concat_2_files.txt') as fille:
    a = fille.read()
    b = a.split("\n")
    for data in b :
        array.append(data)
array.pop()
print(len(array))

# array now has each line of concat data
# for test_ind in test_index:



