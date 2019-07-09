echo "Downloading...."
mkdir DKwalls
cd DKwalls
lynx -image_links -dump -nonumbers -listonly wallpapercave.com/dark-knight-hd-wallpaper | grep 'https://.*/wp/.*\.jpg$' > urls.txt
wget -i urls.txt --wait=1
rm urls.txt
cd ..
echo "Done!"
