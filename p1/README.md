# DifferentPhoneticsDetection_NLP
# Introduction 
This project is about finding different forms of reading a sentence.
There were different ways ti implement this such as using recursive function, trees, dynamic programming etc..
##### Here I implemented this by a recursive function which has an efficient run time...
The performance and explanation of my code is ecplained breifly below(also in comments of my code)
At first I assemble the phonetic of whole sentence together and then I try to find all the possible subtrings.
I seperate a substring and check wether it is in my dictionary or not and also I have to check recursively wether the remaining parts may make meaning ful words or not...

I have put my codes in p1/src . My main files are `main.py` and `datamapping.py` and I have also a script to run them named `run_script.py` which will be explained later .

In p1/out I have my outout files which contains `phonetics_states.txt` and `final_answer.txt`.
Actually the final output is in`final_answer.txt`.
It also contains `test_results` folder which is my output to those 5 determined test cases.

In p1/in I have the `Entries.csv` which is a comma seperated data set and also some input files for test.


# Dependencies
All you need is python3 :))
##### Notice the version should be only 3!
(because of the differnces between python 2 and python3 in ASCII codes)

# Getting Started
Here is how you can run my project:
``` 
python run_script_py textfilename
```

###### No need to add format (.txt etc)
If you have problem with the script(actually there might be any) you can run the files seperately also 
Then you only need to do this:
``` 
python main.py textfilename
python datamapping.py
```
# Test
The only thing you have to notic is that you should put you test data in tests folder because of the structure of my script.
#### Thanks For Your Attention
