#!/usr/bin/python

import os

# returns the files in a directory
def getFiles(directory):
	files = []
	for f in os.listdir(directory):
		files.append(f)
	return files

# parses the test case and returns a list of each line
def parse(testCase):
	f = open("/home/joolz/JAB/ScriptTest/testCases/"+testCase, "r")
	lines = []
	for line in f:
		lines.append(line.rstrip())
	return lines

# returns the command to execute a test
def buildString(text):
	retString = 'pytest --cmdInput="' + text[4] + '" TestFriends.py::' + text[0] + ' "-s"'
	return retString

if __name__ == '__main__':
	
	# stores the name of the test cases in testCases
	testCases = getFiles('testCases')
	testCases.sort()

	#print testCases

	# change the working directory to executables to run the tests
	os.chdir('executables')

	# loop for testing each test case
	for test in testCases:

		# lines stores the each line of a single test case
		lines = parse(test)
		#print lines

		# build the command and execute
		command = buildString(lines)
		print command 
		os.system(command)
