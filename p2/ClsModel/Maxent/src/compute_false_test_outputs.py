with open("../output.test.txt") as file1:
    output_string = file1.read().split("\n")

with open("../‫‪input.test.txt‬‬") as file2:
    input_string = file2.read().split("\n")

est_classes = []
counter = 0
for row in output_string:
    m = row.split("\t")
    if len(m) > 2:
        if float(m[2]) > float(m[4]):
            est_classes.append(m[1])

        elif float(m[2]) < float(m[4]):
            est_classes.append(m[3])


true_classes = []
# print(est_classes)
for row in input_string:
    m = row.split(" ")
    true_classes.append(m[0])

with open("../wrong_estimated.txt","w") as wrong:
    for i in range(len(est_classes)):
        if i > 114:
            break
        if true_classes[i] != est_classes[i]:
            print(i)
            print(true_classes[i])
            print(est_classes[i])
            print("*************")
            wrong.write(str(i)+"\n"+true_classes[i] +"\n" + est_classes[i]+ "\n"+"***********"+"\n")  
wrong.close()