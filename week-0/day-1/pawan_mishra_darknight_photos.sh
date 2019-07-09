#!/bin/bash

#  Submitted by PAWAN MISHRA pawone3@gmail.com


curl https://wallpapercave.com/dark-knight-hd-wallpaper > source_dkr.txt

# cat source_dkr.txt

# cat source_dkr.txt | grep "class=\"wpinkw\""

# cat source_dkr.txt | grep "class=\"wpinkw\"" | cut -d'"' -f6

# for i in `cat source_dkr.txt | grep "class=\"wpinkw\"" | cut -d'"' -f6`;do echo $i; echo $i; done

for i in `cat source_dkr.txt | grep "class=\"wpinkw\"" | cut -d'"' -f6`;do wget https://wallpapercave.com/w/$i.jpg; done
