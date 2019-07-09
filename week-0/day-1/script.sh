#getting html file of the website using wget
wget "https://wallpapercave.com/dark-knight-hd-wallpaper";

#extracting the wallpapers from html file using slug name
mainImages=$(grep -o 'slug="dark-knight-hd-wallpaper.*"' dark-knight-hd-wallpaper)

#extracting child routes of images from $mainImages
result=$(grep -o "/wp/.*jpg" <<< "$mainImages");

#parent url of website
url="https://wallpapercave.com/";

#looping all the images and downloading the images with wget
for i in $result; do
	wget $url$i
done

#removing html file
rm dark-knight-hd-wallpaper