for i in `curl https://wallpapercave.com/dark-knight-hd-wallpaper | grep -o "/download/[A-Za-z0-9-]*"`
do
wget "https://wallpapercave.com$i"
done


