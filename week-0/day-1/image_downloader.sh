#get the website in terminal
wget -U/Mozilla -q "https://wallpapercave.com/dark-knight-hd-wallpaper" -O -

wget -U/Mozilla -q "https://wallpapercave.com/dark-knight-hd-wallpaper" -O -|grep 'g data-url'

wget -U/Mozilla -q "https://wallpapercave.com/dark-knight-hd-wallpaper" -O -|grep 'g data-url'|cut -d\" -f2

wget -U/Mozilla -q "https://wallpapercave.com/dark-knight-hd-wallpaper" -O -|grep 'g data-url'|cut -d\" -f2|while read id;do echo "Downloading $id.jpg";wget -q -c "https://wallpapercave.com/$id.jpg";done


