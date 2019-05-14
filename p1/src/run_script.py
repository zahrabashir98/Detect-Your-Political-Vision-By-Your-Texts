import os
import sys

code_base_directory = "../../p1"
def run():
    print("Running files")
    os.system('python3 main.py %s'% sys.argv[1]) 
    os.system('python3 datamapping.py')

run()