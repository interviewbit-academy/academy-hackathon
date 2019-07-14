# Get the HTML Document of the webpage and save in wallpapers.html
curl -o wallpapers.html https://wallpapercave.com/dark-knight-hd-wallpaper

# Exract all the wallpaper urls and store into urls.txt
grep -o '.*jpg' wallpapers.html | cut -d '=' -f 6 | cut -d '"' -f 2 > urls.txt

# Remove all empty lines from urls.txt
sed -i '/^[[:space:]]*$/d' urls.txt

# Append Web site domain name at the beginning
sed -i 's/^/https:\/\/wallpapercave.com/' urls.txt

# Make a new directory for storing the wallpapers
mkdir wallpapers

# Download the wallpapers into the wallpapers directory
wget -i urls.txt -P ./wallpapers

# And we are done downloading the wallpapers enjoy... :-)