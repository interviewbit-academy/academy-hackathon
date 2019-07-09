#!/bin/bash

wget -q -O source.txt https://wallpapercave.com/dark-knight-hd-wallpaper
grep -oh 'wp/.*.jpg' source.txt >> url.txt

# keep one copy of duplicate lines 
sort url.txt | uniq >> uniqurl.txt

while IFS= read -r line; 
do
    wget https://wallpapercave.com/$line
done < uniqurl.txt
  