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

# creates a file for reporting results
def initializeReport(fileName, numCases):

		# delete output file if it already exists
    if os.path.isfile(fileName):
        print "file already exists... deleting and making new testOutput.html"
        os.remove(fileName)
    else:
        print "creating new testOutput.html"

		# create output file
    fout = open(fileName, "w+")
    fout.write("<html>")
    fout.write("<head>")
    fout.write("<title>Test Results</title>")
    fout.write("</head>")
    fout.write("<body>")
    fout.write("<p>")
    fout.write("Results for " + str(numCases) + " test case(s)")
    fout.write("<br>")
    fout.write("<br>")

    return fout

# adds test results to the output file
def addTestResult(testCaseInfo, result, outputFile):
    outputFile.write('<HR WIDTH="500px" ALIGN="LEFT" SIZE="3">')
    outputFile.write("<b>Test Name:</b> " + testCaseInfo[0] + "<br/>")
    outputFile.write("<b>Requirement:</b> " + testCaseInfo[1] + "<br/>")
    outputFile.write("<b>Component:</b> " + testCaseInfo[2] + "<br/>")
    outputFile.write("<b>Method:</b> " + testCaseInfo[3] + "<br/>")
    outputFile.write("<b>Input(s):</b> " + testCaseInfo[4] + "<br/>")
    outputFile.write("<b>Expected Outcome:</b> " + testCaseInfo[5] + "<br/>")
    outputFile.write("<b>Test Result:</b> " + result + "<br/>")
    outputFile.write("<br/>")

# closes the report
def closeReport(fileName):
    fileName.write("</p>")
    fileName.write("</body>")
    fileName.write("</html>")
    fileName.close()


if __name__ == '__main__':

    # stores the names of the test cases in testCases
    testCases = getFiles('testCases')
    testCases.sort()
    #print testCases
    os.chdir('reports')

		#initialize the output file
    fout = initializeReport("testOutput.html", len(testCases))

    os.chdir('../testCases')
    # loop for testing each test case
    for test in testCases:
        # lines stores each line of a single test case
        lines = parse(test)

        os.chdir('../testCasesExecutables')

        # check_output runs the test lines[0].py with input lines[4] and stores output in testOut 
        testOut = subprocess.check_output([sys.executable, lines[0] + ".py", lines[4]])
        
				# add results to the report
        addTestResult(lines, testOut, fout)

        os.chdir('../testCases')

    # close report
    closeReport(fout)
    os.chdir('../reports')

		# open report in browser
    webbrowser.open('file://' + os.path.realpath("testOutput.html"))

