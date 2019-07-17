#html file
wget "https://wallpapercave.com/dark-knight-hd-wallpaper"; 

mainImages=$(grep -o 'slug="dark-knight-hd-wallpaper.*"' dark-knight-hd-wallpaper)

#to get child path =" https://wallpapercave.com/wp/IQNtlNL.jpg" from main site
imgs=$(grep -o "/wp/.*jpg" <<< "$mainImages");

#main website
url="https://wallpapercave.com/";

#downloading all the images from ^img that child slug using wget
for i in $imgs; do
	wget $url$i
done

#delete html file
rm dark-knight-hd-wallpaper 
