#!/bin/bash
#MADE BY haxez.org
# This is a script that will solve the password challenge of Hack This Site basic level 6.
# The password is dynamically generated so please replace the value of MyString with the password.
MyString='62cf4;j=' #replace this value
i=0
base=0
echo "Converting to ascii value"
while (( i++ < ${#MyString} ))
do
   char=$(expr substr "$MyString" $i 1)
    for j in `printf "%d" \'$char` ; do
    	j=$((j+base))
    	printf \\$(printf '%03o' $j)
    	base=$((base-1))
    done;
done;
