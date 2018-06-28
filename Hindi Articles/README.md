## Task 
Annotation of TIMEX3 tags in  15 articles from the Dainik Bhaskar Corpus 

## Details 

Total No. of Sampled Articles:  10 

Total No. of Articles having less than 1 TIMEX3 Tags:  4

Total No. of Articles having more than 2 TIMEX3 Tags:  6

## Explanation 

In all the articles,  there are a **minimum of 2 TIMEX3 Tags** - 

**One for the Date Published:** 

ie.  Wed, 29 Nov 2017 06:04 PM
```
DATE value="2017-11-29T18:04"
```
[========]

**Article No: 4**

Instance 1:
अब विधायक के ही वार्ड में ऐसा मामला सामने आया है

```
' अब '
DATE  value="PRESENT_REF"
```
> Reasoning:  Here we assume the reference time is Dec 03, 2017 So, the present time is interpreted as of Dec 03, 2017.

Instance 2 :
यहां नगर निगम ने कुछ माह पहले ही करीब 50 लाख रुपये की लागत से सड़क के दोनों और इंटरलॉ¨कग टाइल्स का काम करवाया था।

```
' कुछ माह '
no need to tag
```
> Reasoning:  Here It say "Kuch maah" which means some months or few months and we can't identify the duration of few months.

[========]

**Article No: 5**

स्थानीय थाना क्षेत्र के गांव ¨सगलामऊ निवासी शिवराज ¨सह पुत्र जयराम ¨सह  गत रात को  ग्राम धर्मपुर में राजेंद्र पुत्र मोतीलाल की बेटी की शादी में शामिल होने गए थे।

```
गत रात को
type="DATE"  value="2017-12-02TNI"
```
>Reasoning:  Here 'gatt raat ko' which means late night or may be last night so, the present day is interpretted as one day before. 

तभी थोड़ी देर में गांव के सुभाष ने आकर शिवराज ¨सह को बताया

```
'  थोड़ी देर में '
 DURATION  value="PXM"
 ```
 >Reasoning:  It say 'thori der mai' which means that the event happens for a duration for some minutes.
 
[========]

**Article No: 7**

अफरोज की शादी करीब आठ साल पहले पूर्वा फैय्याज अली निवासी जामू के साथ हुई थी।
```
 'आठ साल पहले'
DURATION  value="P8Y"
```
> Reasoning: Here It says "aath saal pahle" which means eight years ago so the event happens for duartion of eight years.

 आरोप है कि जामू शनिवार रात अफरोज के पास पहुंचा और पैसे मांगने लगा।
```
'शनिवार रात'
TIME  value="2017-12-02TNI"
```
> Reasoning: Here It says saturday night which means it denotes to time So, we are assuming that we know that the document creation time is Saturday, Dec 02, 2017.

[========]

**Article No: 8**

चार बदमाश शनिवार तड़के तीन बजे घटना को अंजाम दे रहे हैं
```
 'शनिवार'
DATE  value="2017-12-02"
```
```
 ' तीन बजे '
TIME  value="T03:00"
```
[========]

**Article No: 9**

 एक दिसंबर से नान सब्सिडी घरेलू गैस सिलेंडर की कीमत 803.50 रुपये हो गई है।
```
 'एक दिसंबर'
DATE  value="XXXX-12-01"
```
>Reasoning : Unless we know the year to which the text is anchoring the current temporal expression, the value attribute will leave the year underspecified by means of placeholders: XXXX.

तीस नवंबर की रात 12 बजे एक बार फिर इसकी कीमतों में इजाफा किया गया।
```
 'रात 12 बजे'
TIME  value="T24:00"
```
>Reasoning : Here It says 'raat ko 12 baje' which means 12 o'clock midnight.

हर महीने कम हो रही सब्सिडी घरेलू रसोई गैस सिलेंडरों की कीमतों में लगातार इजाफा होता जा रहा है।
```
 'हर महीने'
SET  value="P1M"  quant="EVERY"
```
यानी सिलेंडर की कीमत अब 496 रुपये हो चुकी है।
```
 'अब '
DATE  value="PRESENT_REF"  ANCHOR_VALUE="2017-12-03"
```
>Reasoning : For PRESENT_REF expressions, it is usually possible to give the general timeframe under which "present" should be interpreted. To do so, the tag is given an ANCHOR_VAL with the utterance's reference time. we assume the reference time is "2017-12-03".

 सितंबर में नान सब्सिडी सिलेंडर की कीमत 655.50 रुपये हो गई।
 ```
 'सितंबर '
DATE  value="2017-09"
```
[========]

**Article No: 10**

 पीड़ितों ने शनिवार को जेवर कोतवाली में चार लोगों के खिलाफ लूटपाट व मारपीट का मामला दर्ज कराया है।
```
 'शनिवार'
DATE  value="2017-WXX-6"
```
Reasoning : Here, ISO allows for a day of the week to be specified in the week-based format, e.g."2017-WXX-6" for Saturday of any week in 2017, where Monday is day 1 and thus Saturday is day 6.
So, "Prefer Month-Based to Week-Based Format" Rule.
