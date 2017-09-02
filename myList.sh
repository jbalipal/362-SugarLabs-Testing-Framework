#!/bin/bash
file_path=$((readlink -f myList) | head -c-7)
echo $file_path
#!/$file_path
cat /dev/null > output.html
echo "<html>" >> output.html
echo "<head>" >> output.html
echo "<title>Top Level Directory Contents</title>" >> output.html
echo "</head>" >> output.html
echo "<body>" >> output.html
echo "<p>" >> output.html
echo "The Contents of myList's Containing Folder Are" >> output.html
echo "<br>" >> output.html
echo "<br>" >> output.html
for entry in `ls $file_path`; do
 echo $entry >> output.html      #Writes output to an html file
 echo "<br>" >> output.html
done
echo "</p>" >> output.html
echo "</body>" >> output.html
echo "</html>" >> output.html
xdg-open output.html       #open 







