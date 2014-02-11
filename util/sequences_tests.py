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
import os
import sys

VERSION = "0.3"

def main():
    clArguments = parser.parse_args()

    #print clArguments
    #sys.exit(0)

    errorsCount = 0
    warningsCount = 0

    execPath = []

    # Build the command line for Jade execution
    if clArguments.useJade :
        if clArguments.topXdf == None or not os.path.isfile(clArguments.topXdf):
            sys.exit("Please use -xdf argument to set the path of a top network")
        elif clArguments.vtl == None or not os.path.isdir(clArguments.vtl):
            sys.exit("Please use -vtl argument to set the path of a VTL folder")
        else:
            if clArguments.executable != None:
                execPath.append(clArguments.executable)
            else:
                execPath.append("Jade")
            execPath.extend(["-xdf", clArguments.topXdf, "-L", clArguments.vtl])

        if clArguments.loopNumber != None:
            print "Warning : By default, Jade read only one time the input file. The -l value you passed will be ignored."

        if not clArguments.enableDisplay:
            execPath.append("-nodisplay")

    # Build the command line for standalone decoder
    elif clArguments.useClassic:
        if clArguments.executable == None:
            sys.exit("Please use -e argument to set the path of a decoder")
        elif not os.path.isfile(clArguments.executable) or not os.access(clArguments.executable, os.X_OK):
            sys.exit(clArguments.executable + " must be an executable file !")
        else:
            execPath.append(clArguments.executable)

        # Set the max loops number
        if clArguments.loopNumber != None:
            execPath.extend(["-l", str(clArguments.loopNumber)])

        # Disable display
        if not clArguments.enableDisplay:
            execPath.append("-n")

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

        finalCommandLine = list(execPath)

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


def setupCommandLine():
    # Help on arparse usage module : http://docs.python.org/library/argparse.html#module-argparse
    global parser

    parser = argparse.ArgumentParser(description='Execute parser to test video decoding', version=VERSION)

    options = parser.add_argument_group(title="Parameters")

    mode = options.add_mutually_exclusive_group(required=True)
    mode.add_argument("-jade", action="store_true", default=False, dest="useJade")
    mode.add_argument("-classic", action="store_true", default=False, dest="useClassic")

    jade = parser.add_argument_group("Parameters for -jade mode", "Test a decoder in LLVM with Jade toolchain")
    jade.add_argument("-xdf", action="store", dest="topXdf",
                            help="Path to the Top_*.xdf network of the decoder")
    jade.add_argument("-vtl", action="store", dest="vtl",
                            help="Path to the VTL directory of the decoder")

    classic = parser.add_argument_group("Parameters for -classic mode", "Test a classic C decoder")
    classic.add_argument("-l", "--loops", type=int, action="store", dest="loopNumber",
                        help="Number of times input is read for every file")

    options.add_argument("-e", "--executable", action="store", dest="executable",
                        help="In -classic mode, path to a decoder. In -jade mode, path to Jade executable.")
    options.add_argument("-s", "--sequences", action="store", dest="sequences", required=True,
                        help="Path to directory containing sequences (ie : containing MPEG4/AVC/etc. folder).")
    options.add_argument("-n", "--nodisplay", action="store_false", dest="enableDisplay", default=True,
                        help="Pass this argument to disable display when testing decoders.")
    options.add_argument("-f", "--filestypes", choices=["mpeg","avc","hevc","hevcIntra", "hevcConf"], default=DEFAULT_FILE_LIST, dest="filesKey",
                        help="Set the type of videos to test (default='"+DEFAULT_FILE_LIST+"')")
    options.add_argument("-q", "--quick", action="store_true", dest="quickTest", default=False,
                        help="Test the decoder on a small subset of sequences.")
    options.add_argument("--skip-yuv", action="store_true", dest="skipYuv", default=False,
                        help="Skip the consistency checking using the YUV file.")
    options.add_argument("--verbose", action="store_true", dest="verbose", default=False,
                        help="Verbose mode.")


if __name__ == "__main__":
    setupCommandLine()
    computeFileList()
    main()
