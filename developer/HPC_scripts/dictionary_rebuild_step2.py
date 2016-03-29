# take the 21CFR_dictionary_merged-file.txt and build a dictionary for Gensim

import gensim
from gensim import corpora, models, similarities
file = open('/home/yu.lin/21CFR/output/21CFR_dictionary_merged-file.txt')

texts = [[word for word in line.split('|') if word <>'\n']
         for line in file]

dictionary = corpora.Dictionary(texts)

# store the dictionary for future reference
dictionary.save('/home/yu.lin/21CFR/runs/gensim_tmp/21CFR_2wp_dict.dict') 

#print(dictionary)

