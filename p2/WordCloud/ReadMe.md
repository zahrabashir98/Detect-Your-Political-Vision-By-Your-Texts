# WordCloud:
I drawd word cloud for these 8 cases:
* label1
* label2
* label1 - label2
* label2 - label1
**and all these four again by removing stopwords**

About label1 and label2 it was clear we give the text to the wordcloud module and it gives a picture according to frequency of word(number of repetitions) and if I wanted to remove wordstops the module had `add_stop_words` method
About cases of 3 and 4(deletions): I caculated the freuencies of each label and saved them in some dictionaries and then I check the commons and then I gave the text to the module agian :D
### Dependencies of this level:
* persian_wordcloud (PersianWordCloud, add_stop_words)

