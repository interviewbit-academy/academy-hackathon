#!/bin/bash

#make di t save wallpapers
mkdir ./walpapers

#move to wallpapers directory
cd ./walpapers/

#download the html file
wget https://wallpapercave.com/dark-knight-hd-wallpaper

#find the image links and download the images
for x in $(grep -Po '(?<=href=")[^"]*/w/[^"]......' dark-knight-hd-wallpaper | cut -d '/' -f 3 | uniq); do wget https://wallpapercave.com"/wp/$x.jpg";done

#remove the html file
rm dark-knight-hd-wallpaper
