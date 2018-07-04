#python3

"""
created by kunal on 04-07-2018@17:11

Appends POS tags to data.
Format of data should be - [Hindi Word]\t[Feature]\t[Feature]...\n

POS tag will be appended to end of the word.

hindi-pos-tagger folder renamed as pos should be in same directory as this script along with Plain_Text and BIO_TaggedM Folders. 
"""

import xml.etree.ElementTree as ET
import os

for indexval in range(1,301):
    #parses xml file
    str_index=str(indexval)
    print("Processing File:"+str_index)
    tree = ET.parse('Plain_Text/C-' + str_index + '.xml')    
    root = tree.getroot()
 
    #creates input file for POS tagger
    str_text = ET.tostring(root, encoding='utf8', method='text').decode('utf8')
    pos_input_file = open('hindi.input.txt', 'w+')
    pos_input_file.write(str_text)
    pos_input_file.close()

    #system commands for hindi-pos-tagger
    os.system('cp /home/kunal/Documents/ILTIMEX2012/hindi.input.txt /home/kunal/Documents/ILTIMEX2012/pos')
    os.system('cd pos && make tag')
    os.system('cd pos && cp /home/kunal/Documents/ILTIMEX2012/pos/hindi.output /home/kunal/Documents/ILTIMEX2012') #copies output file to main directory


    #reformatting output file
    pos_output_file = open('hindi.output')
    pos_output_str = pos_output_file.readlines()
    for i in range(len(pos_output_str)):
        pos_output_str[i] = pos_output_str[i].split('\t')

    #gets tagged data file
    tagged_file = open('BIO_TaggedM/C-' + str_index + '.txt', 'r+')
    tagged_file_str = tagged_file.readlines()


    """
    The POS tag is appended to the end of the file. The script checks for equality of hindi words in both the files.
    In case of '।', SYM is automatically appended without checing as POS tagger converts it to '.'
    The counter of the tagged file also increments on encountering any of the characters in skip_char.
    In case of inequality inspite of above conditions, the pos counter is incremented.
    """
    p_count = 0
    t_count = 0
    skip_char = ['\n',' ', '\t', '।', '.', '<']
    while p_count<len(pos_output_str) and t_count <len(tagged_file_str):
      #  print(pos_output_str[p_count][0] + " " + tagged_file_str[t_count].split('\t')[0])
        if (tagged_file_str[t_count][0] == '।'):
            tagged_file_str[t_count] = tagged_file_str[t_count][:-1] + '\t' + 'SYM' + '\n'

        if(tagged_file_str[t_count][0] in skip_char):
            t_count += 1
            continue
    #    if(pos_output_str[p_count][0][0] in skip_char ):
    #       p_count += 1
        if(pos_output_str[p_count][0]==tagged_file_str[t_count].split('\t')[0]):
            tagged_file_str[t_count] = tagged_file_str[t_count][:-1] + '\t' + pos_output_str[p_count][2] + '\n'
            p_count+=1
            t_count+=1
        else:
            p_count+=1
            
            

    #The tagged file is overwritten with resulting output.
    new_tagged_file = open('BIO_TaggedM/C-' + str_index + '.txt', 'w+')
    new_tagged_file.writelines(tagged_file_str)

