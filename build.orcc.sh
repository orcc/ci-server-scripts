#!/bin/bash

NBARGS=3
function print_usage() {
    echo
    echo "Usage: $0 <working_directory> <feature_dir> <plugin_dir>"
    echo "    <working_directory>           Path to folder used to perform build & tests"
    echo "    <feature_dir>                 Path to eclipse feature folder"
    echo "    <plugin_dir>                  Path(s) to folder(s) containing eclipse plugins directories"
}

if [ $# -lt $NBARGS ]; then
    print_usage
    exit $E_BADARGS
fi

[ ! -d "$2" ] && echo "Missing features directory" && print_usage && exit $E_BADARGS
[ ! -d "$3" ] && echo "Missing plugins directory" && print_usage && exit $E_BADARGS

source `dirname $0`/defines.sh

SOURCEFEATUREDIR=$2

echo "***START*** `date -R` Build type: $BUILDTYPE"
rm -fr $BUILDDIR
mkdir -p $PLUGINSDIR
mkdir -p $FEATURESDIR/net.sf.orcc

cp -ur $SOURCEFEATUREDIR/* $FEATURESDIR/net.sf.orcc

# Remove the 2 first arg from command line
shift 2
# Loop over resulting cli arguments
for arg; do
    cp -ur $arg/* $PLUGINSDIR
done

echo ""
echo "****************************************************************"
echo "*             Generate Cal Xtext arcitecture                   *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.cal
java -cp $MWECP org.eclipse.emf.mwe2.launch.runtime.Mwe2Launcher src/net/sf/orcc/cal/GenerateCal.mwe2

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "* Generate Java sources from Xtend [net.sf.orcc.backends]      *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.backends
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*  Generate Java sources from Xtend [net.sf.orcc.models]       *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.models
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*    Generate Java sources from Xtend [net.sf.orcc.core]       *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.core
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*    Generate Java sources from Xtend [net.sf.orcc.simulators] *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.simulators
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen ../net.sf.orcc.core/xtend-gen:src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*    Generate Java sources from Xtend [net.sf.orcc.ui]         *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/net.sf.orcc.ui
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*   Generate Java sources from Xtend [org.xronos.orcc]         *"
echo "****************************************************************"
echo ""
cd $PLUGINSDIR/org.xronos.orcc
rm -fr xtend-gen/*
java -cp $XTENDCP org.eclipse.xtend.core.compiler.batch.Main -cp $XTENDCP -d xtend-gen ../net.sf.orcc.backends/xtend-gen:src

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*                    Launch PDE Build                          *"
echo "****************************************************************"
echo ""

# Define PDE build specific variables
LAUNCHERJAR=`echo $ECLIPSEBUILD/plugins/org.eclipse.equinox.launcher_*.jar`
BUILDFILE=`echo $ECLIPSEBUILD/plugins/org.eclipse.pde.build_*`/scripts/build.xml
CONFIGDIR=$ORCCWORK/pde-config
KEEPONLYLATESTVERSIONS=true # Set to false when a Release build will be defined
LOCALREPO=$ORCCWORK/repository.$BUILDTYPE

if [ "$BUILDTYPE" == "tests" ]
then
    PDEBUILDTYPE=I
elif [ "$BUILDTYPE" == "nightly" ]
then
    PDEBUILDTYPE=N
else
    PDEBUILDTYPE=R
fi

mkdir -p $LOCALREPO
mkdir -p $BUILDDIR

$ECLIPSEBUILD/eclipse   -nosplash -consoleLog \
                        -application org.eclipse.ant.core.antRunner \
                        -buildfile $BUILDFILE \
                        -Dbuilder=$CONFIGDIR \
                        -DbaseLocation=$ECLIPSEBUILD \
                        -DpluginPath=$ECLIPSEBUILD:$BUILDDIR \
                        -DbuildType=$PDEBUILDTYPE \
                        -DtopLevelElementId=net.sf.orcc \
                        -DbuildDirectory=$BUILDDIR \
                        -Dbase=$BUILDDIR \
                        -Dp2.mirror.slicing.latestVersionOnly=$KEEPONLYLATESTVERSIONS \
                        -Dp2.build.repo=file:$LOCALREPO

[ "$?" != "0" ] && exit 1

echo ""
echo "****************************************************************"
echo "*       Installing Orcc plugins on eclipse runtime             *"
echo "****************************************************************"
echo ""
echo "Uninstall old Orcc feature"

$ECLIPSEBUILD/eclipse   -nosplash -consoleLog \
                        -application org.eclipse.equinox.p2.director \
                        -destination $ECLIPSERUN \
                        -uninstallIU net.sf.orcc.feature.group \
|| echo -e "\n*** There is no existing Orcc feature to uninstall. This is probably the first time this script is \
launched since last eclipse reinstall. Please ignore the previous error message. ***"

echo "Install new Orcc feature"
$ECLIPSEBUILD/eclipse   -nosplash -consoleLog \
                        -application org.eclipse.equinox.p2.director \
                        -destination $ECLIPSERUN \
                        -artifactRepository file:$LOCALREPO \
                        -metadataRepository file:$LOCALREPO \
                        -repository $ECLIPSEREPOSITORY \
                        -installIU net.sf.orcc.feature.group

[ "$?" != "0" ] && exit 1

echo "***END*** $0 `date -R`"
