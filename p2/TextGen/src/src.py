import random
unigram_dict_1 = {}
unigram_dict_2 = {}
bigram_dict_1 = {}

def get_unigram_dixt():
    with open("../../Model/label1.1gram.lm") as f2:
        d = f2.read().split("\n")
        u1 = []

        for data in d:
            u1.append(data.replace("|"," "))
        u1.pop()
        # print(u1)
        for data in u1:
            key = data.split(" ")[0]
            value = data.split(" ")[1]
            unigram_dict_1[key] = value
    return unigram_dict_1


def get_unigram_dixt_2():
    with open("../../Model/label2.1gram.lm") as f2:
        d = f2.read().split("\n")
        u2 = []

        for data in d:
            u2.append(data.replace("|"," "))
        u2.pop()
        # print(u2)
        for data in u2:
            key = data.split(" ")[0]
            value = data.split(" ")[1]
            unigram_dict_2[key] = value
    return unigram_dict_2

def get_bigram_dict_1():
    with open("../../Model/label1.2gram.lm") as f1:
        d = f1.read().split("\n")
        u1 = []

        for data in d:
            u1.append(data.replace("|"," "))
        u1.pop()
        # print(u1)
        for data in u1:
            key = data.split(" ")[0],data.split(" ")[1]
            value = data.split(" ")[2]
            bigram_dict_1[key] = value
    return bigram_dict_1 


def get_random_word_unigram1(p):
    print(p)
    sum = 0
    for key, value in unigram_dict_1.items():          
        sum += float(value)
        try:
            print("in try")
            if p <= sum:
                print("iff")
                return key
            else:
                print("else")
                continue
        except:
            print("except")
            return "."        


def get_random_word_unigram2(p):
    print(p)
    sum = 0
    for key, value in unigram_dict_2.items():
        # print("KEYYYYYYYYYYYYYYYY")        
        # print(key)
        # print(value)
        if value == "":
            value = 0.0002
        sum += float(value)
        try:
            if p <= sum:
                return key
            else:
                continue
        except:
            return "."        
             
def get_random_word_bigram1(p):

    sum = 0
    for key, value in bigram_dict_1.items():          
        sum += float(value)
        if p <= sum:
            return key


if __name__ == '__main__':
    
    # print("LABEL1")
    seed_number = input("Enter seed : ")
    random.seed(seed_number)
    # n1 = int(input ("enter n for label1 unigram: "))
    # unigram_dict_1 = get_unigram_dixt()
    # string = ""
    # new_word= ""
    # num = []
    # # random values
    # for i in range(n1):
    #     num.append(int(random.random()*100)%5)
    
    # with open("../‫‪label1.1gram.gen‬‬","w") as f1:
    #     for i in range(n1):
    #         string = ""
    #         for j in range(num[i]):
    #             new_word =  get_random_word_unigram1(random.random())
    #             # print(new_word)
    #             string += " " + new_word
    #         print(string+".")
    #         f1.write(string[1:len(string)]+"."+"\n")
    
    # print("**********************")
    # print("LABEL2")
    # seed_number = input("Enter seed : ")
    # random.seed(seed_number)
    # n2 = int(input ("enter n for label2 unigram: "))
    # unigram_dict_2 = get_unigram_dixt_2()
    # string = ""
    # new_word= ""
    # num = []
    # # random values
    # for i in range(n2):
    #     num.append(int(random.random()*100)%6)

    # with open("../‫‪label2.1gram.gen‬‬","w") as f2:
    #     for i in range(n2):
    #         print("BARE+%s om"%i)
    #         string = ""
    #         for j in range(num[i]):
    #             new_word =  get_random_word_unigram2(random.random())
    #             # print(new_word)
    #             if new_word == "":
    #                 j = 0
    #             if new_word != "":
    #                 string += " " + new_word
    #         print(string+".")
    #         f2.write(string[1:len(string)]+"."+"\n")


    n1 = int(input ("enter n for label1 bigram: "))
    # bigram
    bigram_dict_1= get_bigram_dict_1()
    new_word = ["",""]
    string = ""
    counter = 0

    for i in range(n1):
        string = ""
        counter = 0
        new_word = ["",""]
        while(new_word[1]!= "<\s>"  ):
            if counter == 0 :
                new_word = get_random_word_bigram1(random.random())
                if new_word[0] == "<s>":
                    string += " " + new_word[0] + new_word [1]
                    counter += 1
            else:
                new_word = get_random_word_bigram1(random.random())
                if new_word[0] != "<s>":
                    string += " " + new_word[0] + new_word [1]
                    counter += 1
    
        print(string)
        print("\n")
        # while(new_word[0]!="<s>"):

            # value = all_words[random_number]
            # words = value.split(" ")
            # if words[0]== "<s>":
            #     string += " " + value





# with open("../../ProcessedData/MohammadRezaPahlavi/lebel2_begin_end.txt") as d:
#     all_words = (d.read()).split(' ')
# print("*********************")

# with open("../label2.1gram.gen", "w") as f1:
#     for i in range(n2):
#         input_seed = int(input("enter seed : "))
#         print ("Random number with seed %s\n"%input_seed)
#         random.seed( input_seed )
#         value = ""
#         string = ""
#         while(value != '<\s>'):
#             random_number = random.randint(0,len(all_words)-1)
           
#             value = all_words[random_number]
#             if value != '<s>':
#                 string += " "+ value
#         print(string[1:len(string)])
#         f1.write(string[1:len(string)]+"\n")
#         print("------------")

# #################################################################################

# n1 = int(input ("enter n for label1 Bigram: "))

# with open("../../Model/bare_bigram_label1.txt") as d:
#     all_words = (d.read()).split('\n')
# print("*********************")

# with open("../label1.2gram.gen", "w") as f1:
#     for i in range(n1):
#         input_seed = int(input("enter seed : "))
#         print ("Random number with seed %s\n"%input_seed)
#         random.seed(input_seed)
#         value = ""
#         string = ""
#         words = ["", ""]
#         counter = 0

#         while(words[1] != '<\s>'):
#             if counter != 0 :
#                 random_number = random.randint(0,len(all_words)-1)
#                 value = all_words[random_number]
#                 words = value.split(" ")
#                 string += " " + value
#             elif counter == 0:
#                 while(words[0]!="<s>"):
#                     # rahe dige inke beine oona ke <s> daran bezani
#                     random_number = random.randint(0,len(all_words)-1)
#                     value = all_words[random_number]
#                     words = value.split(" ")
#                     if words[0]== "<s>":
#                         string += " " + value
                

#         print(string[1:len(string)])
#         f1.write(string[1:len(string)]+"\n")
#         print("------------")

# print("\n\n")


# n2 = int(input ("enter n for label2 Bigram: "))

# with open("../../Model/bare_bigram_label2.txt") as d:
#     all_words = (d.read()).split('\n')
# print("*********************")

# with open("../label2.2gram.gen", "w") as f2:
#     for i in range(n2):
#         input_seed = int(input("enter seed : "))
#         print ("Random number with seed %s\n"%input_seed)
#         random.seed(input_seed)
#         value = ""
#         string = ""
#         words = ["", ""]
#         while(words[1] != '<\s>'):
#             random_number = random.randint(0,len(all_words)-1)
#             value = all_words[random_number]
#             words = value.split(" ")
#             string += " " + value

#         print(string[1:len(string)])
#         f2.write(string[1:len(string)]+"\n")
#         print("------------")
