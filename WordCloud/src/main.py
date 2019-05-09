
label1_frequencies = {}
label2_frequencies = {}

# Label 1

with open("../../ProcessedData/ImamKhomeini/label1.txt") as d:
    content = d.read()
    all_words_list = content.split(' ')
    print(len(all_words_list))

    for data in all_words_list:
        if data not in label1_frequencies:
            label1_frequencies[data] = 1

        elif data in label1_frequencies:
            label1_frequencies[data] += 1

with open("frequencies_1.txt", 'w') as f:  
    f.write(str(label1_frequencies))
f.close()

for freq in label1_frequencies:
    label1_frequencies[freq] /= len(all_words_list)/100

with open("frequencies_1_1.txt", 'w') as f:  
    f.write(str(label1_frequencies))
f.close()


# Label 2

with open("../../ProcessedData/MohammadRezaPahlavi/label2.txt") as d:
    content = d.read()
    all_words_list = content.split(' ')
    print(len(all_words_list))

    for data in all_words_list:
        if data not in label2_frequencies:
            label2_frequencies[data] = 1

        elif data in label2_frequencies:
            label2_frequencies[data] += 1

with open("frequencies_2.txt", 'w') as f:  
    f.write(str(label2_frequencies))
f.close()

for freq in label2_frequencies:
    label2_frequencies[freq] /= len(all_words_list)/100

with open("frequencies_2_1.txt", 'w') as f:  
    f.write(str(label2_frequencies))
f.close()