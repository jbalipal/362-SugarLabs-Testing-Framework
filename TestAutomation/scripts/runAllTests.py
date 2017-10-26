#!/usr/bin/python

import sys
import os
import subprocess
import webbrowser
from scriptFunct import * 

if __name__ == '__main__':

    # clean temp directory for individual test results
    cleanDir('temp')

    # stores the names of the test cases in testCases
    testCases = getFiles('testCases')
    testCases.sort()

    os.chdir('testCases')
    # loop for testing each test case
    for test in testCases:
        # lines stores each line of a single test case
        lines = parse(test)

        os.chdir('../testCasesExecutables')

        # check_output runs the test lines[0].py with input lines[4] and stores output in testOut 
        testOut = subprocess.check_output([sys.executable, lines[0] + ".py", lines[4], lines[5]])
        
        # create individual test result
        os.chdir('../temp')
        makeTestResult(lines, testOut, test[:-4]+"Result.txt")

        os.chdir('../testCases')

    # create output file for all results
    #fout = initializeReport("testOutput.html", len(testCases))
    makeReport("testOutput.html", len(testCases))

    # open report in browser
    webbrowser.open('file://' + os.path.realpath("testOutput.html"))

