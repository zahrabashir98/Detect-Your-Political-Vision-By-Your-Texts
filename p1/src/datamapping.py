from collections import defaultdict
import csv

# i have another python file in my package which its task is
# to mapp the phonetic sentences to persian words and write them to a file

def dataMapping():
    data = []
    with open('../out/phonetics_states.txt') as my_file:
        m = my_file.readlines()
        for i in m:
            data.append(i.rstrip('\n').split(" "))

    dic = {}
    with open("../in/Entries.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            dic[row[0]] = row[1]

    answers = defaultdict(list) 

    f = open("../out/final_answer.txt", "w") 
    counter = 0
    for d in data :
        for i  in range(len(d)):

            for key, value in dic.items():
                if key == d[i] :
                    answers[counter].append(value)
        counter += 1

    for value in answers:
        print(answers[value])
        f.write(str(answers[value]))
        f.write("\n")

dataMapping()