import rake

# This is the code to generate keywords from CFR in bulk.

# 
stoppath = "FoxStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file and setting phrase length in words to 1
rake_object = rake.Rake(stoppath, min_char_length=5, max_words_length=2, min_keyword_frequency=1)

#2. get all the files
import glob, os, re
i = 0
#for file in glob.glob(os.path.join('/home/yu.lin/21CFR/output/text_section/RAKE/', '*.txt')):
file = os.environ['INPUT'] 
file_1 = '/home/yu.lin/21CFR/output/text_section/RAKE/'+file 
#i = i+1
f2re = file.replace('.csv2txt.txt','') 
# changed the f2re name

# 2. run on RAKE on a given text
sample_file = open(file_1, 'r')
text = sample_file.read()
keywords = rake_object.run(text)

# 3. print results to single file for each input file
    #outputfilename = "/home/yu.lin/21CFR/output/CFR_keywords_RAKE/"+f2re+".key"
output_file = open("/home/yu.lin/21CFR/output/CFR_keywords_RAKE/"+f2re+".key",'w')
for keyword, wordscore in keywords:
    keyword = str(keyword)
    wordscore = str(wordscore)
    output_file.write(keyword+","+wordscore+"\n")
output_file.close()
    
#print i