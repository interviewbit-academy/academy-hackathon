#!/bin/bash

clear
echo "Downloading images ..."
wget -r -A jpg https://wallpapercave.com/dark-knight-hd-wallpaper
mv wallpapercave.com wallpapercave
rm -rf wallpapercave/img
rm -rf wallpapercave/wpt
rm -rf wallpapercave/robots.txt.tmp
mv wallpapercave/wp/* wallpapercave/
rm -rf wallpapercave/wp
echo "Done!!!"
