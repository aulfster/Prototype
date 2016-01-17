import sys
import time
import os

filevar = "c_elegans_p.fa"
f = open(filevar,"r")

gene_set = ["C38D4.8", "Y105E8A.5", "F20D12.3", "F58A4.14" , "R01H10.6", "T25F10.5", "C48B6.8", "C27A7.4", "F59C6.7", "F38G1.1", "F33H1.1", "F54C1.5", "C02H7.1", "C27H5.7", "H01G02.2", "ZK520.3", "C04C3.5", "M04C9.5", "D1009.5", "Y110A7A.20", "C54G7.4", "R148.1", "K07G5.3", "K03E6.4", "Y38F2AL.2", "Y32G9A.6", "Y102E9.1", "T27B1.1", "Y75B8A.12", "Y41G9A.1", "R31.3", "F10B5.4", "F02D8.3" ]

text_file = open(filevar + "_temp_now","a")

while True:
    line = f.readline()
    writeString = ""
    if line == "":
        break
    tt = line[1:-1]    
    if line.startswith(">"):
        if line[-2].isalpha():
            tt = line[1:-2]
        if tt in gene_set:
            writeString = line
            last_pos = f.tell()  
            while True:
                temp_line = f.readline()
                if temp_line.startswith(">") or temp_line == "":
                    f.seek(last_pos)
                    break
                writeString = writeString + temp_line
            text_file.write(writeString)

text_file.close()
f.close()


