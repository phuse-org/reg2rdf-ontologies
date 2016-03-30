# this file is followed by dictionary_rebuild_step2
# this file is similar with word_bag transformation
# it takes all the sections, and transform the key word phrase into one word
# it takes more than 12 hours to run all 7305 files in 21 CFR.

# RAKE output as a key phrase dict
# same as the 
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

# In[22]:

import pickle

with open("/home/yu.lin/21CFR/output/myKeyPhraseDict.txt", "rb") as myFile:
    key_phrase_dict = pickle.load(myFile)


# read all the text file for all sections 
import glob, os, re, sys


#def input_all_files(DIR):
#   files = []
#    for file in glob.glob(os.path.join(DIR, '*.*')):
#        files.append(file)
#   return files

# this are all the text in clean form compare to the csv file

#DIR = "/home/yu.lin/21CFR/output/text_section/RAKE"
#files = input_all_files(DIR)
#print len(files)


# transform the files
import string
# read the lines in each file
import nltk
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

stoplist = set(nltk.corpus.stopwords.words("stopwords_CFR")) 
updateFile1 = open('/home/yu.lin/21CFR/logfile/dictionray_rebuild_log.txt','w')

filename=os.environ['INPUT'] 
file = '/home/yu.lin/21CFR/output/text_section/RAKE/'+filename
updateFile = open('/home/yu.lin/21CFR/output/21CFR_dictionary/'+filename+'.txt','w')    
with open(file) as f:  
    lines = []
    s = f.read()
    for eachkey in key_phrase_dict.keys():
        if re.search(eachkey,s):
            s = s.replace(eachkey,key_phrase_dict[eachkey])
        #s = s.decode("utf-8")
        #lines= s.split('.')# some sentences are splitted by : or ;
    sentence_delimiters = re.compile(u'[\\[\\]\n.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]')
    lines = sentence_delimiters.split(s)
    for line in lines:
       # print line
        if not line.startswith('[') and len(line) >1:
             
            for word in line.lower().split():
                word = re.sub(r"[^A-Za-z_]+", '', word) # remove all others, only keep letters, and the "_" for word phrase
                if (word not in stoplist):
                    if (word.endswith(('ed','ing'))) and (word <> "labeling"):
                        word = wnl.lemmatize(word,'v')
                    else:
                        word = wnl.lemmatize(word)
                    if len(word)>2 :
                        #print word
                        word.encode("utf-8")
                        updateFile.write(word+"|")
            updateFile.write("\n")
    updateFile1.write("writing words from "+filename)
    f.close()
        #newfile = file.replace('clean','new_clean')
        #os.rename(file,newfile)
                
updateFile.close() 
updateFile1.close()

