import sys
import time
import os

#file_name = "b_xylophilus"
#f = open("m_incognita.fa","r")
#temp_file_name = "m_incognita.fa"
#organism_name= "m_incognita"
f = open(sys.argv[1],"r")

temp_file_name = sys.argv[1]
temp_file_name = temp_file_name.split(".")[0]
organism_name = temp_file_name.split(os.path.sep)[0]



if os.path.isfile(temp_file_name + "_temp.fa"):
    os.remove(temp_file_name + "_temp.fa")

text_file = open(temp_file_name + "_temp.fa","a")

while True:
    line = f.readline()
    if line == "":
        break
    if line.startswith(">"):
        temp = line.split("\t")
        flag = 0
        for str in temp:
            if "WBGene" in str:
                line = str
                line = ">" + line + "|" + temp[1]
                flag = 1

        if flag == 0:
            line = temp[0] + "|" + organism_name

        line = line + "\n"
    text_file.write(line)

text_file.close()
f.close()

f = open(temp_file_name + "_temp.fa","r")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

mapping = {}

count_keys = 0
while True:
    line = f.readline()
    if line == "":
        break
    if line.startswith(">"):
        temp = line.split("|")[0][1:]
        key_str = line
        tag = line[1:-1]
        writeString = ""
        last_pos = f.tell()  
        while True:
            temp_line = f.readline()
            if temp_line.startswith(">") or temp_line == "":
                f.seek(last_pos)
                break
            writeString = writeString + temp_line
                
        

        flag = 0
        for key in mapping.keys():
            tt = key.split("|")[0]
            if tt[-1] not in numbers:
                if temp[1:-1] in key.split("|")[0]:
                    flag = 1
                    if len(mapping[key]) < len(writeString):
                        del mapping[key]
                        mapping[tag] = writeString
                    break
            else: 
                if temp[1:] in key.split("|")[0]:
                    flag = 1
                    if len(mapping[key]) < len(writeString):
                        del mapping[key]
                        mapping[tag] = writeString
                    break
                    
        if flag == 0:
            mapping[tag] = writeString
            count_keys = count_keys + 1
f.close()

os.remove(temp_file_name + "_temp.fa")


if count_keys < 25000:
    temp_file_name = temp_file_name + "_g.fa"
else:
    temp_file_name = temp_file_name + "_b.fa"

with open(temp_file_name, "a") as text_file:
    for key in mapping.keys():
        line = ">" + key + "\n" + mapping[key]
        text_file.write(line)        
text_file.close()

sys.exit()


            
    
    
