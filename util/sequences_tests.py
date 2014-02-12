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

from __future__ import print_function
import os, sys, re, signal
import argparse, subprocess, csv

VERSION = "0.3"

PATH='path'
FRAMES='nbFrames'
SIZE='size'

def main():
    args = parser.parse_args()

    errorsCount = 0
    warningsCount = 0

    fileList = parseSequencesList()

    finalCommandLine = buildCommand()

    for sequence in fileList:

        if not os.path.exists(sequence[PATH]):
            warning("input file", sequence[PATH], "does not exists")
            warningsCount += 1
            continue
        elif not os.access(sequence[PATH], os.R_OK):
            warning("input file", sequence[PATH], "is not readable")
            warningsCount += 1
            continue

        finalCommandLine.extend(["-i", sequence[PATH]])

        if args.checkYuv:
            yuvPath = getYUVFile(sequence[PATH])
            if not os.path.exists(yuvPath):
                warning("YUV file", yuvPath, "does not exists")
                warningsCount += 1
                continue
            elif not os.access(yuvPath, os.R_OK):
                warning("YUV file", yuvPath, "is not readable")
                warningsCount += 1
                continue
            finalCommandLine.extend(["-o", yuvPath])

        if not args.noNbFrames:
            finalCommandLine.extend(["-f", sequence[FRAMES]])

        traceMsg = "Try to decode " + sequence[PATH]
        if args.checkYuv:
            traceMsg += " / check with YUV " + outputFile + ":"

        if args.verbose:
            print("Command: ", ' '.join(finalCommandLine))

        print(traceMsg)
        commandResult = subprocess.call(finalCommandLine)

        if commandResult != 0:
            sys.stderr.write("Error, command returned code " + str(commandResult))
            errorsCount += 1
    # endfor

    if errorsCount != 0:
        ws, es = "", ""
        if errorsCount > 1 : es = "s"
        if warningsCount > 1 : ws = "s"
        sys.exit("The test suite finished with " + str(errorsCount) + " error"+es+" and " + str(warningsCount) + " warning"+ws+".")
    elif warningsCount != 0:
        s = ""
        if warningsCount > 1 : s = "s"
        warning("The test suite finished with no error but", warningsCount, "warning"+s+".")
    else :
        print("The test suite finished with no error !")

def buildCommand():
    args = parser.parse_args()
    commandToRun = [args.executable]

    if args.options:
        commandToRun.append(args.options)

    return commandToRun

# Parse the inputList given in argument, and extract information about videos
def parseSequencesList():
    args = parser.parse_args()

    patternString = None
    if args.regexp:
        patternString = args.regexp
    elif args.filter:
        patternString = args.filter.replace('.', '\.')
        patternString = patternString.replace('?', '.')
        patternString = patternString.replace('*', '(.+)')

    if patternString:
        pattern = re.compile(patternString)
    else:
        pattern = None

    cptEntries = 0
    cptFiltered = 0

    result = []
    with open(args.inputList, 'rb') as csvfile:
        # Reader ignores lines starting with '#', and compute automatically values in a
        # dictionary indexed by (PATH, FRAMES, SIZE)
        entries = csv.DictReader(
            (row for row in csvfile if not row.startswith('#')),
            fieldnames=(PATH, FRAMES, SIZE),
            skipinitialspace=True, delimiter=',')
        for sequenceEntry in entries:
            cptEntries += 1
            if pattern:
                if pattern.match(sequenceEntry[PATH]):
                    result.append(sequenceEntry)
                    cptFiltered += 1
                else:
                    continue
            else:
                result.append(sequenceEntry)

    if args.verbose:
        print(cptEntries, "sequences found in", args.inputList)
        if pattern:
            print(len(result), "selected by '"+pattern.pattern+"'")
    return result

# Replace the suffix of a path by the 'yuv' extension. Returns the resulting YUV path
def getYUVFile(sequencePath):
    return '.'.join(sequencePath.split('.')[:-1]) + ".yuv"

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
    optional.add_argument("-f", "--filter", action="store", dest="filter",
                        help="Filter fileList entries with a wildcard")
    optional.add_argument("--options", action="store", dest="options",
                        help="Additional options to append to the executable command line")
    optional.add_argument("-re", "--regexp", action="store", dest="regexp",
                        help="Same as filter, but use classic regexp instead")
    optional.add_argument("--check-yuv", action="store_true", dest="checkYuv", default=False,
                        help="Search for YUV files corresponding to sequence, and check the consistency of each frame")
    optional.add_argument("--no-nb-frames", action="store_true", dest="noNbFrames", default=False,
                        help="Set tu true if you don't want to pass the number of frames to decode")
    optional.add_argument("--verbose", action="store_true", dest="verbose", default=False, help="Verbose mode")

    # Perform some control on arguments passed by user
    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        sys.exit("--directory option must contain the path to a valid directory")

    if not os.path.exists(args.inputList):
        sys.exit("Error: file " + args.inputList + " not found !")

def warning(*objs):
    print("WARNING: ", *objs, end='\n', file=sys.stderr)

def handler(type, frame):
    if type == signal.SIGINT:
        sys.exit("The test suite has been interrupted !")
    elif type == signal.SIGABRT:
        sys.exit("The test suite has been aborted !")
    else:
        sys.exit("Unknown signal catched: " + str(type))
if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGABRT, handler)
    configureCommandLine()
    main()
