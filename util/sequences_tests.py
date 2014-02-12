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
    global args

    errorsCount = 0
    warningsCount = 0

    fileList = parseSequencesList()

    finalCommandLine = buildCommand()

    for sequence in fileList:

        inputFile = sequence[PATH]
        if not os.path.exists(inputFile):
            warning("input file", inputFile, "does not exists")
            warningsCount += 1
            continue
        elif not os.access(inputFile, os.R_OK):
            warning("input file", inputFile, "is not readable")
            warningsCount += 1
            continue

        finalCommandLine.extend(["-i", inputFile])

        if args.checkYuv:
            yuvFile = getYUVFile(inputFile)
            if not os.path.exists(yuvFile):
                warning("YUV file", yuvFile, "does not exists")
                warningsCount += 1
                continue
            elif not os.access(yuvFile, os.R_OK):
                warning("YUV file", yuvFile, "is not readable")
                warningsCount += 1
                continue
            finalCommandLine.extend(["-o", yuvFile])

        # Stop decoding when all frames have been processed
        if not args.noNbFrames:
            if sequence[FRAMES]:
                finalCommandLine.extend(["-f", sequence[FRAMES]])
            else:
                finalCommandLine.extend(["-l", '1'])
                warning("Input list doesn't containes the number of frame for "+inputFile+"\n"+
                    "As fallback, '-l 1' has been added to the command line.")

        traceMsg = "Try to decode " + inputFile
        if args.checkYuv:
            traceMsg += " / check with YUV " + yuvFile

        if args.verbose:
            traceMsg += " with command \n" + ' '.join(finalCommandLine)

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
    global args
    global additional_args
    commandToRun = [args.executable]

    if additional_args:
        # User used -args to add command line arguments
        commandToRun.append(' '.join(additional_args))

    return commandToRun

# Parse the inputList given in argument, and extract information about videos
def parseSequencesList():
    global args

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
            if pattern and not pattern.match(sequenceEntry[PATH]):
                continue

            cptFiltered += 1
            if args.directory:
                sequenceEntry[PATH] = args.directory + os.sep + sequenceEntry[PATH]

            sequenceEntry[PATH] = sequenceEntry[PATH].replace('/', os.sep)
            result.append(sequenceEntry)
        #endfor

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

    parser = argparse.ArgumentParser(add_help=False,
        description='Test a list of video sequences. All unrecognized arguments given to this script will be used when on EXECUTABLE command line')

    mandatory = parser.add_argument_group(title="Mandatory arguments")
    mandatory.add_argument("-e", "--executable", action="store", dest="executable", required=True,
                        help="Main executable to run")
    mandatory.add_argument("-i", "--inputList", action="store", dest="inputList", required=True,
                        help="Path to the file containing list of sequences to decode")

    optional = parser.add_argument_group(title="Other options")
    filtering = optional.add_mutually_exclusive_group(required=False)
    filtering.add_argument("-f", "--filter", action="store", dest="filter",
                        help="Filter INPUTLIST entries with a wildcard (ex: '*qp28*'")
    filtering.add_argument("-re", "--regexp", action="store", dest="regexp",
                        help="Same as --filter, but use classic regexp instead")

    optional.add_argument("-d", "--directory", action="store", dest="directory",
                        help="Path to directory containing sequences. If INPUTLIST contains relative paths, you must set this variable to the root directory they are relative to.")
    optional.add_argument("--check-yuv", action="store_true", dest="checkYuv", default=False,
                        help="Search for a reference YUV file corresponding to each sequence, and check its consistency while decoding")
    optional.add_argument("--no-nb-frames", action="store_true", dest="noNbFrames", default=False,
                        help="Set to true if you don't want to limit the number of frames to decode")
    optional.add_argument("--verbose", action="store_true", dest="verbose", default=False, help="Verbose mode")

    optional.add_argument('-v', "--version", action="version", version= "%(prog)s " + VERSION, help="Print the current version of this script")
    optional.add_argument('-h', "--help", action="help", help="Display this message")

    # parse_known_args() will return a tuple (<known_args> as Namespace, <unknown_args> as List)
    parsed_args = parser.parse_known_args()

    # Perform some control on arguments passed by user
    if not os.path.isdir(parsed_args[0].directory):
        sys.exit("--directory option must contain the path to a valid directory")

    if not os.path.exists(parsed_args[0].inputList):
        sys.exit("Error: file " + parsed_args[0].inputList + " not found!")

    if not os.path.exists(parsed_args[0].executable):
        sys.exit("Error: executable file " + parsed_args[0].executable + " not found!")
    elif not os.access(inputFile, os.X_OK):
        sys.exit("Error: file " + parsed_args[0].executable + " is not executable ! Please check its mode.")

    return parsed_args

def warning(*objs):
    print("WARNING:", *objs, end='\n', file=sys.stderr)

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

    parsed_args = configureCommandLine()
    args = parsed_args[0]
    additional_args = parsed_args[1]

    main()
