
unigram_label1_frequencies = {}
unigram_label2_frequencies = {}
bigram_label1_frequencies = {}
bigram_label2_frequencies = {}
trigram_label1_frequencies = {}
trigram_label2_frequencies = {}

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

def unigram():
    t1,t2,v1,v2 = unigram_calculate_frequences(unigram_label_1_tokens, unigram_label_2_tokens, unigram_label_1_vocab, unigram_label_2_vocab)
    file1 = open("../bare_p_1_unigram.txt","w")
    file2 = open("../bare_data_1_unigram.txt","w")
    with open("../label1.1gram.lm", "w") as f1:
        for word in unigram_label1_frequencies:
            num_of_repeats = unigram_label1_frequencies[word]
            # print(num_of_repeats)
            p_x = (num_of_repeats + 1) /(t1  +v1 + 1)
            file1.write("%s\n"%p_x)
            f1.write("%s|%s\n"%(word,p_x))
            file2.write("%s\n"%word)

    f1.close()
    file1.close()

    file1 = open("../bare_p_2_unigram.txt","w")
    file2 = open("../bare_data_2_unigram.txt","w")
    with open("../label2.1gram.lm", "w") as f2:
        for word in unigram_label2_frequencies:
            num_of_repeats = unigram_label2_frequencies[word]
            # print(num_of_repeats)
            p_x = (num_of_repeats + 1) /(t2  +v2 + 1)
            file1.write("%s\n"%p_x)
            f2.write("%s|%s\n"%(word,p_x))
            file2.write("%s\n"%word)
    f2.close()

    return v1,v2

def bigram( v1, v2):

    with open("../../ProcessedData/ImamKhomeini/inpp.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    pair_string = ""
    number_of_start_symbols_1 = 0
    number_of_start_symbols_2 = 0
    
    with open("../bare_bigram_label1.txt", "w") as file1:
        for i in range(len(all_words_list)):
            if i != len(all_words_list)-1:

                if all_words_list[i] == '<s>':
                    number_of_start_symbols_1 += 1

                pair_string = all_words_list[i] +" "+ all_words_list[i+1]
                file1.write(pair_string+"\n")

                if pair_string not in bigram_label1_frequencies:
                    bigram_label1_frequencies[pair_string] = 1
                    pair_string = ""

                elif pair_string in bigram_label1_frequencies:
                    bigram_label1_frequencies[pair_string] += 1
                    pair_string = ""
    print(bigram_label1_frequencies)
    file1.close()

    with open("../../ProcessedData/MohammadRezaPahlavi/lebel2_begin_end.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    pair_string = ""
    with open("../bare_bigram_label2.txt", "w") as file2:
        for i in range(len(all_words_list)):
            if i != len(all_words_list)-1:

                if all_words_list[i] == '<s>' or "<\\s>":
                    number_of_start_symbols_2 += 1

                pair_string = all_words_list[i] +" "+ all_words_list[i+1]
                file2.write(pair_string+"\n")

                if pair_string not in bigram_label2_frequencies:
                    bigram_label2_frequencies[pair_string] = 1
                    pair_string = ""

                elif pair_string in bigram_label2_frequencies:
                    bigram_label2_frequencies[pair_string] += 1
                    pair_string = ""

    # saving language model

    with open("../label1.2gram.lm", "w") as f1:
        for word in bigram_label1_frequencies:
            parts = word.split(" ")
            num_of_repeats = bigram_label1_frequencies[word]
            if parts[0] == "<s>" or "<\\s>":
                p_x = (num_of_repeats + 1) /(number_of_start_symbols_1  +v1 + 1)
            else:
                p_x = (num_of_repeats + 1) /(unigram_label1_frequencies[parts[0]]  +v1 + 1)
            f1.write("%s|%s\n"%(word,p_x))
    f1.close()
    with open("../label2.2gram.lm", "w") as f2:
        for word in bigram_label2_frequencies:
            parts = word.split(" ")
            num_of_repeats = bigram_label2_frequencies[word]
            if parts[0] == "<s>" or "<\\s>":
                p_x = (num_of_repeats + 1) /(number_of_start_symbols_2  +v1 + 1)
            else:
                p_x = (num_of_repeats + 1) /(unigram_label2_frequencies[parts[0]]  +v2 + 1)

            f2.write("%s|%s\n"%(word,p_x))
    f2.close()


def trigram( v1, v2):
    with open("../../ProcessedData/ImamKhomeini/inpp.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    triple_string = ""

    for i in range(len(all_words_list)):
        if i < len(all_words_list)-2:

            triple_string = all_words_list[i] +" "+ all_words_list[i+1] + " " + all_words_list[i+2]

            if triple_string not in trigram_label1_frequencies:
                trigram_label1_frequencies[triple_string] = 1
                triple_string = ""

            elif triple_string in trigram_label1_frequencies:
                trigram_label1_frequencies[triple_string] += 1
                triple_string = ""
    
    
    with open("../../ProcessedData/MohammadRezaPahlavi/lebel2_begin_end.txt") as d:
        content = d.read()
        all_words_list = content.split(' ')

    triple_string = ""

    for i in range(len(all_words_list)):
        if i < len(all_words_list)-2:

            triple_string = all_words_list[i] +" "+ all_words_list[i+1] + " " + all_words_list[i+2]

            if triple_string not in trigram_label2_frequencies:
                trigram_label2_frequencies[triple_string] = 1
                triple_string = ""

            elif triple_string in trigram_label2_frequencies:
                trigram_label2_frequencies[triple_string] += 1
                triple_string = ""
    
    # saving language model
    with open("../label1.3gram.lm", "w") as f1:
        for word in trigram_label1_frequencies:
            parts = word.split(" ")
            num_of_repeats = trigram_label1_frequencies[word]
            p_x = (num_of_repeats + 1) /(bigram_label1_frequencies[parts[0]+" "+ parts[1]]  +v1 + 1)
            f1.write("%s|%s\n"%(word,p_x))
    f1.close()

    with open("../label2.3gram.lm", "w") as f2:
        for word in trigram_label2_frequencies:
            parts = word.split(" ")
            num_of_repeats = trigram_label2_frequencies[word]
            p_x = (num_of_repeats + 1) /(bigram_label2_frequencies[parts[0]+" "+ parts[1]]  +v2 + 1)
            f2.write("%s|%s\n"%(word,p_x))
    f2.close()


if __name__ == "__main__":
    unigram_label_1_tokens = 0
    unigram_label_2_tokens = 0
    unigram_label_1_vocab = 0
    unigram_label_2_vocab = 0

    v1, v2 = unigram()
    bigram(v1, v2)
    trigram(v1, v2)
    # handle if data was UNK