with open("../../ClsData/train.txt") as train:
    string = train.read().split("\n")
train.close()

label1 = "Imam"
label2 = "Shah"
dictionary_1 = {}
dictionary_2 = {}
label_1_count = 0
label_2_count = 0
label_1_vocab = 0
label_2_vocab = 0
for data in string :

    if data != "":
         # Imam
        if data[0] == label1[0]:
            new = data[len(label1)+1:]
            sentence = new.split(" ")
            for word in sentence:
                if word not in dictionary_1:
                    dictionary_1[word] = 1
                    label_1_count += 1
                    label_1_vocab += 1

                elif word in dictionary_1:
                    dictionary_1[word] += 1
                    label_1_count += 1

        # Shah
        elif data[0] == label2[0]:
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


label_1_frequencies = {}
label_2_frequencies = {}
# print(dictionary_1[])
V = label_1_vocab + label_2_vocab
for word in dictionary_1:
    label_1_frequencies[word] = dictionary_1[word] + 1 / label_1_count + V

for word in dictionary_2:
    label_2_frequencies[word] = dictionary_2[word] + 1 / label_2_count + V

# print(label_1_frequencies)
# print(dictionary_1)