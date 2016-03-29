#!/bin/sh

TASKS=7305
STEP=1

DIR=home/yu.lin/21CFR/output/21CFR_dictionary
PREFIX=all_
SUFFIX=_1.txt

all_tags=( txt)

merge_one () 
{
    echo "Parameter #1 is $1"
    
    # delete existing list if any
    rm -f list_"$1".txt; 
    
    # create a sorted list
    for ((i=1;i<=$TASKS;i=i+$STEP))
    do
      echo ""$DIR"/*" >> list_"$1".txt ;
    done
    
    # remove old aggregated if any
    rm -f "$PREFIX""$1""$SUFFIX"
    
    # create sorted aggregated
    { xargs cat < list_"$1".txt ; } > "$PREFIX""$1""$SUFFIX"
}

for j in "${all_tags[@]}";
do 
    merge_one $j ;
done 