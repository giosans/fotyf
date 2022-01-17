#!/bin/bash

# # List all the formats you wish to have
# SIZES="640x480 800x600 1024x768"

# pass directory as first argument to the script
# Use '.' (current directory) if no argument was passed
DIR=${1:-.}

find $DIR -type f | while read file; do
#   for size in $SIZES; do
       # Resize and rename DSC01258.JPG into DSC01258_640x480.JPG, etc.
       # Remove the ! after $size if you do not wish to force the format
       currentSize=$(identify -format "%[fx:w]x%[fx:h]" "$file")
       if [ "$currentSize" == "6000x4000" ]; then
	   size="750x500"
	   convert -resize "${size}!" "$file" "${file%.*}_${size}.${file##*.}"
	   echo "6000x4000 conversion succesfull"
       elif [ "$currentSize" == "4000x6000" ]; then
	   size="500x750"
	   convert -resize "${size}!" "$file" "${file%.*}_${size}.${file##*.}"
	   echo "4000x6000 conversion succesfull"
       else
	   echo "no proper image for conversion. Do not resize..."
       fi
#   done
done

# RUN THIS AS FOLLOWING:
# $ chmod +x convert.sh
# $ ./convert.sh  # JUST RUN THIS
# $ ./convert.sh large-gallery # if you need to work inside a folder
# # btw., to identify the format of an image, go for the following:
# $ identify -format "%[fx:w]x%[fx:h]\n" *.jpg
