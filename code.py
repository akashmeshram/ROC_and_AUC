# -*- coding: utf-8 -*-
"""
@author: Akash Meshram 

"""
#import files for various opertions
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz

# Array for frequency
x = np.linspace(15, 50, 1000)

# Normal Distribution
def ndis(std, mean):
    c = 1.0 / np.sqrt(2*np.pi*(std**2))
    y = c*np.exp(-((x-mean)**2)/(2.0*(std**2)))
    return y

# Plot for probablity distribution
def drawPlot(y1, y2, name):
    fig, ax = plt.subplots()
    ax.set_title(name, fontsize=14)
    ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.5)
    ax.set_ylabel('value', fontsize=12)
    ax.set_xlabel('Test results', fontsize=12)
    ax.plot(x, y1, c='b', alpha=0.8)
    ax.plot(x, y2, c='r', alpha=0.8)
    ax.legend(["Positive","Negetive"])

# For calculation of TPR and FPR and AUC
def auc(y1, y2, name):
    tpr = [None for _ in range(len(x))]
    fpr = [None for _ in range(len(x))]
    b = np.sum(p1y)
    c = np.sum(p2y)
    for i in range(len(x)):
        a1 = np.sum(y1[i:])
        a2 = np.sum(y2[i:])
        tpr[i] = a1/b 
        fpr[i] = a2/c
    draw_roc(tpr, fpr, name)
    area = trapz(tpr, dx=len(fpr)/len(x))
    print('AUC  { ' + name + "} : " + str(area))
    return area

# For plotting ROC curve
def draw_roc(tp,fp, name):
    fig, ax = plt.subplots()
    ax.set_title(name, fontsize=14)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.plot((x-15)/35,(x-15)/35, '--')
    ax.set_ylabel('TPR', fontsize=12)
    ax.set_xlabel('FPR', fontsize=12)
    ax.plot(fp, tp, c='g', alpha=0.8)


## Entering standered deviation and Mean values ##

# company's Data
p1y = ndis(1, 37)
p2y = ndis(4, 32)


## Calculation and plotting ##
drawPlot(p1y, p2y, 'Company')
ar = auc(p1y, p2y, 'Company')


    