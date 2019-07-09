link=https://wallpapercave.com/dark-knight-hd-wallpaper #link to website
wget $link -O website #download website and store html in website file
#fetch all img tags from website 
#fetch all src attribute values with ""
#remove "" from srcs and store in imglinks
grep -o '<img[^>]*>' website | grep -o 'src *= *"[^"]*"' | grep -o '"[^"]*"' | cut -d '"' -f 2 > imglinks
link=`echo $link | cut -d '/' -f 1,2,3` #strip dark-knight-hd-wallpaper
mkdir pics #make directory to download pics
for imglink in `cat imglinks`;
do
	imglink=$link$imglink #concatenate domain with relative address
	echo 'Downloading '$imglink #verbose output
	# -P to save to directory
	# -q to suppress output
	# -b to run download in background to speed up processing
	# -nc to skip downloads which already exist
	wget -P pics $imglink -q -b -nc;
done 
rm website imglinks #delete temporary files