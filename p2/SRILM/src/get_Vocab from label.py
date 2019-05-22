with open('label2.txt') as f:
    corpus = f.read()
    corpus = corpus.split()
    vocal = []
    for word in corpus:
        if word not in vocal:
            vocal.append(word)
    vocal.sort() # sorts normally by alphabetical order
    vocal.sort(key=len, reverse=False) # sorts by descending length
with open('vocab2.txt', 'w') as f:
    for word in vocal:
        f.write(word + '\n')