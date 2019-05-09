import glob
import os


punc = ['.','؟',':','؛','،','»']
def extract(string):
    for pun in punc:
        string = string.replace(pun, ' ')
    # print(string)
    return string


list_of_dir_1 = glob.glob("../../RawData/ImamKhomeini/*.txt")
list_of_dir_2 = glob.glob("../../RawData/MohammadRezaPahlavi/*.txt")
counter1 = 1
counter2 = 1

for name in list_of_dir_1:
    d = open("%s"%name, "r", encoding="utf-8") 
    string = extract(d.read())
    f = open("../ImamKhomeini/%s.txt"%counter1, "w")
    f.write(string)
    f.close()
    counter1 += 1

for name in list_of_dir_2:
    d = open("%s"%name, "r", encoding="utf-8") 
    string = extract(d.read())
    f = open("../MohammadRezaPahlavi/%s.txt"%counter2, "w")
    f.write(string)
    f.close()
    counter2 += 1
