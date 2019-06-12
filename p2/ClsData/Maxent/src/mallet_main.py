import time
import os
import fileinput
import sys
import random

def get_arabic_words():
    arabic_list = ["اعوذ","بالله","الشیطان","الرجیم","بسم","الله","الرحمن","الرحیم","رب","سید","الحمدلله","لله","والسلام","غلیکم"]
    return arabic_list

def create_input_fromat(words, label):

    mini_dictionary = {}
    bigram_dictionary = {}
    arabic = False
    length = len(words)
    arabic_dictionary = get_arabic_words()

    # 1gram
    for word in words:
        if word in mini_dictionary:
            mini_dictionary[word] +=1
        elif word not in mini_dictionary:
            mini_dictionary[word] = 1

    # 2gram
    for i in range(len(words)):
        if len(words) <= 2:
            break
        string  = ""
        # seperating bigrams by _
        string = "%s_%s" %(words[i],words[i+1])
        
        if string in bigram_dictionary:
            bigram_dictionary[string] += 1
        elif word not in bigram_dictionary:
            bigram_dictionary[string] = 1

        if i == len(words) -2 :
            break

    string_fromat = label 
    for data in mini_dictionary:
        s = ""
        s = "f_%s:%s" %(data, mini_dictionary[data])
        string_fromat += " " + s

    for data in bigram_dictionary:
        s = ""
        s = "f_%s:%s" %(data, bigram_dictionary[data])
        string_fromat += " " + s

    string_fromat += " " + "length:%s"%length
    for word in words:
        if word in arabic_dictionary:
            arabic = True
            break
        elif word not in arabic_dictionary:
            pass

    if arabic == True:
        string_fromat += " " + "has_arabic:1"
    else:
        string_fromat += " " + "has_arabic:0"
    # print(string_fromat)
    return string_fromat


label1 = "Imam"
label2 = "Shah"

# train
with open("../../train.txt") as file1:
    string = file1.read().split("\n")
file1.close()
string.pop()

with open("../‫‪input.train.txt‬‬", "w") as filehandle:
    for data in string :
        words = data[len(label1)+1:].split(" ")
        label = data[0:len(label1)]
        string_fromat = create_input_fromat(words, label)
        filehandle.write(string_fromat+"\n")
filehandle.close

# test
with open("../../test.txt") as file2:
    string = file2.read().split("\n")
file2.close()
string.pop()

with open("../‫‪input.test.txt‬‬", "w") as filehandle:
    for data in string :
        words = data[len(label1)+1:].split(" ")
        label = data[0:len(label1)]
        string_fromat = create_input_fromat(words, label)
        filehandle.write(string_fromat+"\n")
filehandle.close
