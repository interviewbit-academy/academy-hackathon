url='https://wallpapercave.com/dark-knight-hd-wallpaper'
durl='https://wallpapercave.com'

echo "Getting content of webpage"
content=$(wget $url -q -o -)

echo "Getting img tags out of webpage"
imgs=($(grep -oE "<img.*/>" <<< $content))
images=()

echo "Creating links"
for i in ${imgs[@]}
do
	arr=($(grep 'src=/wp' <<< $i))
	len=${#arr[@]}
	if ["$len" -ne 0 ]
	then
		loc=`echo "$i" | cut -d '"' -f 2`
		images+=($durl$loc)
	fi
done

echo "Making Download directory"
mkdir -p piyush_raj_download

for i in ${images[@]}
do
	echo "Downloading image: "$i
	wget -P ./piyush_raj_download $i
done

echo "All images downloaded"


















