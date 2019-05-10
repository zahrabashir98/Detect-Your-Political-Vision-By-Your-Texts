
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words


label1_frequencies = {}
label2_frequencies = {}


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
    image.save('result%s.png'%number)


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
    image.save('result%s.png'%number)

if __name__ == '__main__':
    
    text1 = open('../../ProcessedData/ImamKhomeini/label1.txt', encoding='utf-8').read()
    text2 = open('../../ProcessedData/MohammadRezaPahlavi/label2.txt', encoding='utf-8').read()

    manual = False
    # I set it false because I have recorded the results one time
    if manual:
        calculate_frequences()

    wc_without_removing_stopWords(text1, 1)
    wc_without_removing_stopWords(text2, 2)
    wc_with_removing_stopWords(text1, 3)
    wc_with_removing_stopWords(text2, 4)

    calculate
    wc_of_label1_minus_label2(text, 5)
    wc_of_label2_minus_label1(text, 6)
    wc_of_label1_minus_label2_removeStopWords(text, 7)
    wc_of_label2_minus_label1_removeStopWords(text, 8)




