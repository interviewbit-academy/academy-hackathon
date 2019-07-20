#/bin/bash

for url in $(cat URLs.txt); do
	open -a "Google Chrome" $url
done
