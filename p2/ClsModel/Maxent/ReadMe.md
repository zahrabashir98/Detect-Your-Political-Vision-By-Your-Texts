
# ClsModel/Maxent

**The structure of folders is shown below:**
* /src
* * /after_optimization
* /before_optimization
* model.bin
* Test.errors.txt
* Test.output.txt
* Test.report.txt
* ReadMe.md
* wrong_predicted.txt

I think the files are clear as are told in the document.
In src I have a python code which reads the outputs and reports which are predicted true and which are false . which its out put is `wrong_predicted.txt` that shows the index (number of ilne) of data which are not predicted correctly.

I only added `before_optimization` and `after_optimization` folders which contain all data and models (input and output) of two steps of making model better

Actually the better results are put as main results in my homework.

Wong predicted example:
We can refer to `wong_predicted.txt` and see the wrong ilnes and check them from input.For example the following sentence is predicted `امام` but it is `شاه`.

> شاه  ولت:1 نیز:1 وظیفه:1 دارد:1 که:1 برای:1 حل:1 مشکلات:1 استخدامی:1
> و:1 تجدیدنظر:1 در:1 سازمان‌های:1 دولتی:1 اقدام:1 لازم:1 بنماید:1
> length:17 has_arabic:0 ولتنیز:1 نیزوظیفه:1 وظیفهدارد:1 داردکه:1
> کهبرای:1 برایحل:1 حلمشکلات:1 مشکلاتاستخدامی:1 استخدامیو:1 وتجدیدنظر:1
> تجدیدنظردر:1 درسازمان‌های:1 سازمان‌هایدولتی:1 دولتیاقدام:1 اقداملازم:1
> لازمبنماید:1

As we can see in `Test.output.txt`:

	array:20	امام	0.6097463457307801	شاه 	0.39025361142903714

The reason may be some similar features because as you can see here the probabilities are near(60, 40) and A human can also make mistake in these sentences.

