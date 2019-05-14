
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words


label1_frequencies = {}
label2_frequencies = {}
str1 = ""
str2 = ""
######################################################################################
##        calculate each label's frequency(number of repeats) in order to           ##
##  have a manual wordcloud. And I can also check the correctness of module above.  ##
######################################################################################

def calculate_frequences():

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
    
     	
    copy_freq_1 = label1_frequencies.copy()
    for freq in copy_freq_1:
        copy_freq_1[freq] /= len(all_words_list)/100

    with open("frequencies_1_1.txt", 'w') as f:  
        f.write(str(copy_freq_1))
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

    copy_freq_2 = label2_frequencies.copy()
    for freq in copy_freq_2:
        copy_freq_2[freq] /= len(all_words_list)/100

    with open("frequencies_2_1.txt", 'w') as f:  
        f.write(str(copy_freq_2))
    f.close()



def getStopWordsList():
    with open("stopwords.txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    return content

def wc_without_removing_stopWords(text, number):

    wordcloud = PersianWordCloud(
        only_persian=True,
        max_words=100,
        margin=0,
        width=800,
        height=800,
        min_font_size=1,
        max_font_size=500,
        background_color="black"
    ).generate(text)
    image = wordcloud.to_image()
    image.show()
    image.save('../out/%s.jpg'%number)


def wc_with_removing_stopWords(text, number):
    
    stopWordsList= getStopWordsList()
    stopwords = add_stop_words(stopWordsList)

    wordcloud = PersianWordCloud(
        only_persian=True,
        max_words=100,
        stopwords=stopwords,
        margin=0,
        width=800,
        height=800,
        min_font_size=1,
        max_font_size=500,
        background_color="black"
    ).generate(text)
    image = wordcloud.to_image()
    image.show()
    image.save('../out/%s.jpg'%number)

def calculate_label1_minus_label2():

    label2_freq_copy = label2_frequencies.copy()
    label1_freq_copy = label1_frequencies.copy()

    for data2 in label2_freq_copy:
        if data2 in label1_freq_copy:
            label1_freq_copy[data2] -= label2_freq_copy[data2]
            continue
    str1 = ""
    for word in label1_freq_copy:
        if label1_freq_copy[word] >0:
            str1 += "%s "%word
    print(str1)
    return str1


def calculate_label2_minus_label1():

    label1_freqq_copy = label1_frequencies.copy()
    label2_freqq_copy = label2_frequencies.copy()


    for data1 in label1_freqq_copy:
        if data1 in label2_freqq_copy:
            label2_freqq_copy[data1] -= label1_freqq_copy[data1]
            continue
    str2 = ""
    for word in label2_freqq_copy:
        if label2_freqq_copy[word] >0:
            str2 += "%s "%word
    return str2


if __name__ == '__main__':
    
    text1 = open('../../ProcessedData/ImamKhomeini/label1.txt', encoding='utf-8').read()
    text2 = open('../../ProcessedData/MohammadRezaPahlavi/label2.txt', encoding='utf-8').read()

    manual = True
    # I set it false because I have recorded the results one time
    if manual:
        calculate_frequences()

    wc_without_removing_stopWords(text1, 1)
    wc_without_removing_stopWords(text2, 2)
    wc_with_removing_stopWords(text1, 3)
    wc_with_removing_stopWords(text2, 4)
    new_text1 = calculate_label1_minus_label2()
    new_text2 = calculate_label2_minus_label1()
    wc_without_removing_stopWords(new_text1, 5)
    wc_without_removing_stopWords(new_text2, 6)
    wc_with_removing_stopWords(new_text1, 7)
    wc_with_removing_stopWords(new_text2, 8)




