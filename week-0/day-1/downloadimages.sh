baseurl="https://wallpapercave.com";

for relativeurl in `curl $baseurl/dark-knight-hd-wallpaper | grep -o "/download/[a-zA-Z0-9-]*"`;
do
wget "$baseurl$relativeurl";
done;
