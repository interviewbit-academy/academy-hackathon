#!/bin/sh

#Get html page from url https://wallpapercave.com/dark-knight-hd-wallpaper  into  wp.html

wget https://wallpapercave.com/dark-knight-hd-wallpaper -O wp.html


#Get all the image links from wp.html  and add  missing prefixes . Here missing prefix is https://wallpapercave.com . Save urls in urls.txt after adding prefixes.

grep -Eo "(https?:)?/[^/\s]+/\S+\.(jpg|png|gif)" wp.html | sed "s/^\//https\:\/\/wallpapercave.com\//g" -r > urls.txt


#Get wallpapers from urls.txt using wget

wget -i urls.txt -P wallpapers/
