#!/bin/bash
source `dirname $0`/defines.sh

BUILDDEPS=org.eclipse.pde.feature.group,org.eclipse.emf.sdk.feature.group,org.eclipse.xtext.sdk.feature.group,org.eclipse.gef.feature.group
ECLIPSEARCHIVE=eclipse-platform-4.2-linux-gtk-x86_64.tar.gz

mkdir -p $ORCCWORK

rm -fr $ECLIPSERUN
rm -fr $ECLIPSEBUILD

mkdir $ECLIPSERUN
mkdir $ECLIPSEBUILD

tar -xzaf $ECLIPSEARCHIVE
cp -r eclipse/* $ECLIPSERUN
cp -r eclipse/* $ECLIPSEBUILD

rm -rf eclipse

cd $ORCCWORK
$ECLIPSEBUILD/eclipse 	-nosplash -consoleLog \
						-application org.eclipse.equinox.p2.director \
						-destination $ECLIPSEBUILD \
						-repository $ECLIPSEREPOSITORY \
						-followReferences \
						-installIU $BUILDDEPS

exit 0
