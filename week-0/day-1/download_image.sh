#!/bin/bash
rm -r images
wget -k https://wallpapercave.com/dark-knight-hd-wallpaper

cat dark-knight-hd-wallpaper | grep img | grep -Po 'src="\K.*?(?=")' | sed 's/\?.*//' | grep -i '/wp/' > links.txt

wget -i links.txt
mkdir images
rm -r links.txt
rm -r dark-knight-hd-wallpaper
mv *.jpg images/