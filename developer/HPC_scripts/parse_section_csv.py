# Functionality of this code:  read all the files in the section folder, remove all the "|" in lines.

# read all the files from the folder
import sys
import os
import re

DIR = "/home/yu.lin/21CFR/section/"
#new_DIR = "/home/yu.lin/21CFR/section/clean"
#os.makedirs(new_DIR)
section_no_list = []
for i in os.listdir(DIR):
    if i.endswith(".csv"):
        
        for line in open(DIR+i,"r"):  # there is only one line in the file
            line = re.sub("\"\|\"","",line)
#            print line
            cell_list = line.split("\",\"",1)
            section_no = cell_list[0]
            if section_no not in section_no_list:
                section_no_list.append(section_no)
                section_no = re.sub("[^0123456789\.]","",section_no)
                updateFile = open(DIR+"clean/"+section_no+".csv",'w')
                updateFile.write(line)
                updateFile.close()
            else:
				logFile = open("/home/yu.lin/21CFR/logfile/parse_section_csv.log")
				logFile.write("Sections of 21CFR with amandment content:\n")
                logFile.write(i+"\n")
				logFile.write(section_no+"\n")
                
                #above sections have amandment, which overwrites current csv files
#            print section_no
#            