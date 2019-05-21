import random

def split_data(all_words_list,label, num, f):

    train_len = (len(all_words_list) * 8)//10
    test_len = (len(all_words_list)) - (train_len)
    # print(train_len)
    # print(test_len )

    test_data  = random.sample(all_words_list,test_len)
    for test in test_data:
        all_words_list.remove(test)
    train_data = all_words_list

    train_string = ""
    if f != 10:
        with open("../%s/train/label%s.txt"%(label, num), "w") as f1:
            for tr in train_data:
                f1.write('%s ' % tr)
            f1.close()

        with open("../%s/test/label%s.txt"%(label, num), "w") as f2:
            for te in test_data:
                f2.write('%s ' % te)
            f2.close()
    if f == 10:
        with open("../%s/train/label%s_begin_end.txt"%(label, num), "w") as f1:
            for tr in train_data:
                f1.write('%s ' % tr)
            f1.close()

        with open("../%s/test/label%s_begin_end.txt"%(label, num), "w") as f2:
            for te in test_data:
                f2.write('%s ' % te)
            f2.close()


if __name__ == "__main__":
    with open("../../ProcessedData/ImamKhomeini/label1.txt") as d:
        string1 = d.read()
        all_words_list = string1.split(' ')
        split_data(all_words_list,"ImamKhomeini", "1",9)
        print(len(all_words_list))

    with open("../../ProcessedData/MohammadRezaPahlavi/label2.txt") as d:
        string2 = d.read()
        all_words_list = string2.split(' ')
        split_data(all_words_list,"MohammadRezaPahlavi", "2",9)
        print(len(all_words_list))
    
    with open("../../ProcessedData/ImamKhomeini/lebel1_begin_end.txt") as d:
        string2 = d.read()
        all_words_list = string2.split(' ')
        split_data(all_words_list,"ImamKhomeini", "1",10)
        print(len(all_words_list))
    
    with open("../../ProcessedData/MohammadRezaPahlavi/lebel2_begin_end.txt") as d:
        string2 = d.read()
        all_words_list = string2.split(' ')
        split_data(all_words_list,"MohammadRezaPahlavi", "2",10)
        print(len(all_words_list))
