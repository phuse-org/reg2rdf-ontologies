# Generate a file contains the dictionary for later use

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

def key_phrase(phrase_path):
    files = []
    import glob, os,re
    for file in glob.glob(os.path.join(phrase_path, "*.key")):
        files.append(file)

    key_phrase = dict()
    for file_name in files:
        with open(file_name) as f:
            for line in f:
                line = line.decode('utf-8').strip()
                line_words = line.split(',')
                words = line_words[0]
                words=re.sub(r"[^A-Za-z ]+", '', words)
                words_s = words.split()
                words_1 = []
                if len(words_s) > 1: 
                    for word in words_s:
                        
                        if (word.endswith(('ed','ing')) and word <> 'labeling'):
                            word = wnl.lemmatize(word,'v')
                        else:
                            word = wnl.lemmatize(word)
                        words_1.append(word)
                        words_2 = "_".join(words_1)
                    key_phrase[words]=words_2
    return key_phrase 
   
# read all key phrase and stemmed form from the RAKE key word extraction result

phrase_path = "/home/yu.lin/21CFR/output/CFR_keywords_RAKE"
key_phrase_dict = key_phrase(phrase_path)

import pickle

with open("/home/yu.lin/21CFR/output/myKeyPhraseDict.txt", "wb") as myFile:
#/dev/shm/myKeyPhraseDict.txt
    pickle.dump(key_phrase_dict, myFile)
    
 