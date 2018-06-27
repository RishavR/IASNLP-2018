## Task 
Annotation of TIMEX3 tags in  15 articles from the Dainik Bhaskar Corpus 

## Details 

Total No. of Sampled Articles:  5 

Total No. of Articles having less than 2 TIMEX3 Tags:  1

Total No. of Articles having more than 2 TIMEX3 Tags:  4

Total No. of (Presumed) Ambiguous instances:  2

## Explanation 

In all the articles,  there are a **minimum of 2 TIMEX3 Tags** - 

**One for the Date Published:** 

ie.  Wed, 29 Nov 2017 06:04 PM
```
DATE value="2017-11-29T18:04"
```
**One for the Date Last Updated:**

ie.  Wed, 29 Nov 2017 20:04 PM
```
DATE value="2017-11-29T20:04"
```

[========]

**Article No: 46**

Instance 1:
'नियमों की उल्लंघना करने वाले वाहन चालकों के खिलाफ छेड़े अभियान के दौरान विभाग ने एक माह में 200 चालान काट कर करीब बीस लाख रुपये का रेवेन्यू पंजाब सरकार के खाते में जमा करवाया है।'

```
' एक माह'
DURATION  value="P1M"
```
> Reasoning:  Here the Abhiyan has been going on for a duration of 1 month.

Instance 2:
' उन्होंने कहा कि पंजाब सरकार ने गुरदासपुर में एटीओ की तैनाती भी की है जो पूरा दिन रोड पर चे¨कग करते है। '

```
' पूरा दिन'
 DURATION value="P1D"
 ```
 >Reasoning:  It says 'pura din road pe check krte h' which means that the event happens for a duration of a whole day
 


[========]

**Article No: 47**

' वे बैंक पहुंचे और पूरे मामले की जानकारी लिए तो पता चला कि 24, 26 व 28 नवंबर को रेलवे टिकट जारी कराने के लिए खाते से 25 हजार का आनलाइन भुगतान कर दिया गया है '

```
'24'
DATE value="2017-11-24"

'26'
DATE value="2017-11-26"

'28 नवंबर'
DATE value="2017-11-28"
```
>Reasoning:  Here 24,26 and 28 refers to 3 discreet dates in November  in the same year when the article has been written. 

>AMBIGUITY:  We have taken 24 and 26 as seperate tags refering to 24th and 26th of November. Is it correct, considering that they do not a explicit relationship to 'November' (unlike the tag '28 November' )
And if it is correct, then rather should we take '28' and 'November' as seperate tags?  


[========]

**Article No: 49**

'  बीते पांच सालों में मासिक आधार पर रुपए का प्रदर्शन '

```
'बीते पांच सालों'
TRANSLATION - 'Past Five Years'
DURATION value="2013-XX-XX"
```
> Reasoning: We consider it as - "In the past 5 years" and hence make a Duration TIMEX3 tag.  Since we don't know the specific date/month since the counting has been started, we assume that the period starts from year 2013 in general.

```
'मासिक'
SET value="P1M" quant="EVERY"
```
> Reasoning: According to [2005 Standard for the Annotation of 
Temporal Expressions](https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-timex2-guidelines-v0.1.pdf) we can reasonably assert that this is a SET whose value is P1M denoting a period of 1 Month with a quant value equivalent to EVERY/ EACH. Basically we set the quant value according to the translation of मासिक as 'Every Month'.

> Ambiguity: Can we consider  बीते पांच सालों में मासिक as a single tag? 

___

