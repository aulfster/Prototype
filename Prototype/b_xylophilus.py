import sys
import time
import os

f = open("b_xylophilus.fa","r")
t0 = time.time()


text_file = open("temp.fa","a")

while True:
    line = f.readline()
    if line == "":
        break
    if line.startswith(">"):
        line = line.split("\t")[0]
        line = line + "\n"
    text_file.write(line)

text_file.close()
f.close()

timeFile = open("time.txt","a")
t1 = time.time()
now = t1 - t0
timeFile.write(str(now)+"\n")
timeFile.close()

f = open("temp.fa","r")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

mapping = {"tag" : None}

while True:
    line = f.readline()
    if line == "":
        break
    if line.startswith(">"):
        if line[-2] not in numbers:
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
                if tag[0:-1] in key:
                    flag = 1
                    if len(mapping[key]) < len(writeString):
                        del mapping[key]
                        mapping[tag] = writeString
                    break
                    
            if flag == 0:
                mapping[tag] = writeString
        else:
            tag = line[1:-1]
            writeString = ""
            last_pos = f.tell()   
            while True:     
                temp_line = f.readline()
                if temp_line.startswith(">"):
                    f.seek(last_pos)
                    break
                writeString = writeString + temp_line
            mapping[tag] = writeString
f.close()

os.remove("temp.fa")

timeFile = open("time.txt","a")
t2 = time.time()
now = t2-t1
timeFile.write(str(now)+"\n")
timeFile.close()

with open("b_xylophilus_p.fa", "a") as text_file:
    del mapping["tag"]
    for key in mapping.keys():
        line = ">" + key + "\n" + mapping[key]
        text_file.write(line)        
text_file.close()

timeFile = open("time.txt","a")
t3 = time.time()
now = t3-t2
timeFile.write(str(now)+"\n")
timeFile.close()

sys.exit()


            
    
    
