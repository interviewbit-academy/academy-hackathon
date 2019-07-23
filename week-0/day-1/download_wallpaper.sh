echo "###########          Welcome          ##########"
wget -r -l 1 -A jpg https://wallpapercave.com/dark-knight-hd-wallpaper
echo "Creating new folder DarkKnightWallpapers.........."
mkdir DarkKnightWallpapers
mv ./wallpapercave.com/wp/* ./DarkKnightWallpapers
rm -r ./wallpapercave.com/
printf "Download finished !\nWallpapers downloaded in folder 'DarkKnightWallpapers'"