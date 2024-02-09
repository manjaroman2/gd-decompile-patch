#!/bin/bash 

pck_file=""

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "supply first arg ex dir" 
    echo "supply second arg name" 
    exit 1 
fi 
if [ ! -z "$3" ]; then
    pck_file="$3"
else
    if [ -z "$pck_file" ]; then 
        echo "provide pck file" 
        exit 1 
    fi 
fi 

cd .. 
./decomp-3.5.3.sh $pck_file $1
cd $1

chmod +x $name/stuff.sh 
$name/stuff.sh 

# echo 
echo "python $2/apply.py" 
echo "python $2/create_patch.py" 
