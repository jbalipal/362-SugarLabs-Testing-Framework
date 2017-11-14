# helper methods for runAllTests.py

import sys
import os

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

# clean directory
def cleanDir(dirName):
    dirFiles = getFiles(dirName)
    os.chdir(dirName)
    for f in dirFiles:
        os.remove(f)
    os.chdir('..')

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
    fout.write("<table border = 1>")
    fout.write("<tr><th>Test No.</th><th>Test Name</th><th>Requirement</th><th>Component</th><th>Method</th><th>Inputs</th><th>Expected Outputs</th><th>Test Result</th></tr>")

    return fout

# adds test results to the output file
def makeTestResult(testCaseInfo, result, outputFile, testNum):
    f = open(outputFile, "w+")
    
    f.write("<tr>")
    f.write("<td>" + str(testNum) + "</td>")
    f.write("<td>" + testCaseInfo[0] + "</td>")
    f.write("<td>" + testCaseInfo[1] + "</td>")
    f.write("<td>" + testCaseInfo[2] + "</td>")
    f.write("<td>" + testCaseInfo[3] + "</td>")
    f.write("<td>" + testCaseInfo[4] + "</td>")
    f.write("<td>" + testCaseInfo[5] + "</td>")
    f.write("<td>" + result + "</td>")
    f.write("</tr")
    f.write("</br>")
    f.close()

# create test report 
def makeReport(outputFile, numCases):
    os.chdir('../reports')
    fout = initializeReport(outputFile, numCases)
    os.chdir('..')
    results = getFiles('temp')
    results.sort()
    os.chdir('temp')

    for individualResult in results:
        with open(individualResult) as infile:
            fout.write(infile.read())
    os.chdir('../reports')
    closeReport(fout)

# closes the report
def closeReport(fileName):
    fileName.write("</p>")
    fileName.write("</body>")
    fileName.write("</html>")
    fileName.close()

