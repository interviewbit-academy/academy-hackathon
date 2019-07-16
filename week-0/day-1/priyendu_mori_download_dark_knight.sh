#!/bin/bash

url='https://wallpapercave.com/dark-knight-hd-wallpaper'
durl='https://wallpapercave.com'

echo "Getting content of webpage"
content=$(wget $url -q -O -)

echo "Getting img tags out of webpage"
imgs=($(grep -oE "<img.*/>" <<< $content))
images=()

echo "Creating image links"
for i in ${imgs[@]}
do
	arr=($(grep 'src="/wp' <<< $i))
	len=${#arr[@]}
	if [ "$len" -ne 0 ]
	then
		loc=`echo "$i" | cut -d'"' -f 2`
		images+=($durl$loc)
	fi
done

echo "Making download directory priyendu_mori_dark_knight_photos_downloaded if does not exist"
mkdir -p priyendu_mori_dark_knight_photos_downloaded

for i in ${images[@]}
do
	echo "Downloading image: "$i
	wget -P ./priyendu_mori_dark_knight_photos_downloaded $i 	
done

echo "All images downloaded to priyendu_mori_dark_knight_photos_downloaded directory"