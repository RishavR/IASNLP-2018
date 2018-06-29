## Task 
Annotation of TIMEX3 tags in  15 articles from the Dainik Bhaskar Corpus 

## Details 

Total No. of Sampled Articles:  15

## Explanation 

In all the articles,  there are a **minimum of 1 TIMEX3 Tags** - 

**The Date Published:** 

ie.  Wed, 29 Nov 2017 06:04 PM
```
DATE value="2017-11-29T18:04"
```
[========]

**Article No: 21**

Instance 1:
28 अक्टूबर को तड़के लगभग चार बजे विजयगढ़ (अलीगढ़) के तेल कारोबारी राजकुमार वाष्र्णेय के साथ बदमाशों ने लूटपाट की थी।


```
'चार बजे '
type=TIME value=16:00
```
> Reasoning:  Here चार बजे does not tells us if its 4 in the morning or in the afternoon. So, we take 4 in afternoon as it is the standard time

**Article No: 22**

Instance 1:
इसके अलावा अब हर बुधवार को सीट बेल्ट व हेलमेट दिवस की भी शुरुआत हो चुकी है।


```
'हर बुधवार '
type=SET value=XXXX-W03-07 quant=EVERY
```
> Reasoning:  this is a timer tag for duration.  हर बुधवार denotes 'every wednesday, so we use a quatizer with value 'EVERY'.

**Article No: 24**

Instance 1:
मामले में वर्तमान जिलाधिकारी सुरेंद्र विक्रम ने ज्वाइंट मजिस्ट्रेट, सीएमओ व मुख्य कोषाधिकारी की तीन सदस्यीय जांच टीम गठित कर एक सप्ताह के अंदर अभिलेखीय जांच कर स्पष्ट व तथ्यात्मक रिपोर्ट मांगी थी



```
'वर्तमान '
type=DATE value=2017-11-30
```
> Reasoning: Here वर्तमान means present time. So, we used date tag with value of the published date.

Instance 1:
पूर्व में निलंबित सीएमओ के कार्यकाल का मामला  दवा व सर्जिकल आइटम की खरीद में हुई यह गंभीर वित्तीय अनियमितता यहां तमाम घोटालों व अवैध नियुक्ति आदि के मामले में पिछले वर्ष निलंबित किए गए पूर्व सीएमओ के कार्यकाल का है।



```
'पिछले वर्ष '
type=DATE value=2016-XX-XX
```
> Reasoning: Here पिछले वर्ष denote the last year. So, we used a date tag with date value of last year an we use X for the values we dont know.

