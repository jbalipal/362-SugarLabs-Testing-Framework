#This is the beginning of the script that will be used to parse through a .txt file that will then
#invoke method calls and write to a separate .txt file to

#This command open the txt file to be read by the script
file = open("test.txt", "r")
data = []
test_ID = []
requirement = []
component =[]
method = []
test_input = []
expected_outcomes = []

for line in file:
    data.append(line.strip())

#this is just a test statement that prints out everything that is currently stored in the
#data list
#print data

#The following loops are based on the fact that the txt file will have test cases every
#6 lines. So, first six lines of the txt file will be a test case then the second set of 6 lines
#(lines 6-11) will be the second test case and so on.

#This loop will store all of the test_ID's in the txt file into the test_ID list
for i in range(0, len(data), 6):
    test_ID.append(data[i])
#This loop will store all of the test requirements in the txt file into the requirement list
for i in range(1, len(data), 6):
    requirement.append(data[i])
#This loop will store all of the test components in the txt file into the component list
for i in range(2, len(data), 6):
    component.append(data[i])
#This loop will store all of the test methods in the txt file into the method list
for i in range(3, len(data), 6):
    method.append(data[i])
#This loop will store all of the test inputs in the txt file into the test_input list
for i in range(4, len(data), 6):
    test_input.append(data[i])
#This loop will store all of the test expected outcomes into the expected_outcomes list
for i in range(5, len(data), 6):
    expected_outcomes.append(data[i])

