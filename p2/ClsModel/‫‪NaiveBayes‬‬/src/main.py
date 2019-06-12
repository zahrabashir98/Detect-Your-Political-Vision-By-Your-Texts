import math

# with open("../../ClsData/train.txt") as train:
# with open("test/train.txt") as train:
#     string = train.read().split("\n")
# train.close()


inp = input ("You wnat to run program for my data or your TestCase? 1/2 \n")
if inp == "1":
    label1 = "Imam"
    label2 = "Shah"
    write_name = "Test"
    with open("../../../ClsData/train.txt") as train:
        string = train.read().split("\n")
    train.close()
    test_address = "../../../ClsData/test.txt"

elif inp == "2":
    label1 = "c1"
    label2 = "c2"
    write_name = "TestCase"
    with open("test/train.txt") as train:
        string = train.read().split("\n")
    train.close()
    test_address = "test/test.txt"


dictionary_1 = {}
dictionary_2 = {}
label_1_count = 0
label_2_count = 0
V = 0
count_of_docs_1 = 0
count_of_docs_2 = 0

for data in string :

    if data != "":
         # Imam
        if data[0] == label1[0] and data[1] == label1[1]:
            count_of_docs_1 += 1
            new = data[len(label1)+1:]
            sentence = new.split(" ")
            for word in sentence:
                if word not in dictionary_1:
                    dictionary_1[word] = 1
                    label_1_count += 1
                    if word not in dictionary_2:
                        V += 1

                elif word in dictionary_1:
                    dictionary_1[word] += 1
                    label_1_count += 1

        # Shah
        elif data[0] == label2[0] and data[1] == label2[1]:
            count_of_docs_2 += 1
            new = data[len(label2)+1 :]
            sentence = new.split(" ")
            for word in sentence:
                if word not in dictionary_2:
                    dictionary_2[word] = 1
                    label_2_count += 1
                    if word not in dictionary_1:
                        V += 1

                elif word in dictionary_2:
                    dictionary_2[word] += 1
                    label_2_count += 1

label_1_frequencies = {}
label_2_frequencies = {}
class_1_prob = count_of_docs_1/ (count_of_docs_1 + count_of_docs_2)
class_2_prob = count_of_docs_2 / (count_of_docs_1 + count_of_docs_2)

print(count_of_docs_1)
print(count_of_docs_2)
# V += 1
print("V:",V)
for word in dictionary_1:
    label_1_frequencies[word] = (dictionary_1[word] + 1) / (label_1_count + V)

for word in dictionary_2:
    label_2_frequencies[word] = (dictionary_2[word] + 1) / (label_2_count + V)

#UNK
label_1_frequencies["UNK"] = 1 / (label_1_count + V)
label_2_frequencies["UNK"] = 1/ (label_2_count + V)

# Test part
real_category = []
with open(test_address) as test:
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
        real_category.append(correct_label)
        new = data[len(label1)+1:]
        raw_sentences.append(new)
        sentence = new.split(" ")

        p_1 = 0
        p_2 = 0
        for word in sentence:
            if word in label_1_frequencies:
                p_1 += math.log10(label_1_frequencies[word])
            elif word not in label_1_frequencies:
                p_1 += math.log10(label_1_frequencies["UNK"])

        for word in sentence:
            if word in label_2_frequencies:
                p_2 += math.log10(label_2_frequencies[word])
            else:
                p_2 += math.log10(label_2_frequencies["UNK"])
        
        p_1 += math.log10(class_1_prob)
        p_2 += math.log10(class_2_prob)
        p_label_1[new] = p_1
        p_label_2[new] = p_2

estimated_label = []
counter = 0
with open("../%s.output.txt"%(write_name), "w") as file1:
    for s in raw_sentences:
        counter += 1
        print("%s %s %s %s"%(label1, p_label_1[s], label2, p_label_2[s]))
        file1.write("%s %s %s %s"%(label1, p_label_1[s], label2, p_label_2[s]))
        if counter < len(raw_sentences):
            file1.write("\n")

        if p_label_1[s] > p_label_2[s] :
            estimated_label.append(label1)
        else:
            estimated_label.append(label2)
file1.close()


print(estimated_label)
print(real_category)
tp = 0
tn = 0
fp = 0
fn = 0
label1_fields = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
label2_fields = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}

for i in range(len(real_category)):
    if estimated_label[i] == label1 and  real_category[i]== label1:
        label1_fields['tp'] += 1
        label2_fields['tn'] += 1

    elif estimated_label[i] == label2 and  real_category[i]== label2:
        label2_fields['tp'] += 1
        label1_fields['tn'] += 1
    
    elif estimated_label[i] == label2 and  real_category[i]== label1:
        label1_fields['fn'] += 1
        label2_fields['fp'] += 1

    elif estimated_label[i] == label1 and  real_category[i]== label2:
        label2_fields['fn'] += 1
        label1_fields['fp'] += 1


tp = label1_fields['tp'] + label2_fields['tp']
tn = label1_fields['tn'] + label2_fields['tn']
fp = label1_fields['fp'] + label2_fields['fp']
fn = label1_fields['fn'] + label2_fields['fn']

total_precision = (tp) / (tp + fp)
total_recall = (tp) / (tp + fn)
total_f1 = 2* (total_precision * total_recall) / (total_precision + total_recall)
total_accuracy = (tp + tn) / (tp + tn + fp + fn)

label1_precision = (label1_fields['tp']) / (label1_fields['tp'] + label1_fields['fp'])
label1_recall = (label1_fields['tp']) / (label1_fields['tp'] + label1_fields['fn'])
label1_f1 = 2* (label1_precision * label1_recall) / (label1_precision + label1_recall)
label1_accuracy = (label1_fields['tp'] + label1_fields['tn']) / (label1_fields['tp'] + label1_fields['tn'] + label1_fields['fp'] + label1_fields['fn'])

label2_precision = (label2_fields['tp']) / (label2_fields['tp'] + label2_fields['fp'])
label2_recall = (label2_fields['tp']) / (label2_fields['tp'] + label2_fields['fn'])
label2_f1 = 2* (label2_precision * label2_recall) / (label2_precision + label2_recall)
label2_accuracy = (label2_fields['tp'] + label2_fields['tn']) / (label2_fields['tp'] + label2_fields['tn'] + label2_fields['fp'] + label2_fields['fn'])
print(p_label_1)
print(p_label_2)

with open("../%s.report.txt‬‬"%write_name, "w") as file1:
    file1.write("%s\n%s\n%s\n%s" %(total_recall, total_precision, total_f1, total_accuracy))