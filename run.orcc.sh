#!/bin/bash
source `dirname $0`/defines.sh

[ ! -d "$2" ] && echo "Second argument must be a directory with Orcc projects as subfolders" && exit 1
[ -z "$3" ] && echo "Third argument must be the backend you want to use" && exit 1
[ -z "$4" ] && echo "Fourth argument must be the project where is located your top network" && exit 1
[ -z "$5" ] && echo "Fifth argument must be the qualified name of the top network" && exit 1
[ -z "$6" ] && echo "Sixth argument must be the directory you want to build sources" && exit 1

APPDIR=$2
BACKEND=$3
PROJECT=$4
NETWORK=$5
OUTPUT=$6
FLAGS=$7

echo "***START*** $0 `date -R`"

[ ! -d "$OUTPUT" ] && mkdir -p $OUTPUT

RUNWORKSPACE=$APPDIR
rm -fr $RUNWORKSPACE/.metadata $RUNWORKSPACE/.JETEmitters 
rm -fr $RUNWORKSPACE/**/bin

echo "Register Orcc projects in eclipse workspace"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.cal.workspaceSetup \
                        -data $RUNWORKSPACE \
                        $APPDIR

[ "$?" != "0" ] && exit 1


# Frontend will generate IR only for used files. But all IR must be generated for jade and java backend
if [ "$BACKEND" != "jade" ] && [ "$BACKEND" != "java" ]; then
    FENETWORK=$NETWORK
fi

echo ""
echo "Generate Orcc IR for $PROJECT and projects it depends on"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.cal.cli \
                        -data $RUNWORKSPACE \
                        $PROJECT \
                        $FENETWORK \
                        -vmargs -Xms40m -Xmx768m

[ "$?" != "0" ] && exit 1

rm -fr $OUTPUT/*

echo ""
echo "Build application with $BACKEND backend"
$ECLIPSERUN/eclipse     -nosplash -consoleLog \
                        -application net.sf.orcc.backends.$BACKEND \
                        -data $RUNWORKSPACE \
                        -p $PROJECT \
                        -o $OUTPUT \
                        $FLAGS \
                        $NETWORK \
                        -vmargs -Xms40m -Xmx768m

[ "$?" != "0" ] && exit 1

echo "***END*** $0 `date -R`"
