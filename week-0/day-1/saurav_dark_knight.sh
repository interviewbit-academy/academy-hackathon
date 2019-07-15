#!/usr/bin/bash
wget -O index.html https://wallpapercave.com/dark-knight-hd-wallpaper
url="https://wallpapercave.com/wp/"
grep -o '<img data-url="[^"]*"' index.html | grep -o '"[^"]*"' | sed 's/"//g'| while read -r line; do
	wget "$url$line.jpg"
done

