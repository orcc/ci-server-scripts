#!/bin/bash
source `dirname $0`/defines.sh

echo "***START*** $0 `date -R`"

ECLIPSEURL="http://eclipse.ialto.com/eclipse/downloads/drops4/R-4.3-201306052000/eclipse-platform-4.3-linux-gtk-x86_64.tar.gz"

BUILDDEPS="org.eclipse.pde.feature.group,org.eclipse.emf.sdk.feature.group,org.eclipse.xtext.sdk.feature.group,org.eclipse.gef.feature.group"

mkdir -p $ORCCWORK

rm -fr $ECLIPSERUN
rm -fr $ECLIPSEBUILD

mkdir $ECLIPSERUN
mkdir $ECLIPSEBUILD

echo "Downloading Eclipse"
wget --progress=dot:mega $ECLIPSEURL

ECLIPSEARCHIVE=`echo eclipse-platform-*.tar.gz`

echo "Uncompressing"
tar -xzaf $ECLIPSEARCHIVE

echo "Update java max heap size"
sed -i -e "s/-Xmx384m/-Xmx512m/g" eclipse/eclipse.ini

echo "Copying eclipse/* into $ECLIPSERUN and $ECLIPSEBUILD"
cp -r eclipse/* $ECLIPSERUN
cp -r eclipse/* $ECLIPSEBUILD

echo "Deleting 'eclipse' directory and archive downloaded"
rm -rf eclipse
rm $ECLIPSEARCHIVE

echo "Installing plugins required for build step into eclipse.build"
cd $ORCCWORK
$ECLIPSEBUILD/eclipse 	-nosplash -consoleLog \
						-application org.eclipse.equinox.p2.director \
						-destination $ECLIPSEBUILD \
						-repository $ECLIPSEREPOSITORY \
						-followReferences \
						-installIU $BUILDDEPS

[ "$?" != "0" ] && exit 1

echo "***END*** $0 `date -R`"
