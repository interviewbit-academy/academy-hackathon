#/bin/bash
# ===================================================================
# Purpose:           Download Dark Knight HD wallpapers using bash scripts 
#					 from this URL: https://wallpapercave.com/dark-knight-hd-wallpaper
# Author:            Manan Nahata
# Revsion:           Last change: 09/07/2019
# ===================================================================
url="https://wallpapercave.com/dark-knight-hd-wallpaper"  #url to download dark knight wallpapers
url1="https://wallpapercave.com"

echo "Downloading the source code of the page" 
wget -O page.html $url # Download the html from page to page.html

#Parse the html and observe that all the dark-knight wallpapers have slug = "dark-knight-hd-wallpaper"
#Use grep to find all such instances from the html
#	Outputs something: 
#					<a href="/w/IQNtlNL" class="wpinkw"><img data-url="IQNtlNL"
#					 slug="dark-knight-hd-wallpaper" src="/wp/IQNtlNL.jpg" 
#					 alt="The Dark Knight Rises HD Wallpapers | I Have A PC" class="wpimg" /></a>
#Use cut and "=" as a delimiter to strip the given fields,
#Select the correct column corresponding to filenames of images
#	Outputs something:
#					"/wp/IQNtlNL.jpg" alt
#Use cut and '"' as a delimiter and select the column containing filename
#	Outputs:
#			/wp/IQNtlNL.jpg
#Save all these filenames to a text file				

cat page.html | grep 'slug="dark-knight-hd-wallpaper"' | cut -d '=' -f6 | cut -d '"' -f2 >> filenames.txt

mkdir downloads # Create a directory to save the images

# loop over the filenames and wget the images
echo "Starting download of wallpapers"
for i in `cat filenames.txt`
do
	wget -P downloads "https://wallpapercave.com/$i"
done

rm page.html filenames.txt # Delete unnecessary files
echo "Done!"
