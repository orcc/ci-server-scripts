#!/bin/bash
source `dirname $0`/defines.sh

[ ! -d "$2" ] && echo "Second argument must be a directory with Orcc projects as subfolders" && exit 1
[ -z "$3" ] && echo "Third argument must be the backend you want to use" && exit 1
[ -z "$4" ] && echo "Fourth argument must be the project where is located your top network" && exit 1
[ -z "$5" ] && echo "Fifth argument must be the qualified name of the top network" && exit 1
[ ! -d "$6" ] && echo "Sixth argument must be the directory you want to build sources" && exit 1
APPDIR=$2
BACKEND=$3
PROJECT=$4
NETWORK=$5
OUTPUT=$6
FLAGS=$7

RUNWORKSPACE=$ORCCWORK/workspace
mkdir -p $RUNWORKSPACE

echo "Register Orcc projects in eclipse workspace"
$ECLIPSERUN/eclipse 	-nosplash -consoleLog \
						-application net.sf.orcc.cal.workspaceSetup \
						-data $RUNWORKSPACE \
						$APPDIR

echo "Generate Orcc IR for $PROJECT and projects it depends on"
$ECLIPSERUN/eclipse 	-nosplash -consoleLog \
						-application net.sf.orcc.cal.cli \
						-data $RUNWORKSPACE \
						$PROJECT \
						-vmargs -Xms40m -Xmx768m

echo "Build application with $BACKEND backend"
$ECLIPSERUN/eclipse 	-nosplash -consoleLog \
						-application net.sf.orcc.backends.$BACKEND \
						-data $RUNWORKSPACE \
						-p $PROJECT \
						-o $OUTPUT \
						$FLAGS \
						$NETWORK \
						-vmargs -Xms40m -Xmx768m

exit 0
