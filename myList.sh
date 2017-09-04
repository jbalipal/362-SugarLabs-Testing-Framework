#!/bin/bash
file_path=$((readlink -f myList) | head -c-7) #initializes variable that represents filepath to code
cat /dev/null > output.html                   #Creates blank file "output.html" and clears it if it already exists
echo "<html>" >> output.html                  #Begins feeding code to output.html
echo "<head>" >> output.html
echo "<title>Top Level Directory Contents</title>" >> output.html
echo "</head>" >> output.html
echo "<body>" >> output.html
echo "<p>" >> output.html
echo "The Contents of myList's Containing Folder Are" >> output.html
echo "<br>" >> output.html
echo "<br>" >> output.html
for entry in `ls $file_path`; do
 echo $entry >> output.html      #Writes output to an html file, making sure each entry is on a new line
 echo "<br>" >> output.html
done
echo "</p>" >> output.html
echo "</body>" >> output.html
echo "</html>" >> output.html    #Finish feed to output.html
xdg-open output.html       #open output.html in default browser







