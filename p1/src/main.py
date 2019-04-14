import csv
import sys
from collections import defaultdict

#######################################################################
###                                                                 ###
###   Notice running it only with python3 (not any lower version)   ###
###                                                                 ###
#######################################################################

# here is the function which assembles all phonetics of input
def phoneticGenerator(sentence):
    phonetic = ""
    for item in sentence:
        for key, value in dic.items():
            if key == item :
                phonetic += value
    return phonetic


# this function checks wether the input word is in dataset or not
def is_in_dataset(word):

    for i in range(len(all_phonetics)):
        
        if all_phonetics[i] == word :
            return True
    return False


# here is the function which first calls "breakWord"
def input(string):
    breakWord(string, len(string), "")


# this is my recursive function
def breakWord( string,  n,  result):

    # worde breaking procedure 
    for i in range(1,n+1):
        prefix = string[0:i]

        if (is_in_dataset(prefix)) :
            # if reached end of sentence
            if (i == n):
                result += prefix
                print(result)    
                f.write(result)
                f.write("\n")
                return
            # call "breakWord" recursively for the rest of word
            breakWord(string[i:n+1], n-i, result + prefix + " ")


if __name__ == '__main__':

    f = open("../out/phonetics_states.txt", "w")
    all_phonetics = []
    word_phonetic_map = {}
    dic = {}
    with open("../in/Entries.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # i have a dictionary with keys of persian_words and values of phonetics
            dic[row[1]] = row[0]
            i = 0
            for each_data in row:
                if i%5 == 0:
                    all_phonetics.append(each_data)
                
                i += 1

    sentence = ""
    with open("../in/%s.txt"%sys.argv[1]) as inp:
        input_data = inp.readlines()
        # notice you should't have any extra line in your input
        for line in input_data:
            sentence = line.rstrip('\n').split(" ")
            
    phonetic = phoneticGenerator(sentence)

    input(phonetic)
