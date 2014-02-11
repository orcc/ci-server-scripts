#!/usr/bin/python
'''
Copyright (c) 2014, IETR/INSA of Rennes
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  * Neither the name of the IETR/INSA of Rennes nor the names of its
    contributors may be used to endorse or promote products derived from this
    software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
'''

import argparse
import subprocess
import os, sys

VERSION = "0.3"

def main():
    clArguments = parser.parse_args()

    errorsCount = 0
    warningsCount = 0

    # Check validity of "sequences" directory
    if not os.path.isdir(clArguments.sequences):
        sys.exit("The sequence path must be a valid directory, containing sequences")

    if clArguments.quickTest:
        fileList = fileList_reduce
    else:
        fileList = fileList_all

    if not fileList.has_key(clArguments.filesKey) :
       clArguments.filesKey = DEFAULT_FILE_LIST

    for file in fileList[clArguments.filesKey]:
        file = file.replace("/", os.sep)
        inputFile = file
        outputFile = '.'.join(file.split('.')[:-1]) + ".yuv"

        inputPath = clArguments.sequences + os.sep + inputFile
        outputPath = clArguments.sequences + os.sep + outputFile

        if not os.path.exists(inputPath):
            print "Warning : input file", inputPath, "does not exists"
            warningsCount += 1
            continue
        elif not os.access(inputPath, os.R_OK):
            print "Warning : input file", inputPath, "is not readable"
            warningsCount += 1
            continue

        if not clArguments.skipYuv:
            if not os.path.exists(outputPath):
                print "Warning : output file", outputPath, "does not exists"
                warningsCount += 1
                continue
            elif not os.access(outputPath, os.R_OK):
                print "Warning : output file", outputPath, "is not readable"
                warningsCount += 1
                continue

        finalCommandLine = buildBasicCommand()

        finalCommandLine.extend(["-i", inputPath])

        traceMsg = "Try to decode " + inputFile

        if not clArguments.skipYuv:
            finalCommandLine.extend(["-o", outputPath])
            traceMsg += " and check consistency with " + outputFile + ":"

        if clArguments.verbose:
            print " ".join(finalCommandLine)

        print traceMsg
        commandResult = subprocess.call(finalCommandLine)

        if commandResult != 0:
            sys.stderr.write("Error, command returned code " + str(commandResult))
            errorsCount += 1

    if errorsCount != 0:
        ws, es = "", ""
        if errorsCount > 1 : es = "s"
        if warningsCount > 1 : ws = "s"
        sys.exit("The test suite finished with " + str(errorsCount) + " error"+es+" and " + str(warningsCount) + " warning"+ws+".")
    elif warningsCount != 0:
        s = ""
        if warningsCount > 1 : s = "s"
        print "The test suite finished with no error but", warningsCount, "warning"+s+"."
        sys.exit()
    else :
        print "The test suite finished with no error !"
        sys.exit()

def buildBasicCommand():
    args = parser.parse_args()
    commandToRun = []

    # Build the command line for Jade execution
    if args.useJade :
        if args.topXdf == None or not os.path.isfile(args.topXdf):
            sys.exit("Please use -xdf argument to set the path of a top network")
        elif args.vtl == None or not os.path.isdir(args.vtl):
            sys.exit("Please use -vtl argument to set the path of a VTL folder")
        else:
            if args.executable != None:
                commandToRun.append(args.executable)
            else:
                commandToRun.append("Jade")
            commandToRun.extend(["-xdf", args.topXdf, "-L", args.vtl])

        if args.loopNumber != None:
            print "Warning : By default, Jade read only one time the input file. The -l value you passed will be ignored."

        if not args.enableDisplay:
            commandToRun.append("-nodisplay")

    # Build the command line for standalone decoder
    elif args.useClassic:
        if args.executable == None:
            sys.exit("Please use -e argument to set the path of a decoder")
        elif not os.path.isfile(args.executable) or not os.access(args.executable, os.X_OK):
            sys.exit(args.executable + " must be an executable file !")
        else:
            commandToRun.append(args.executable)

        # Set the max loops number
        if args.loopNumber != None:
            commandToRun.extend(["-l", str(args.loopNumber)])

        # Disable display
        if not args.enableDisplay:
            commandToRun.append("-n")

    return commandToRun


def configureCommandLine():
    # Help on arparse usage module : http://docs.python.org/library/argparse.html#module-argparse
    global parser

    parser = argparse.ArgumentParser(description='Test a suite of video sequences', version=VERSION)

    expected = parser.add_argument_group(title="Mandatory arguments")
    expected.add_argument("-e", "--executable", action="store", dest="executable", required=True,
                        help="")

    expected.add_argument("-d", "--directory", action="store", dest="directory", required=True,
                        help="Path to directory containing sequences (ie: containing folder like HEVC/AVC/etc.)")

    expected.add_argument("-i", "--inputList", action="store", dest="inputList", required=True,
                        help="Path to the file containing list of sequences to decode")

    optional = parser.add_argument_group(title="Other options")
    optional.add_argument("--check-yuv", action="store_true", dest="checkYuv", default=False,
                        help="Search for YUV files corresponding to sequence, and check the consistency of each frame")
    optional.add_argument("--no-nb-frames", action="store_true", dest="verbose", default=False,
                        help="Set tu true if you don't want to pass the number of frames to decode")
    optional.add_argument("--verbose", action="store_true", dest="verbose", default=False, help="Verbose mode")


if __name__ == "__main__":
    configureCommandLine()
    main()
