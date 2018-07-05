"""
created by kunal on 03-07-2018@15:53
modified by rishav on 04-07-2018@11:52

MODIFICATIONS MADE: 
    1. Improved formatting of output text with tabs 
    2. Cleaned up special character deletion process using regex 
    3. Added some code to consider all files in the folder and generate subsequent output text
    4. Fixed bug of missing the ending daari for each document and putting a space after each daari 
"""
import xml.etree.ElementTree as ET
import re 

#log=""
#Set Defaults
file=open("festivals.txt",'r')
text=file.read()
file.close()
festivals=text.split(".")
file=open("daysOfWeek.txt",'r')
text=file.read()
file.close()
days=text.split()
file=open("monthOfYear.txt",'r')
text=file.read()
file.close()
months=text.split()

# Additional pivot tokens manually annotated from the text document
# Tweak this and include more tokens if CRF++ gives erroneous values.
file=open("timeLogs.txt",'r')
text=file.read()
file.close()
tempList=text.split()
pivotTokens=[x[1:len(x)-1] for x in tempList if x[0] == '\'']

def dateChecker(token):
    #print(token)
    match1=re.findall(r'([0-9]|[०१२३४५६७८९१०])+',token)
    match2=re.findall(r'(-|:|\.|,)+',token)
    if len(match1) > 0 and len(match2) > 0:
        return True
    else:
        return False
    return False
   
def isPivot(token):
    match= token in festivals or token in days or token in months or token in pivotTokens or dateChecker(token)
    return match

def containsDigitandChar(token):
    #print(token)
    match1=re.findall(r'([0-9]|[०१२३४५६७८९१०])+',token)
    match2=re.findall(r'(-|:|\.|,)+',token)
    if len(match1) > 0 or len(match2) > 0:
        return True
    else:
        return False
    return False

for indexval in range(1,301):
    #parses xml file
    str_index=str(indexval)
    print("Processed File:"+str_index)
    tree = ET.parse('C-'+str_index+'.xml')
    root = tree.getroot()



    #append start and end of temporal expressions with quantity of "Value" attribute
    for timeExpression in root.findall("./TEXT/ILTIMEX"):
        #log+=timeExpression.text+"\n"
        timeExpression.text = list(timeExpression.attrib.values())[0] + " "+ timeExpression.text + " "+ list(timeExpression.attrib.values())[0]
        #print(timeExpression.text)


    str_text = ET.tostring(root, encoding='utf8', method='text').decode('utf8')
    #str2=str
    # Removes ALL special characters except those which can be required to get true returns for containsDigitandChar
    # Tweak this if CRF++ is giving erroneous values. 
    str_text= re.sub(r'(\(|\)|~|`|;|\'|\"|\?|\+|\{|\}|\[|\]|\/|\\|!|@|#|$|%|\^|&|\*)','', str_text)
    #takes care of the case of double daari or "।।" 
    str_text= re.sub(r'।।','।', str_text)
    # Splits by daari 
    str2_list=re.split('(।)',str_text)
    mod_list=[]
    for sentence in str2_list:
        mod_list.extend(sentence.split(" "))
    str_list = str_text.split()
    check_list=str_list[:]

    # Logical Code of creating the output file 
    flag = 0
    t_flag = ''
    txt = ""
    for token in mod_list:
        if token == "P" or token=="D" or token == "F":
            t_flag = token
            if flag == 0:
                flag = 1
            elif flag == -1:
                flag = 0;
            continue
        
        if flag==0:
            labelPivot="NaN"
            labelDAC = "NaN"
        # takes care of the condtition of marking ' ' (blank space) as O 
            if token == '':
                txt += token + "\t " + "\t" + '\n'  
            else:
                txt += token + "\tO " + "\t" + labelPivot + "\t" + labelDAC + '\n' 
        if flag==-1:
            val = isPivot(token)
            if val == True: 
                labelPivot="PIV"
            else:
                labelPivot="NaN"
            dac=containsDigitandChar(token)
            if dac == True: 
                labelDAC="DAC"
                #print(token)
            else:
                labelDAC="NaN"
            txt += token + "\tI-" + t_flag + "\t" + labelPivot + "\t" + labelDAC + '\n'   
        if flag==1:
            val = isPivot(token)
            if val == True: 
                labelPivot="PIV"
            else:
                labelPivot="NaN"
            dac=containsDigitandChar(token)
            if dac == True: 
                labelDAC="DAC"
                #print(token)
            else:
                labelDAC="NaN"
            txt += token + "\tB-" + t_flag + "\t" + labelPivot + "\t" + labelDAC + '\n'  
            flag = -1
    

    str_index2="output"
    #export 
    f = open("../BIO_TaggedM/C-"+str_index+".txt", 'w+')
    f.write(txt)
    f.close()