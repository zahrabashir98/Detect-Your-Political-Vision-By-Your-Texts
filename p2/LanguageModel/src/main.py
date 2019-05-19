
unigram_label1_frequencies = {}
unigram_label2_frequencies = {}
bigram_label1_frequencies = {}
bigram_label2_frequencies = {}


def unigram_calculate_frequences(t1,t2,v1,v2):

    # Label 1
    with open("../../ProcessedData/ImamKhomeini/in.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')
        print(len(all_words_list))

        for data in all_words_list:
            if data not in unigram_label1_frequencies:
                unigram_label1_frequencies[data] = 1
                t1 += 1
                v1 += 1

            elif data in unigram_label1_frequencies:
                unigram_label1_frequencies[data] += 1
                t1 += 1
     	

    # Label 2
    with open("../../ProcessedData/MohammadRezaPahlavi/label2.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')
        print(len(all_words_list))

        for data in all_words_list:
            if data not in unigram_label2_frequencies:
                unigram_label2_frequencies[data] = 1
                t2 += 1
                v2 += 1

            elif data in unigram_label2_frequencies:
                unigram_label2_frequencies[data] += 1
                t2 += 1
    return t1,t2,v1,v2

def unigram(word):
    t1,t2,v1,v2 = unigram_calculate_frequences(unigram_label_1_tokens, unigram_label_2_tokens, unigram_label_1_vocab, unigram_label_2_vocab)
    y = input("Train in label1 or label2?\n1/2")
    if y == '1':
        num_of_repeats = unigram_label1_frequencies[word]
        print(num_of_repeats)
        print(t1)
        p_x = (num_of_repeats + 1) /(t1  +v1 + 1)
        print(p_x)

    else :
        num_of_repeats = unigram_label2_frequencies[word]
        print(num_of_repeats)
        print(t2)
        p_x = (num_of_repeats + 1) /(t2  +v2 + 1)
        print(p_x)
    print("**********************")
    return v1,v2

def bigram(word, v1, v2):

    with open("../../ProcessedData/ImamKhomeini/inpp.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    pair_string = ""

    for i in range(len(all_words_list)):
        if i != len(all_words_list)-1:
            pair_string = all_words_list[i] +" "+ all_words_list[i+1]
    
            if pair_string not in bigram_label1_frequencies:
                bigram_label1_frequencies[pair_string] = 1
                pair_string = ""

            elif pair_string in bigram_label1_frequencies:
                bigram_label1_frequencies[pair_string] += 1
                pair_string = ""
    print(bigram_label1_frequencies)
    
    with open("../../ProcessedData/MohammadRezaPahlavi/lebel2_begin_end.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    pair_string = ""
    for i in range(len(all_words_list)):
        if i != len(all_words_list)-1:
            pair_string = all_words_list[i] +" "+ all_words_list[i+1]
    
            if pair_string not in bigram_label2_frequencies:
                bigram_label2_frequencies[pair_string] = 1
                pair_string = ""

            elif pair_string in bigram_label2_frequencies:
                bigram_label2_frequencies[pair_string] += 1
                pair_string = ""

    words = word.split(" ")
    print(words)
    y = input("Train in label1 or label2?\n1/2")

    if y == '1':
        num_of_repeats = bigram_label1_frequencies[word]
        print(num_of_repeats)
        print(type(unigram_label1_frequencies[words[0]]))
        p_x = (num_of_repeats + 1) /(unigram_label1_frequencies[words[0]]  +v1 + 1)
        print(p_x)

    else :
        num_of_repeats = bigram_label2_frequencies[word]
        print(num_of_repeats)
        p_x = (num_of_repeats + 1) /(unigram_label2_frequencies[words[0]]  +v2 + 1)
        print(p_x)

    print("**********************")

        
if __name__ == "__main__":
    unigram_label_1_tokens = 0
    unigram_label_2_tokens = 0
    unigram_label_1_vocab = 0
    unigram_label_2_vocab = 0
    bigram_label_1_tokens = 0
    bigram_label_2_tokens = 0
    bigram_label_1_vocab = 0
    bigram_label_2_vocab = 0
    v1,v2 = unigram("dogs")
    bigram("dogs chase",v1, v2)