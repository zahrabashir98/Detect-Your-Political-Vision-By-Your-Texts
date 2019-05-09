import nltk
nltk.download('punkt')
import re
import inflect
import glob

def stopWordsList():
    with open("stopwords.txt") as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    return content

def tokenize(string):
    return nltk.word_tokenize(string)


def remove_non_ascii(words):
    # new_words = []
    # for word in words:
    #     new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    #     new_words.append(new_word)
    # return new_words
    pass


def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
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
    words = remove_stopwords(words)
    return words

# Main

list_of_dir_1 = glob.glob("../../Data/ImamKhomeini/*.txt")
list_of_dir_2 = glob.glob("../../Data/MohammadRezaPahlavi/*.txt")
# list_of_dir_1 = ["../Data/MohammadRezaPahlavi/1.txt"]

counter1 = 1
counter2 = 1

for name in list_of_dir_1:

    d = open("%s"%name, "r", encoding="utf-8") 
    word_data = d.read()
    tokenized_words = tokenize(word_data)
    words = normalize(tokenized_words)
    print(words)
    with open("../ImamKhomeini/%s.txt"%counter1, 'w') as filehandle:  
        for item in words:
            filehandle.write('%s ' % item)
        filehandle.close()
    counter1 += 1

for name in list_of_dir_2:

    d = open("%s"%name, "r", encoding="utf-8") 
    word_data = d.read()
    tokenized_words = tokenize(word_data)
    words = normalize(tokenized_words)
    print(words)
    with open("../MohammadRezaPahlavi/%s.txt"%counter2, 'w') as filehandle:  
        for item in words:
            filehandle.write('%s ' % item)
        filehandle.close()
    counter2 += 1
