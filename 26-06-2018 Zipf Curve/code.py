#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:48:26 2018

@author: rishav
"""
import nltk as nlp
import re
import matplotlib.pyplot as plt 

paragraph= """ The United States which has long sought Japanese action to stimulate its economy appears to be satisfied Tokyos latest package is a major development and allows leading industrial nations to reaffirm their agreement to stabilize currencies
    
Monetary sources said they believed that US Treasury Secretary James Baker considered Tokyos package announced yesterday to be a major stimulation of the Japanese economy
    
But yesterdays statement by seven leading industrial powers endorses the yens rise from around 153 to the dollar the level at the February 22 Paris Accord to about 145 today
    
The supplementary budget worth about 34 billion dlrs was announced by the ruling Liberal Democratic Party on the eve of Miyazawas departure for Washington to attend yesterdays meetings of leading industrial nations
    
In a strongly worded statement terming the Japanese action extraordinary and urgent the meeting reaffirmed the Paris Accord by noting that current exchange rates are within ranges broadly consistent with fundamentals or economic reality
    
The Group of Seven the United States Japan West Germany France Britain Italy and Canada therefore repeated their willingness to continue close cooperation to foster exchange rate stability
    
The cooperation agreement has resulted in concerted central bank intervention of 8 billion to 9 billion dlrs to halt the dollars fall"""

paragraph= re.sub(r'[^\w]', ' ', paragraph)
tokens=nlp.word_tokenize(paragraph)
types=nlp.Counter(tokens)
print(tokens)
print(types)
X=list(types.keys())
Y=[]
print(X)
for key in X: 
    Y.append(types[key])
print(Y)
plt.figure(figsize=(50,12))
plt.scatter(X,Y)
plt.xlabel("TOKENS")
plt.ylabel("FREQUENCY")
plt.xticks(rotation='vertical')
plt.savefig("ZIFS_plot.png")