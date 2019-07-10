# Script to download images from url
url="https://wallpapercave.com/dark-knight-hd-wallpaper";
output="dark-images"; 
mkdir $output; 
wget -P $output -nd -p -A jpg -e robots=off $url
