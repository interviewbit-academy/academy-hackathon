# Get the HTML Document of the webpage and save in index.html
curl -o index.html https://wallpapercave.com/dark-knight-hd-wallpaper

# Extract the source of the image using egrep with the help of regular expressions and remove alternate lines using sed
egrep -o "[/]wp[/][[:alnum:]]{7}\.jpg" index.html | sed '1~2d' > urls.txt

# Create the full url by appending the domain 
sed -i 's/^/https:\/\/wallpapercave.com/' urls.txt

# Make a new directory for storing the wallpapers
mkdir batman-wallpapers

# Download the wallpapers into the above directory
wget -i urls.txt -P ./batman-wallpapers
