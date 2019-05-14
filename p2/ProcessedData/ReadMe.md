# Data PreProcessing:

In this level we have two major works to do :
**1. tokenizing**
**2. normalizing**
Also I read somewehre that we do `stemming` and `lemmatizing` in this step so I did it as an extra work(not influencing the process)

What I didi here was the follwing items:
- **Tokenizing :** I did it by `nltk` library of python.
- **Normalizing:**
    - **which contains the fowlling steps:**
        1.  remove_punctuation
        2.  replace_numbers with alphabets
        3.  remove_non_ascii
        4.  remove_stopwords (I read that normalizing contains it but according to the doc I did this step at WordCloud level)
        5.  (Optional) steming
        6.  (Optional) lemmatizing

### Dependencies of this level:
* nltk
* inflect
* num2fawords
* unicodedata
* nltk.stem.lancaster
* nltk.stem.wordnet
* you can get most of them by pip install ...

