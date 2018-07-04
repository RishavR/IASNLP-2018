"""
created by kunal on 03-07-2018@15:53
modified by rishav on 04-07-2018@11:52

MODIFICATIONS MADE: 
    1. Improved formatting of output text with tabs 
    2. Cleaned up special character deletion process using regex 
    3. Added some code to consider all files in the folder and generate subsequent output text 
"""
import xml.etree.ElementTree as ET
import re 

for indexval in range(1,301):
    #parses xml file
    str_index=str(indexval)
    print("Processed File:"+str_index)
    tree = ET.parse('C-'+str_index+'.xml')
    root = tree.getroot()



    #append start and end of temporal expressions with quantity of "Value" attribute
    for timeExpression in root.findall("./TEXT/ILTIMEX"):
    #print(timeExpression.text)
        timeExpression.text = list(timeExpression.attrib.values())[0] + " "+ timeExpression.text + " "+ list(timeExpression.attrib.values())[0]
        #print(timeExpression.text)


    str_text = ET.tostring(root, encoding='utf8', method='text').decode('utf8')
    #str2=str
    # Experimental Split by Daari & Space using regex split  
    #str2_list=re.split('\s|(।)',str2)
    #print(str2_list)
    str_text= re.sub(r'(,|\(|\)|~|`|-|\.|;|:|\'|\"|\?|\+|\{|\}|\[|\]|\/|\\|!|@|#|$|%|\^|&|\*)', ' ', str_text)
    str_list = str_text.split()
    check_list=str_list[:]
    #Split । (period in Hindi) from word
    # REPLACE WITH REGEX 
    y = '।'
    for i in range(len(str_list)):
        if(str_list[i].find(y)!=-1 and len(str_list[i])>1):
            str_list[i]=str_list[i][:str_list[i].find(y)]
            str_list.insert(i+1,y)

    print(str_list)
    flag = 0
    t_flag = ''
    txt = ""
    for token in str_list:
        if token == "P" or token=="D" or token == "F":
            t_flag = token
            if flag == 0:
                flag = 1
            elif flag == -1:
                flag = 0;
            continue
        
        if flag==0:
            txt += token + "\tO " + '\n'
        if flag==-1:
            txt += token + "\tI-" + t_flag +  '\n'    
        if flag==1:
            txt += token + "\tB-" + t_flag + ' \n'
            flag = -1
    


    #export 
    f = open("../BIO_Tagged/C-"+str_index+".txt", 'w+')
    f.write(txt)
    f.close()