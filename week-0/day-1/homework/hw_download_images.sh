#! /bin/bash
dirName='batman'
mkdir $dirName
links=$(lynx -dump https://wallpapercave.com/dark-knight-hd-wallpaper | awk '/http/{print $2}')
temp=()
num=1
for i in $links;
do
	t=$(echo $i | cut -d '/' -f4-)
	t1=$(echo $t | cut -d "w" -f2- | cut -d '/' -f2-)
	if [[ $t1 == *"dark-knight-hd-wallpaper-"* ]];
	then
		img=$(echo $t1 | cut -d '-' -f 5).jpg
		echo 'downloading '$img
		wget -O ./$dirName/$num.jpg 'https://wallpapercave.com/w/'$img
		num=$((num+1))
	fi
done
