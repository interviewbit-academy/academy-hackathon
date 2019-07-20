#!/bin/bash

#This code can only download wallpapers from the website https://wallpaperscave.com

# get entire page's html code..
echo 'Enter The Url Without Any Leading Spaces!'
read url
curl $url -o 'images.html'

# get all images and download them..
i=1;
url=${url#*.com/}
mkdir $url
grep -oh 'https://wallpapercave.com/*.*jpg' images.html | while read -r line;
do
	src=${line#*src=\"}
	curl -o './'$url'/'$url$i'.jpg' 'https://wallpapercave.com/'$src
	((i++))
done

##tried with---->>>>
###https://wallpapercave.com/dark-knight-hd-wallpaper
