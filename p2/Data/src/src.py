import glob
import os
from shutil import copyfile

list_of_files = glob.glob("../../RawData/*.txt")
counter1 = 1
counter2 = 1

for name in list_of_files:
    print(name)
    if "shah" in name:
        copyfile(name, "../MohammadRezaPahlavi/%s.txt"%counter1)
        counter1 += 1

    if "Imam" in name:
        copyfile(name, "../ImamKhomeini/%s.txt"%counter2)
        counter2 += 1
