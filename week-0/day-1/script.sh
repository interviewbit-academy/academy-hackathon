# grab and store html code for wallpapers page
result=$(wget -qO- https://wallpapercave.com/dark-knight-hd-wallpaper)

# store image urls in this array
urls=()

# iterate over the html code and filter image urls using grep
# and add them to urls array
for i in $result
do
	urls+=($(echo $i | grep "/download/dark-knight-hd-wallpaper-"))
done

# length of urls array
# number of images that will be downloaded
len=${#urls[@]}

# iterate over the urls array to remove extra characters
for (( i=0; i<$len; i++ ))
do
	# store current element in temp
	temp=${urls[$i]}
	# remove prefix
	temp="${temp#href=\"}"
	# remove suffix
	temp="${temp%\">}"
	# store it back in same array
	urls[$i]=$temp
done

# base url
base="https://wallpapercave.com"

# add base url
urls=("${urls[@]/#/$base}")

# now, we have the exact download url in urls array
# downloading them using wget
for (( i=0; i<$len; i++ ))
do
	temp=${urls[$i]}
	# download and save the image in current directory
	# images names will be 0.jpg, 1.jpg, 2.jpg, 3.jpg...
	wget -O "${i}.jpg" $temp
done