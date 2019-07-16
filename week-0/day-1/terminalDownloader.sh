#!/bin/bash

userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
baseUrl="https://wallpapercave.com"
url="https://wallpapercave.com/dark-knight-hd-wallpaper"
project="DarkKnightDownloader"
downloadsFolder="downloads"
customRegex='img data-url="\K([^ "]*)'
storeFiles=true

webPageFile="index.html"
customRegexFile="customRegex.txt"

rm -rf "$project" && echo "Removed any existing directory with the name : $project"

mkdir "$project" && cd "$project" && echo "Made new directory $project"

mkdir "$downloadsFolder" && echo "Made downloads Folder $downloadsFolder"

htmlContent=$(wget -U "$userAgent" "$url" -O -) 

echo "Retrieved the WebPage"

if $storeFiles
then
  echo $htmlContent > "$webPageFile"
  echo "Stored Web Page to $webPageFile"	
fi

reqPatterns=$(echo $htmlContent | grep -Po "$customRegex")

echo "Applied custom Regex"

if $storeFiles
then
  echo $reqPatterns > "$customRegexFile"
  echo "Stored Regex Results to $customRegexFile"    
fi

cd $downloadsFolder

while IFS= read -r -d $' ' word
do
  src="$baseUrl/wp/$word.jpg"
  # echo $src
  # echo $word	
  wget -U "$userAgent" $src
  echo "Downloaded from $src"
done < <(echo $reqPatterns)

