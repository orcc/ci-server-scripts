#!/bin/bash
source `dirname $0`/defines.sh

[ ! -s "$2" ] && echo "Second argument must be a directory with Orcc projects as subfolders" && exit 1
[ -z "$3" ] && echo "Third argument must be the project where is located your top network" && exit 1
[ -z "$4" ] && echo "Fourth argument must be the qualified name of the top network" && exit 1
[ ! -s "$5" ] && echo "Fifth argument must be the input stimulus of simulation" && exit 1
[ -f "$6" ] && REFOPTION="-r $6"

APPDIR=$2
PROJECT=$3
NETWORK=$4
INPUT=$5

# Split 2 test to perform a "short circuit evaluation"
[ "$FIFOSIZE" -ge 2 ] 2>/dev/null && SETFIFO="-s $FIFOSIZE" && echo "Fifo size set to $FIFOSIZE"

echo "***START*** $0 `date -R`"

RUNWORKSPACE=$APPDIR
rm -fr $RUNWORKSPACE/.metadata $RUNWORKSPACE/.JETEmitters 
rm -fr $RUNWORKSPACE/**/bin

echo "Register Orcc projects in eclipse workspace"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.cal.workspaceSetup \
                        -data $RUNWORKSPACE \
                        $APPDIR

[ "$?" != "0" ] && exit 1

echo "Generate Orcc IR for $PROJECT and projects it depends on"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.cal.cli \
                        -data $RUNWORKSPACE \
                        $PROJECT \
                        $NETWORK \
                        -vmargs -Xms40m -Xmx768m

[ "$?" != "0" ] && exit 1

echo "Run simulation"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.simulators.cli \
                        -data $RUNWORKSPACE \
                        -n \
                        -i $INPUT \
                        -p $PROJECT \
                        $SETFIFO \
                        $REFOPTION \
                        $NETWORK \
                        -vmargs -Xms40m -Xmx1024m

[ "$?" != "0" ] && exit 1

echo "***END*** $0 `date -R`"
