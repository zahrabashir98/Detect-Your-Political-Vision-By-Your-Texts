import random

# category = input("Genreate Text for Label1 or Label2?")

# sum += random(0ta 1)
# sum <dict[i])

# n1 = int(input ("enter n for label1: "))

# with open("../../ProcessedData/ImamKhomeini/inpp.txt") as d:
#     all_words = (d.read()).split(' ')
# print("*********************")

# with open("../label1.1gram.gen", "w") as f1:
#     for i in range(n1):
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
# print("\n\n")
# n2 = int(input ("enter n for label2: "))

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

##################################################################################

n1 = int(input ("enter n for label1 Bigram: "))

with open("../../Model/bare_bigram_label1.txt") as d:
    all_words = (d.read()).split('\n')
print("*********************")

with open("../label1.2gram.gen", "w") as f1:
    for i in range(n1):
        input_seed = int(input("enter seed : "))
        print ("Random number with seed %s\n"%input_seed)
        random.seed(input_seed)
        value = ""
        string = ""
        words = ["", ""]
        while(words[1] != '<\s>'):
            random_number = random.randint(0,len(all_words)-1)
            value = all_words[random_number]
            words = value.split(" ")
            string += " " + value

        print(string[1:len(string)])
        f1.write(string[1:len(string)]+"\n")
        print("------------")

print("\n\n")


n2 = int(input ("enter n for label2 Bigram: "))

with open("../../Model/bare_bigram_label2.txt") as d:
    all_words = (d.read()).split('\n')
print("*********************")

with open("../label2.2gram.gen", "w") as f2:
    for i in range(n2):
        input_seed = int(input("enter seed : "))
        print ("Random number with seed %s\n"%input_seed)
        random.seed(input_seed)
        value = ""
        string = ""
        words = ["", ""]
        while(words[1] != '<\s>'):
            random_number = random.randint(0,len(all_words)-1)
            value = all_words[random_number]
            words = value.split(" ")
            string += " " + value

        print(string[1:len(string)])
        f2.write(string[1:len(string)]+"\n")
        print("------------")
