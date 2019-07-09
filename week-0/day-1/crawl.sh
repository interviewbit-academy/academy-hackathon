base_url="https://wallpapercave.com"
to_search="dark-knight-hd-wallpaper"
directory="dark-knight-wallpapers"
content=$(curl -L $base_url/$to_search)

files=$(echo $content | grep -o 'src="/wp/[^"]*' | cut -d '/' -f 3)

mkdir $directory

cd $directory

for i in `echo $files | tr ' ' '\n'  | uniq`;
	do
		wget $base_url/wp/$i
	done

cd ..

echo "[-] Done."
