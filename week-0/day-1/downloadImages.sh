#!bin/bash 

#tested on url https://www.ostechnix.com/the-grep-command-tutorial-with-examples-for-beginners/

echo "Enter the url"

read url

wget $url -O index.html

egrep -o '"https://www.[^"]*(.jpg|.png|.gif|.jpeg)"' index.html | egrep -o '[^"]*' > links.txt

wget -i links.txt
