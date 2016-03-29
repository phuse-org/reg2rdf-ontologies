#Input: the 21CFR_dictionary txt file, which contains all the section files with dictionary transformated words.
#Output: gensim_topic_modeling result files

import os,re
from gensim import corpora, models, similarities

# resue the dictionary
dictionary = corpora.Dictionary.load('/home/yu.lin/21CFR/runs/gensim_tmp/21CFR_2wp_dict.dict')
print(dictionary)

logfile = open("/home/yu.lin/21CFR/logfile/gensim_LDA_test.log",'a')
filename="100.100.csv2txt.txt.txt"
logfile.write(filename+"\n")
doc_num = 0
sectionNo = re.sub(".csv2txt.txt.txt",'',filename)
print sectionNo
logfile.write(sectionNo+"\n")
file_1 = "/home/yu.lin/21CFR/output/21CFR_dictionary/100.100.csv2txt.txt.txt"
file_open = open(file_1)
texts = [[word for word in line.split('|') if (word <>'\n')] for line in file_open]
logfile.write("total pragraph: "+str(len(texts))+"\n")
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/home/yu.lin/21CFR/runs/gensim_tmp/CFRdict_phrase.'+sectionNo+'.mm', corpus) 
corpus_1 = corpora.MmCorpus('/home/yu.lin/21CFR/runs/gensim_tmp/CFRdict_phrase.'+sectionNo+'.mm')
print >> logfile,corpus_1
#logfile.write(corpus_1+"\n")
if len(texts)>5:
    chunksize = int(len(texts)/4)
    numtopic = 10
else:
    chunksize = 1
    numtopic = 5
        
lda = models.ldamodel.LdaModel(corpus=corpus,id2word=dictionary, num_topics=numtopic, update_every=1, chunksize=chunksize, passes=4)
lda.save('lda.model')
model = models.LdaModel.load('lda.model')
print >> logfile,model
logfile.write("\n")
        
numTopics = 10

i= 0
keywordfile = '/home/yu.lin/21CFR/output/gensim_LDA_out/gensim_LDA_2wp.'+sectionNo+'.txt'
updateFile = open(keywordfile, 'w')
for topic in model.show_topics(num_topics=numTopics, formatted=False, num_words=10):
    i = i + 1
    updateFile.write("Topic #" + str(i) + ":\n")
    for p, id in [topic]:
        id = str(id)
        p = str(p)
        updateFile.write(id+"["+p+"]\n")
    updateFile.write("----\n")
updateFile.close()

logfile.close()    
