#!/bin/bash

# exits when a command returned non 0 value
set -e
export E_BADARGS=64

[ ! -d "$1" ] && mkdir $1
[ -z "$BUILDTYPE" ] && export BUILDTYPE="tests" && echo "Variable BUILDTYPE has not been set. Initialized to \"tests\""

export ORCCWORK="$1"

ECLIPSEVERSION=kepler
# Used to download the base platform version of eclipse
export ECLIPSEURL="http://eclipse.ialto.com/eclipse/downloads/drops4/R-4.3-201306052000/eclipse-platform-4.3-linux-gtk-x86_64.tar.gz"
# Used to download dependencies (both runtime and build eclipse)
export ECLIPSEREPOSITORY=http://download.eclipse.org/releases/$ECLIPSEVERSION

export ECLIPSERUN=$ORCCWORK/eclipse.runtime
export ECLIPSEBUILD=$ORCCWORK/eclipse.build

export BUILDDIR=$ORCCWORK/build.dir.$BUILDTYPE
export PLUGINSDIR=$BUILDDIR/plugins
export FEATURESDIR=$BUILDDIR/features

# Get the path of the current script. This script is necessary to resolve symlinks to this script
# see http://stackoverflow.com/a/246128/1887976
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
# Create symlinks to antlr jar library and PDE headless build config directory
ln -f -s $DIR/pde-config $ORCCWORK
ln -f -s $DIR/*.jar $ORCCWORK

# Setup eclipse classpath
ECLIPSECP=$(echo $ECLIPSEBUILD/plugins/*.jar | sed -e "s/ /:/g")

# Setup Xtext MWE2 classpath
MWECP=$ECLIPSECP:$(echo $ORCCWORK/antlr-generator-*.jar | sed -e "s/ /:/g")
MWECP=$MWECP:$PLUGINSDIR/net.sf.orcc.cal/src:$PLUGINSDIR/net.sf.orcc.cal.ui/src
export MWECP

# Setup Xtend classpath
XTENDCP=$ECLIPSECP:$PLUGINSDIR/org.jgrapht
for i in $(ls $PLUGINSDIR 2>/dev/null)
do
    [ -d "$PLUGINSDIR/$i/src" ] && XTENDCP=$XTENDCP:$PLUGINSDIR/$i/src
    [ -d "$PLUGINSDIR/$i/src-gen" ] && XTENDCP=$XTENDCP:$PLUGINSDIR/$i/src-gen
done
export XTENDCP
