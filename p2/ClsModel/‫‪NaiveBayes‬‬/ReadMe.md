
# ClsModel/Naive Bayes

## Naive Bayes

### Bag Of Words Effect

One of the wrong and bad defaults in **Naive Bayes** is that we assume that words are independent and their order doesn't matter.
So we treat them as a "Bag of Words" and this is one of the problems
I reached these results about the `TestCase`:

**C1 results:**
{'a2 a3 b2 a4': -4.425968732272281,
'e3 b1 d2 e4': -5.755027451536506,
'b2 b1 a3 a4 d1': -5.851937464544562,
'a2 d3 e4 d2 b1': -6.453997455872525,
'd5 e4 e2 a1 a3 d2': -8.357087442864469}

**C2 Results:**
{'a2 a3 b2 a4': -5.548045439886998,
'e3 b1 d2 e4': -4.672984176495298,
'b2 b1 a3 a4 d1': -6.859799300942752,
'a2 d3 e4 d2 b1': -5.887828024542996,
'd5 e4 e2 a1 a3 d2': -7.898551889934769}

And then we get the maximum of each category as our final answer which is :
c1 -4.425968732272281 c2 -5.548045439886998
c1 -5.755027451536506 c2 -4.672984176495298
c1 -5.851937464544562 c2 -6.859799300942752
c1 -6.453997455872525 c2 -5.887828024542996
c1 -8.357087442864469 c2 -7.898551889934769

real_labels = ['c1', 'c2', 'c1', 'c2', 'c1']
estimated_label = ['c1', 'c2', 'c1', 'c2', 'c2']

The mistake is in `d5 e4 e2 a1 a3 d2` data that it should be c1 but estimated as c2:
C1 : p(d5)  * p(e4) * p(e2)* p(a1) * p(a2) *p(a3)  * p(d2) * p(c1)

C2 :p(d5)  * p(e4) * p(e2)* p(a1) * p(a2) *p(a3)  * p(d2)* p(c2)


### Example of one sentence estimated wrong in naive bayes:

> امام اﺻﻼﺣﺎت ارﺿﯽ آﻗﺎ ﺑﻪ اﯾﻨﺠﺎ ﻣﻨﺘﻬﯽ ﺷﺪ ﮐﻪ ﯾﮏ ﺑﺎزاري درﺳﺖ ﮐﺮد ﺑﺮاي
> آﻣﺮﯾﮑﺎ ﮐﻪ آﻣﺮﯾﮑﺎ ﭼﯿﺰﻫﺎﯾﯽ ﮐﻪ ﺑﺎﯾﺪ ﺑﺮﯾﺰد دور ﺑﻪ اﯾﺮان ﺑﻔﺮوﺷﺪ ﻧﻔﺖ ﻣﺎ را
> ﮐﻪ دارﻧﺪ اﯾﻦ ﻃﻮر ﻣﯽ ﺑﺮﻧﺪ ﺑﻌﺪ از ﺳﯽ ﺳﺎل دﯾﮕﺮ )ﺑﻪ ﻗﻮل ﺷﺎه( ﺑﻌﺪ از ﺳﯽ ﺳﺎل
> دﯾﮕﺮ ﺗﻤﺎم ﻣﯽ ﺷﻮد ﻧﻔﺖ ﻧﻪ اﯾﻨﮑﻪ ﻧﻔﺖ ﺗﻤﺎم ﻣﯽ ﺷﻮد ﻧﺨﯿﺮ ﺗﻤﺎم دارﻧﺪ ﻣﯽ ﮐﻨﻨﺪ
> دارﻧﺪ ﺑﺎ اﯾﻦ ﻟﻮﻟﻪ ﻫﺎي ﺑﺰرگ ﮐﻪ ﺑﻪ اﻧﺪازه اﯾﻦ اﻃﺎق ﺷﺎﯾﺪ ﺑﻌﻀﯽ ﻫﺎﯾﺸﺎن
> ﺑﺰرﮔﯽ اش ﺑﺎﺷﺪ ﺑﻪ اﻧﺪازه ﻗﺎﻣﺖ اﻧﺴﺎن زﯾﺎدﺗﺮ ﺑﻠﻨﺪﯾﺶ دورش ﻫﺴﺖ ﻫﯿﮑﻠﺶ ﻫﺴﺖ
> دارﻧﺪ ﺑﺎ زور ﻧﻔﺖ ﻫﺎي ﻣﺎ را در ﻣﯽ آورﻧﺪ و ﻣﯽ ﻓﺮﺳﺘﻨﺪ ﻃﺮف اﻣﺮﯾﮑﺎ ﻋﻮﺿﺶ ﻫﻢ
> ﮐﻪ ﺑﺎﯾﺪ ﺑﻪ ﻣﺎ ﺑﺪﻫﻨﺪ ﻋﻮﺿﺶ ﻫﻢ اﺳﻠﺤﻪ اي را ﮐﻪ ﻣﯽ ﺧﻮاﻫﺪ اﻣﺮﯾﮑﺎ ﺑﯿﺎﯾﺪ در
> اﯾﺮان ﭘﺎﯾﮕﺎه داﺷﺘﻪ ﺑﺎﺷﺪ در ﻣﻘﺎﺑﻞ ﺷﻮروي ﺑﺎﯾﺪ ﯾﮏ ﭼﯿﺰي ﻫﻢ ﺑﻪ اﯾﺮان ﺑﺪﻫﺪ
> اﮔﺮ ﭼﻨﺎﻧﭽﻪ اﺟﺎزه اش  ﻧﺒﺎﯾﺪ اﺟﺎزه ﺑﺪﻫﻨﺪ ﻟﮑﻦ ﺣﺎﻻ اﯾﻦ ﺧﯿﺎﻧﺖ را ﮐﺮدﻧﺪ و
> ﺧﻮاﺳﺘﻨﺪ اﺟﺎزه ﺑﺪﻫﻨﺪ ﺑﺎﯾﺪ ﯾﮏ ﭼﯿﺰي ﻫﻢ ﺑﺪﻫﺪ ﺑﻪ ﻣﺎ ﮐﻪ ﺑﯿﺎﯾﺪ ﭘﺎﯾﮕﺎه درﺳﺖ
> ﺑﮑﻨﺪ ﻧﻔﺖ ﻣﺎ را ﻣﯽ ﮔﯿﺮد ﭘﺎﯾﮕﺎه درﺳﺖ ﻣﯽ ﮐﻨﺪ ﺑﺮاي ﺧﻮدش ﻋﻮض ﺑﻪ ﻣﺎ ﻣﯽ دﻫﺪ
> ﻋﻮض ﯾﻌﻨﯽ ﭘﺎﯾﮕﺎه درﺳﺖ ﮐﺮدن ﺑﺮاي آﻣﺮﯾﮑﺎ ﯾﺎ آن اﺳﻠﺤﻪ ﻫﺎي ﺑﺰرگ ﺣﺘﯽ از
> ﻣﻤﺎﻟﮏ دﯾﮕﺮ ﻓﺮاﻧﺴﻪ ﻣﯽ ﺧﺮﻧﺪ آن ﭼﯿﺰﻫﺎي ﺑﺴﯿﺎر ﮔﺮان ﻗﯿﻤﺖ را ﮐﻪ ﺑﻪ درد ﻣﺎ
> ﻧﻤﯽ ﺧﻮرد ﺑﻪ ﻋﻮﺿﺶ ﻧﻔﺖ را دارﻧﺪ ﻣﯽ ﺑﺮﻧﺪ ﻃﯿﺎره ﻫﺎي 350 ﻣﯿﻠﯿﻮن دﻻري 350
> ﻣﯿﻠﯿﻮن

Here our classifier detected this as `شاه` which is actually ‍‍`امام`.
The reason is because of Naive Bayes pays attention to `bag-of-words `and the `order` and `sequence` of words is not important to it.
And most of the times Shah talked about financial stuffs so it learned that each of these words are more probable in `شاه‍‍` rather than `امام`.
But we should notice that we need a model which can recognize a group of words and it should be like a sequence and not only a unigram but more than that.

