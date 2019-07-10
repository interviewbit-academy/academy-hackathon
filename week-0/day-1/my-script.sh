mkdir images
wget -nd -r -l 1 -P ./images -A jpg,jpeg https://wallpapercave.com/dark-knight-hd-wallpaper
rm ./images/caveman.jpg ./images/robots.txt.tmp #unecessary files

# -r recursive traversal
# -l recursive level is set 1, so that it doesn't download from next directory
# -P path where images will be saved
# -A download only .jpg and .jpeg images
