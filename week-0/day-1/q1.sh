url="https://wallpapercave.com/dark-knight-hd-wallpaper"
#all Images
wget -r -nd -A jpg -e robots=off $url
#new Directory To StoreRequired Images
mkdir images
#moving Reqd Images To images Dir
mv wp*.jpg images
#deleting Unneccesary Files
find . -maxdepth 1 \! -name 'q1.sh' \! -name 'images' -delete
#Now All Reqd Images Are In images Folder
