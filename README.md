# ROC_and_AUC
For plotting normal PDF curve, ROC curve and calculating AUC values
## INTRODUCTION

The file (code.py) contains code for calculating Normal distribution and its curve along wth ROC curve and respective AUC values.
## REQUIREMENTS

This code requires the following modules:
* [python 3](https://www.python.org/download/releases/3.0/)
* [numpy](http://www.numpy.org)
* [mathplotlib.pyplot](https://matplotlib.org/)

## FUNCTIONS

For normal distribution (it will return PDF values)
```
ndis(<standered deviation>, <mean>)
```
Plotting and comaparing two normal distribution
```
drawPlot(<PDF(Malignant)>,<PDF(Benign)>, <name of comapny>)
```
For AUC
```
auc(<PDF(Malignant)>,<PDF(Benign)>, <name of comapny>)
```
For ROC curve
```
draw_roc(<TPR>,<FPR>, <name of comapny>)
```

## EXECUITNG CODE

Configruation:
* p1y = ndis(standered deviation, mean)
* p2y = ndis(standered deviation, mean)
```
Run as you would normally run a python 3 file.
```

## Authors

* **Akash Meshram** - *Initial work* - [Akash_Meshram](https://github.com/akashmeshram)

