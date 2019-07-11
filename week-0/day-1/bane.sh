#! /bin/bash

url='https://wallpapercave.com/dark-knight-hd-wallpaper'
regex='https://wallpapercave.com/wp*'

# downloads only jpeg,jpg and png files from the url which match regex
wget -nd -r -P dark-knight-wallpapers -A jpeg,jpg,png --accept-regex $regex $url

# removes any non jpeg files
cd dark-knight-wallpapers
rm -- !(*.jpeg|*.jpg|*.png)
cd ..
