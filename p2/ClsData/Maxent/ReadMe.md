# ClsData

The structure of folders is shown below:
* src
* Maxent
* train.txt
* test.txt
* ReadMe.md

These two `train.txt` and `test.txt` files are labeled data with correct formats as told in the doc.
Theire related code is in src (for removing the stopwords and distributing like 80/20 as train and test data )

And In the **Maxent** folder I have the following files:
* src
* ‫‪input.train.txt‬‬
* ‫‪input.test.txt‬‬
* input_2.train.txt
* input_2.test.txt
* ‫‪features.train.bin‬‬
* ‫‪features.test.bin‬‬
* ReadMe.md

In `src` I have the code which I prepare my input data there
I generate features and make a suitable input for mallet 
The results of this `src` are `‫input.train.txt‬‬` and `‫input.test.txt‬‬`.
I also have `input_2.train.txt` and `input_2.test.txt` here.
They are my inputs after optimization and adding some new features.

Then I run the following Mallet command And I will have `features.train.bin‬‬` and `features.test.bin‬‬` as output.

    ‫‪bin/mallet‬‬ ‫‪import-svmlight‬‬ --input "input address" --output "output address"


