import math

# with open("../../ClsData/train.txt") as train:
with open("test/train.txt") as train:
    string = train.read().split("\n")
train.close()

# Shah Imam
label1 = "c1"
label2 = "c2"
dictionary_1 = {}
dictionary_2 = {}
label_1_count = 0
label_2_count = 0
label_1_vocab = 0
label_2_vocab = 0

for data in string :

    if data != "":
         # Imam
        if data[0] == label1[0] and data[1] == label1[1]:
            print()
            new = data[len(label1)+1:]
            sentence = new.split(" ")
            print(sentence)
            for word in sentence:
                if word not in dictionary_1:
                    dictionary_1[word] = 1
                    label_1_count += 1
                    label_1_vocab += 1

                elif word in dictionary_1:
                    dictionary_1[word] += 1
                    label_1_count += 1

        # Shah
        elif data[0] == label2[0] and data[1] == label2[1]:
            new = data[len(label2)+1 :]
            sentence = new.split(" ")
            for word in sentence:
                if word not in dictionary_2:
                    dictionary_2[word] = 1
                    label_2_count += 1
                    label_2_vocab += 1

                elif word in dictionary_2:
                    dictionary_2[word] += 1
                    label_2_count += 1
print(dictionary_1)

label_1_frequencies = {}
label_2_frequencies = {}

flag = True
V = label_1_vocab + label_2_vocab
print(V)

for word in dictionary_1:
    label_1_frequencies[word] = (dictionary_1[word] + 1) / (label_1_count + V)

for word in dictionary_2:
    label_2_frequencies[word] = (dictionary_2[word] + 1) / (label_2_count + V)

#UNK
label_1_frequencies["UNK"] = 1 / (label_1_count + V)
label_2_frequencies["UNK"] = 1/ (label_2_count + V)

# Test part
with open("test/test.txt") as test:
    t = test.read()
    test_list = t.split("\n")
test.close()

p_label_1 = {}
p_label_2 = {}
raw_sentences = [] 

# notice to use upper case / len of both data labels are the same
for data in test_list:

    if data != "":

        correct_label = data[0:len(label1)]
        new = data[len(label1)+1:]
        raw_sentences.append(new)
        sentence = new.split(" ")

        p_1 = 1
        p_2 = 1
        for word in sentence:
            if word in label_1_frequencies:
                p_1 *= label_1_frequencies[word]
            elif word not in label_1_frequencies:
                p_1 *= label_1_frequencies["UNK"]

        for word in sentence:
            if word in label_2_frequencies:
                p_2 *= label_2_frequencies[word]
            else:
                p_2 *= label_2_frequencies["UNK"]
        
        print(p_1 )
        p_label_1[new] = math.log10(p_1)
        p_label_2[new] = math.log10(p_2)
        # print(p_label_1)
        # print(p_label_2)
        p_1 = 1
        p_2 = 1


for s in raw_sentences:
    print("%s %s %s %s"%(label1, p_label_1[s], label2, p_label_2[s]))
# print("Estomated value:",max())