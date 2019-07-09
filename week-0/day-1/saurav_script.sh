echo "Downloading HTML file of the website"; 
`curl https://wallpapercave.com/dark-knight-hd-wallpaper>webpage`;
#echo $x
y=$(grep -e download/dark-knight-hd-wallpaper-* webpage|cut -d '-' -f 5|cut -d '"' -f 1);

echo "Downloading images";

#`mkdir wallpaper_batman`
#`cd wallpaper_batman`
for code in $y
do
	wget "https://wallpapercave.com/download/dark-knight-hd-wallpaper-"$code -O $code.jpg;
done

