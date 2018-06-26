## Assignment

1.  Go on [Gutenberg.org](http://gutenberg.org)
2. Take any free ebook
3. Tokenize the text 
4. Plot Zipf Curve 
5. Make a langugage model (Tri or Quad) **[Pending]**

## Solution 
The solution code as been uploaded. 

A Few Things about it: 

##### Dependencies 

```
import nltk as nlp
import re
import matplotlib.pyplot as plt 
```
##### Corpus Used

So I've used the plaintext version of **The Gift of the Magi**  essentially because of two reasons: 

```
1. I like Gift of The Magi 
2. It is a short story.  

 **Reason being** - Gutenberg throws in a lot of stuff in their plaintext paragraphs like usage clause, transcription credits etc. 
So you need to filter the text first and remove additional stuff like 'Chapter Number', 'Episode Number', 'Dialogue Speaker' etc. etc. to avoid getting unwanted readings. 
``` 

You can try with other texts. Be sure to change the figure_size so that the plot can adjust to the increase/decrease in number of types. 

### Results 

![](https://raw.githubusercontent.com/RishavR/IASNLP-2018/master/26-06-2018%20Zipf%20Curve/ZIFS_plot.png)

### Resources

[1] http://gutenberg.org
