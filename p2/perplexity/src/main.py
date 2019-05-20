unigram_dictionary = {}

def get_unigram_dictionary(language_model_dirs):
    with open(language_model_dir) as f1:
        d = f1.read().split("\n")
        u1 = []

        for data in d:
            u1.append(data.replace("|"," "))
        u1.pop()
        for data in u1:
            key = data.split(" ")[0]
            value = data.split(" ")[1]
            unigram_dictionary[key] = value
    return unigram_dictionary 

def calculate_unigram_perplexity(language_model, text):

    all_words = text.split(" ")
    N = len(all_words)
    UNK = 0.0004
    unigram_dictionary = get_unigram_dictionary(language_model_dir)
    print(unigram_dictionary)

    p = 1
    flag = False

    for i in range(len(all_words)):
        try:
            p *= float(all_words[i])
        except:
            p *= UNK
            flag =True

    print(p)
    if flag:
        PP = p**-(1/float(N+1))
    else:
        PP = p**-(1/float(N))
    print("PP = %s"%PP)
    return PP


#**************************************************************************#
bigram_dictionary = {}
def get_bigram_dictionary(language_model_dirs):
    with open(language_model_dir) as f1:
        d = f1.read().split("\n")
        u1 = []

        for data in d:
            u1.append(data.replace("|"," "))
        u1.pop()
        # print(u1)
        for data in u1:
            key = data.split(" ")[0],data.split(" ")[1]
            value = data.split(" ")[2]
            bigram_dictionary[key] = value
    return bigram_dictionary 


def calculate_bigram_perplexity(language_model, text):

    all_words = text.split(" ")
    N = len(all_words)
    UNK = 0.0004
    bigram_dictionary = get_bigram_dictionary(language_model_dir)
    print(bigram_dictionary)
    # p_w = p_w0|<s> + p_w1|w0 + p_w2|w1 +...
    counter = 0
    p = 1
    flag = False
    for i in range(len(all_words)):
        if counter == 0:
            try:
                p0 = float(bigram_dictionary[("<s>", "%s"%all_words[0])])
            except:
                p0 = UNK
                N = N+1
            
        else:
            try:
                num = float(bigram_dictionary[("%s"%all_words[i-1], "%s"%all_words[i])])
                p *= num
            except:
                p *= UNK
                flag = True

            
        counter +=1
    p = p * p0
    print(p)
    if flag:
        PP = p**-(1/float(N+1))
    else:
        PP = p**-(1/float(N))
    print("PP = %s"%PP)
    return PP

#**********************************************************************************#
trigram_dictionary={}
def get_trigram_dictionary(language_model_dirs):
    with open(language_model_dir) as f1:
        d = f1.read().split("\n")
        u1 = []

        for data in d:
            u1.append(data.replace("|"," "))
        u1.pop()
        # print(u1)
        for data in u1:
            # print(data.split(" "))
            key = (data.split(" ")[0], data.split(" ")[1], data.split(" ")[2])
            value = data.split(" ")[3]
            trigram_dictionary[key] = value
    return trigram_dictionary 


def calculate_trigram_perplexity(language_model, text):

    all_words = text.split(" ")
    N = len(all_words)
    UNK = 0.0004
    trigram_dictionary = get_trigram_dictionary(language_model_dir)
    print(trigram_dictionary)
    counter = 0
    p = 1
    flag = False
    for i in range(len(all_words)):
        if counter == 0:
            try:
                p0 = float(trigram_dictionary[("<s>", "%s"%all_words[0], "%s"%all_words[1])])
                print(trigram_dictionary[("<s>", "%s"%all_words[0], "%s"%all_words[1])])
            except:
                p0 = UNK
                N = N+1
            
        else:
            try:
                if i >1:
                    num = float(trigram_dictionary[("%s"%all_words[i-2], "%s"%all_words[i-1], "%s"%all_words[i])])
                    print(num)
                    p *= num
            except:
                p *= UNK
                flag = True

            
        counter +=1
    p = p * p0

    if flag:
        PP = p**-(1/float(N+1))
    else:
        PP = p**-(1/float(N))
    print("PP = %s"%PP)
    return (PP)


if __name__ == "__main__":
    tyype = input("What is your language model type?\n1)unigram\n2)bigram\n3)trigram")
    if tyype == "1":
        language_model_dir = "../../Model/label1.1gram.lm"
        text = "dogs chase cats"
        calculate_unigram_perplexity(language_model_dir, text)

    if tyype == "2":
        language_model_dir = "../../Model/label1.2gram.lm"
        text = "dogs chase cats"
        calculate_bigram_perplexity(language_model_dir, text)

    if tyype == "3":
        language_model_dir = "../../Model/label1.3gram.lm"
        text = "dogs chase cats"
        calculate_trigram_perplexity(language_model_dir, text)
