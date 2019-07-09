#!/bin/sh
curl -s https://wallpapercave.com/dark-knight-hd-wallpaper | grep -Eo "/w/[0-9A-Za-z]+" | sed "s/\/w\//https:\/\/wallpapercave.com\/wp\//g" -r | sed -E "s/$/\.jpg/g" -r | uniq > urls.txt
wget -i urls.txt
