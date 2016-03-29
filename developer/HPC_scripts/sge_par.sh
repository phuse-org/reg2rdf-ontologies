#$ -cwd
#$ -S /bin/sh
#$ -o sysout
#$ -l h_vmem=2G
#$ -l h_rt=000:01:00
#$ -j y
#$ -N par

#$ -pe thread 1
#$ -t  1-552      #  7537 7305

echo "Running task $SGE_TASK_ID of job $JOB_NAME (ID of $JOB_ID) on $HOSTNAME"

export PATH=/projects/mikem/python/bin:$PATH 
export LD_LIBRARY_PATH=/projects/mikem/python/lib:$LD_LIBRARY_PATH 
export PYTHONPATH=/projects/mikem/python:$PYTHONPATH 
export PYTHONPATH=/projects/mikem/python/lib/python2.7:$PYTHONPATH 
export PYTHONPATH=/projects/mikem/python/lib/python2.7/site-packages:$PYTHONPATH 
export NLTK_DATA=/home/yu.lin/data/nltk_data


LIST=/home/yu.lin/21CFR/output/diff_gensim_run_9.lst
export INPUT=`head -n $SGE_TASK_ID $LIST | tail -n 1`

time python gensim_LDA_single.py   
