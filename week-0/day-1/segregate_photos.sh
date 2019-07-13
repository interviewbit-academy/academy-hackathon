# parse all the years in which I have taken photos
years=$(for i in `ls`; do echo "$i" | cut -d '-' -f 1; done)
echo $years

# loop through all years and make respective directories
for year in `echo $years`;
do
    mkdir $year;
done

# loop through all png images and moving them in respective directory
for img in `ls *.png`;
do
    # figure out target directory from filename
    year=`echo $img | cut -d '-' -f 1`
    mv $img $year/
done

# double check if everything works
for year in `echo $years | uniq`;
do
    echo "Photos I took in $year:"
    ls -l $year
done
