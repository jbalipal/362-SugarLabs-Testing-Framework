#!/usr/bin/python

import sys
import os
import subprocess
import webbrowser

# returns the files in a directory
def getFiles(directory):
    files = []
    for f in os.listdir(directory):
        files.append(f)
    return files

# parses the test case and returns a list of each line
def parse(testCase):

    f = open(testCase, "r")
    lines = []
    for line in f:
        lines.append(line.rstrip())
    f.close()

    return lines

# returns the command to execute a test
def buildString(text):
    # change retString to something that will work with out current tests
    retString = 'python ' + text[0] +'.py ' + text[4]
    return retString

if __name__ == '__main__':

    # stores the name of the test cases in testCases
    testCases = getFiles('testCases')
    testCases.sort()
    #print testCases
    os.chdir('reports')

    # delete old output?
    if os.path.isfile("testOutput.html"):
        print "file already exists... deleting and making new testOutput.html"
        os.remove("testOutput.html")
    else:
        print "creating new testOutput.html"

    f = open("testOutput.html", "w+")
    f.write("<html>")
    f.write("<head>")
    f.write("<title>Test Results</title>")
    f.write("</head>")
    f.write("<body>")
    f.write("<p>")
    f.write("The Test Results for the Sugar Components are:")
    f.write("<br>")
    f.write("<br>")

    os.chdir('../testCases')
    # loop for testing each test case
    for test in testCases:
        # lines stores each line of a single test case
        lines = parse(test)
        #print lines
        # build the command and execute
        os.chdir('../testCasesExecutables')
        #command = buildString(lines)
        #os.system(command)

        # check_output runs the test lines[0].py with input lines[4] and stores output in testOut 
        testOut = subprocess.check_output([sys.executable, lines[0] + ".py", lines[4]])
        f.write(testOut + "<br/>")
        os.chdir('../testCases')


    f.write("</p>")
    f.write("</body>")
    f.write("</html>")
    os.chdir('../reports')
    f.close()

    webbrowser.open('file://' + os.path.realpath("testOutput.html"))

