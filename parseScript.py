#This is the beginning of the script that will be used to parse through a .txt file that will then
#invoke method calls and write to a separate .txt file to

#This command open the txt file to be read by the script
file = open("test.txt", "r")
data = []

for line in file:
    data.append(line.strip())

print data

for i in range(0, len(data), 7):
    print data[i]
#This command will print out the first line of the file
#print file.read()

