#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:48:26 2018

@author: rishav
"""
import nltk as nlp
import re
import matplotlib.pyplot as plt 
#open the plaintext file  
file=open("The_Gift_of_The_Magi.txt")
# Read the file into a string type variable called 'text'
text=file.read()
#Using Regex (Regular Expressions) remove all the special characters in the text.
#This is done by selecting all special characters and substituting them with a space character.  
text= re.sub(r'[^\w]', ' ', text)
# Tokenize the text and store it in a list called tokens 
tokens=nlp.word_tokenize(text)
# Using the Counter function, obtatin the frequency of each token and store it as a 'key - value' 
# Pair in a dictionary called types 
types=nlp.Counter(tokens)
# For Debugging purposes 
print(tokens)
print(types)
# Extract all the 'keys' from the dictionary types and store it as a list in X
X=list(types.keys())
# Declare an empty list Y
Y=[]
#For Debugging purposes
print(X)
# For each item of key in X, find the corresponding value in the dictionary types and store it in list Y
for key in X: 
    Y.append(types[key])
# For Debugging purposes
print(Y)

############ PLOTTING THE GRAPH ##############

#Here we change the figure size to accomodate our huge X axis of Tokens
plt.figure(figsize=(200,12))
# Perform scatter plotting
plt.scatter(X,Y)
# Label on X axis named as Tokens
plt.xlabel("TOKENS")
# Label on Y axis named as Frequency
plt.ylabel("FREQUENCY")
# Changing the orientation of X axis labels (Ticks from now on) to vertical orientation
plt.xticks(rotation='vertical')
#Saving the figure in the PWD (present working directory)
plt.savefig("ZIFS_plot.png")

########### THE END ############# 