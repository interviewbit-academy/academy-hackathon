#!/usr/bin/bash
#above line make bash as default to run

#declare an empty array
keys=()

#iterate through the downloaded html file
for line in $(wget -O- https://wallpapercave.com/dark-knight-hd-wallpaper);
do
#take key of image which look similar to the text and store in keys array
	keys+=($(echo $line | grep "/download/dark-knight-hd-wallpaper-"))
done


for (( i=0; i<${#keys[*]}; i++ ));
do

#remove prefix href
	keys[$i]=${keys[$i]#href=\"}
#remove suffix 
	keys[$i]=${keys[$i]%\">}
done

#base url
url="https://wallpapercave.com"

#concat the base url with key
keys=(${keys[*]/#/$url})

#downloading the image from link in the same directory
for i in ${keys[*]};
do
wget $i
done

