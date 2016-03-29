#$ -cwd
#$ -S /bin/sh
#$ -o sysout
#$ -l h_vmem=2G
#$ -l h_rt=000:10:00
#$ -j y
#$ -N gensim_LDA_nonpar

#$ -pe thread 1
#$ -t  1-1

echo "Running task $JOB_NAME (ID of $JOB_ID) on $HOSTNAME"

export PATH=/projects/mikem/python/bin:$PATH 
export LD_LIBRARY_PATH=/projects/mikem/python/lib:$LD_LIBRARY_PATH 
export PYTHONPATH=/projects/mikem/python:$PYTHONPATH 
export PYTHONPATH=/projects/mikem/python/lib/python2.7:$PYTHONPATH 
export PYTHONPATH=/projects/mikem/python/lib/python2.7/site-packages:$PYTHONPATH 

time python gensim_LDA_single_nonpar.py   
