ls -1 section/*.csv > temp.lst
ls -1 section/clean/*.csv > temp_1.lst
ls -1 /home/yu.lin/21CFR/output/CFR_keywords_RAKE/*.key > temp_key.lst

# merge the files under 21CFR_dictionary into one file: go under the directory and merge the files.
cat * > merged-file.txt

# the gensim_LDA couldn't do a full run. Here is a way to extract the different lines between two list files.
comm -23 <(sort Copy\ of\ temp_21CFR_dictionary.lst) <(sort gensim_run.lst) > diff_gensim_run.lst

# add the string ".csv2txt.txt.txt" to file
sed -e 's/$/.csv2txt.txt.txt/' -i diff_gensim_run.lst

# remove size = 0 files in gensim_LDA_out folder