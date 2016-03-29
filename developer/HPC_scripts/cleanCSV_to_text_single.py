# this section is to put the text of csv file and save as RAKE input, as well as web browser input

import re
import glob
import os
import nltk

	
DIR = "/home/yu.lin/21CFR/output/section/clean/"
filetype = "csv"

# define the output folder
newdir = "/home/yu.lin/21CFR/output/text_section/RAKE"

file=os.environ['INPUT'] 
file1 = file.replace('.csv','')
file = DIR+file
openfile = newdir+"/"+file1+".csv2txt.txt"
updateFile = open(openfile,'w')
with open(file) as f:
    lines =[]
    s = f.read()
    s = s.decode("utf8")
    lines= s.split('","')
    for line in lines:
        if not line.startswith('['):
            for word in line.lower().split():
                word = re.sub(r"[^[,\.:;[\(][\)]0-9A-Za-z]]+", '', word)
                word = word.encode("ascii","ignore")
                updateFile.write(word+" ")
        updateFile.write("\n")
updateFile.close()