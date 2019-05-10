import nltk
nltk.download('punkt')
nltk.download('wordnet')
  
import re
import inflect
import glob
from num2fawords import words as WORDS
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import unicodedata

def stopWordsList():
    with open("stopwords.txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    return content

def tokenize(string):
    return nltk.word_tokenize(string)


# def remove_non_ascii(words):
#     new_words = []
#     for word in words:
#         new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
#         new_words.append(new_word)
#     return new_words
    

punc = ['.','؟',':','؛','،','»']
def remove_punctuation(words):
    new_words = []
    for word in words:
        if word not in punc:
            new_words.append(word)
    return new_words


def replace_numbers(words):
    # using num2fawords module
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = WORDS(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    new_words = []
    stopwords = stopWordsList()
    for word in words:
        if word not in stopwords:
            new_words.append(word)
    return new_words

def stem_words(words):
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    # words = remove_non_ascii(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    ########################################################################################################
    #  I read somewhere that stopwords are in Normalizing but according to the HW I apply it in WordCloud  #
    ########################################################################################################
    # words = remove_stopwords(words)
    return words

if __name__ == '__main__':

    list_of_dir_1 = glob.glob("../../Data/ImamKhomeini/*.txt")
    list_of_dir_2 = glob.glob("../../Data/MohammadRezaPahlavi/*.txt")

    counter1 = 1
    counter2 = 1
    ImamList = []
    ShahList = []

    # tokenize and normalize label1 +stem +lemmatizing
    for name in list_of_dir_1:
        d = open("%s"%name, "r", encoding="utf-8") 
        word_data = d.read()
        tokenized_words = tokenize(word_data)
        words = normalize(tokenized_words)
        stem1 = stem_words(words)
        lem1 = lemmatize_verbs(words)
        ImamList.append(words)
        counter1 += 1

    with open("../ImamKhomeini/label1.txt", 'w') as filehandle: 
        for lists in ImamList: 
            for item in lists:
                filehandle.write('%s ' % item)
    filehandle.close()

    with open("../ImamKhomeini/stem1.txt", "w") as f1:
        f1.write(str(stem1))
        f1.close()
    with open("../ImamKhomeini/lem1.txt", "w") as f1:
        f1.write(str(lem1))
        f1.close()

    # tokenize and normalize label2 +stem +lemmatizing
    for name in list_of_dir_2:
        d = open("%s"%name, "r", encoding="utf-8") 
        word_data = d.read()
        tokenized_words = tokenize(word_data)
        words = normalize(tokenized_words)
        ShahList.append(words)
        counter2 += 1

    with open("../MohammadRezaPahlavi/label2.txt", 'w') as filehandle:  
        for lists in ShahList: 
            for item in lists:
                filehandle.write('%s ' % item)
    filehandle.close()

    with open("../MohammadRezaPahlavi/stem2.txt", "w") as f2:
        f2.write(str(stem1))
        f2.close()
    with open("../MohammadRezaPahlavi/lem2.txt", "w") as f2:
        f2.write(str(lem1))
        f2.close()
