dictionary={}
def get_dictionary(language_model_dirs):
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
            dictionary[key] = value
    return dictionary 


def calculate_perplexity(language_model, text):

    all_words = text.split(" ")
    N = len(all_words)
    UNK = 0.0004
    dictionary = get_dictionary(language_model_dir)
    print(dictionary)
    # p_w = p_w0|<s> + p_w1|w0 + p_w2|w1 +...
    counter = 0
    p = 1
    for i in range(len(all_words)):
        if counter == 0:
            try:
                p0 = float(dictionary[("<s>", "%s"%all_words[0])])
            except:
                p0 = UNK
                N = N+1
            
        else:
            try:
                num = float(dictionary[("%s"%all_words[i-1], "%s"%all_words[i])])
                p *= num
            except:
                p *= UNK
                flag = True

            
        counter +=1
    p = p0 * num
    print(p)
    if flag:
        PP = p**-(1/float(N+1))
    else:
        PP = p**-(1/float(N))
    print("PP = %s"%PP)
    return (PP)


if __name__ == "__main__":
    language_model_dir ="../../Model/label1.2gram.lm"
    calculate_perplexity(language_model_dir, "dogs chase Me")