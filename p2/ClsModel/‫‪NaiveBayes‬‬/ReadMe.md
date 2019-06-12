# ClsModel

## Naive Bayes
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

