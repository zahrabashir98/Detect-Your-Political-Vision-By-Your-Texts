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

flag = True
V = label_1_vocab + label_2_vocab
for word in dictionary_1:
    label_1_frequencies[word] = (dictionary_1[word] + 1) / (label_1_count + V)

for word in dictionary_2:
    label_2_frequencies[word] = (dictionary_2[word] + 1) / (label_2_count + V)

#UNK
label_1_frequencies["UNK"] = 1 / (label_1_count + V)
label_2_frequencies["UNK"] = 1/ (label_2_count + V)

# Test part
with open("test.txt") as test:
    t = test.read()
    test_list = t.split("\n")
test.close()

p_label_1 = {}
p_label_2 = {}

for data in test_list:
    print(data)
    if data != "":
        print("here")
         # Imam
        if data[0] == label1[0]:
            new = data[len(label1)+1:]
            sentence = new.split(" ")
            print(sentence)
            # jomle khali daram
            p_1 = 1
            p_2 = 1
            for word in sentence:
                p_1 *= label_1_frequencies[word]
            for word in sentence:
                p_2 *= label_2_frequencies[word]

            p_label_1[sentence] = p_1
            p_label_2[sentence] = p_2
            print(p_label_1)
            print(p_label_2)
            p_1 = 1
            p_2 = 1

        # Shah
        elif data[0] == label2[0]:
            p_1 = 1
            p_2 = 1
            new = data[len(label2)+1:]
            sentence = new.split(" ")
            # jomle khali daram
            for word in sentence:
                p_1 *= label_1_frequencies[word]
            for word in sentence:
                p_2 *= label_2_frequencies[word]

            p_label_1[sentence] = p_1
            p_label_2[sentence] = p_2
            print(p_label_1)
            print(p_label_2)
            p_1 = 1
            p_2 = 1