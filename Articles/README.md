# Annotation Review

Review of the annotated Hindi news articles


### Total files annotated: 15
#### Total unsure cases: 5

**1. new_file_31**   
Annotations: 6, Unsure: 1

```
Thu, 30 Nov 2017 02:40 PM   
Type:Time, value="2017-11-30T14:40"
```

REASONING: Time of publishing.
```
Thu, 30 Nov 2017 02:40 PM   
Type:Time, value="2017-11-30T14:40"
```

REASONING:  Time of updation.
```
तीन घंटे पहले   
Type:Time value="2017-11-30T11:40"
```

REASONING:  It refers to events 3 hours prior to the writing of the article.
```
दोपहर 2:15   
Type:Time, value="2017-11-30T14:15"
```

REASONING: Refers to present days time.

```
कुछ देर पहले  
```
**UNSURE**: No specific time mentioned.

```
बुधवार   
Type:Date, value="2017-11-29"
```

REASONING: Refers to the Wednesday of that week which is the day before.

AMBIGUITY: The Wednesday could be from last week or before as there is no explicit mention.However as it is a news article, it is safe to assume that it refers to the most recent day.

**2.new_file_32**   
Annotations: 2

```
Wed, 29 Nov 2017 03:35 PM   
Type:Time, value="2017-11-29T15:35"
```

REASONING: Time of publishing.
```
Thu, 30 Nov 2017 10:54 AM  
Type:Time, value="2017-11-30T10:54"
```

REASONING:  Time of updation.

**3.new_file_33**        
Annotations: 10


```
सौ साल  
Type:Duration, value="P100Y"
```
REASONING: Period of 100 years  

```
गुरुवार   
Type:Date, value="2017-11-30"
```

REASONING: Refers to current day.

```
30 नवंबर, 1917   
Type:Date, value="1917-11-30"
```
```
1926   
Type:Date value"1926"
```
```
1940   
Type:Date value"1940"
```

```
1994   
Type:Date value"1994"
```
```
>2015   
Type:Date value"2015"
```
```
1995   
Type:Date value"1995"
```

```
2015   
Type:Date value"2015"
```

REASONING: Specific date.

**4.new_file_34**    
Annotations: 3


```
पिछले साल   
Type:Date value="2016"
```
REASONING: Refers to last year.


**5.new_file_35**    
Annotations: 3


```
बुधवार   
Type:Date, value="2017-11-29"
```
REASONING: Refers to Wednesday, which is the day before the article was written.

AMBIGUITY: The Wednesday could be from last week or before as there is no explicit mention. However as it is a news article, it is safe to assume that it refers to the most recent day.

```
देर शाम तक
value="2017-11-29TEV"
```
REASONING: Refers to evening of the previous day, mentioned before in the article.


**6.new_file_36**  
Annotations: 6, Unsure: 2

```
मंगलवार की शाम
value="2017-11-28TEV"
```
REASONING: Refers to most recent Tuesday.

```
शाम
value="2017-11-28TEV"
```
REASONING: Refers to the evening of the same day mentioned in the article.

```
उस समय
value="2017-11-28TEV"
```
REASONING: Refers to the same time as mentioned in the previous sentence article.

**UNSURE**/AMBIGUITY: Not explicit regarding time.

```
रात के समय
value="2017-11-28TNI"
```
REASONING: Refers to the night of the "same day" mentioned in the article.

**UNSURE**/AMBIGUITY: The article could also be referring to the next day's night.(Wednesday)

**7.new_file_37**  
Annotations: 4


```
बुधवार
Type:Date,value="2017-11-29"
```
REASONING: Previous day

```
2012
Type:Date, value="2012"
```
REASONING: Date

**8.new_file_38** 
Annotations: 3



```
मंगलवार को सुबह करीब दस बजे
Type: Time, value="2017-11-28T10:00"
```
R: Morning of the recent Tuesday.

AMBIGUITY: It says around 10:00 instead of explicit 10.

**9.new_file_39** 
Annotations: 3


```
20 नवंबर
Type: Date, value="2017-11-20'
```
R: Date
AMBIGUITY: Year is not mentioned, but current year is assumed in context.

**10.new_file_40**  
Annotations: 4



```
बुधवार
Type:Date, value="2017-11-29"
```
R: Refers to the day before

```
बुधवार
Type:Date, value="2017-11-29"
```
R: Refers to the day before

**11.new_file_41**  
Annotations: 5, Unsure:2



```
वार्षिक
Type:Range, value="P1Y", frequency="1X"
```
R: Annual (refers to interest rate). 

**UNSURE**: May not pertain to task. Does not refer to any event.
```
जनवरी
Type:Date, value="2018-01-XX"
```
R: Month

A: While year is not mentioned, it is assumed to be the earliest possible January.

```
तीन माह
Type:Duration, value="P3M"
```
R: Duration

A: Dates arent specified, however it can be assumed to be from January.

```
अब तक
```
**UNSURE**: No specific time. Might mean till today.

**12.new_file_42**  
Annotations: 4

```
दो दिन
Type:Duration,value="P2D"
```
R: Duration

A: No exact dates given. Article says "last 2 days"

```
27 नवंबर
Typr:Date, value="2017-11-27"
```
R: Date

**13.new_file_43**  
Annotations: 2


**14.new_file_44**  
Annotations: 8

```
2015
Type:Date, value="2015"
```
```
2015
Type:Date, value="2015"
```
```
2016
Type:Date, value="2016"
```
```
2015
Type:Date, value="2015"
```
```
2015
Type:Date, value="2015"
```
R: Dates

```
6 महीने
Type:Duration, value="P6M"
```
R: Refers to a duration

A: No specific time period is mentioned nor can any be inferred from the article

**15.new_file_45**  
Annotations: 4

```
बुधवार
Type:Date, value="2017-11-29"
```
R: Day. Date can be inferred from article.

```
बुधवार सुबह
Type:Time, value="2017-11-29TMO"
```
R:Refers to morning of day mentioned before in article
