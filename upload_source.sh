#!/bin/sh

PACKAGE=$1

rpmdev-wipetree
VERSION=`cat $1.spec | grep "Version:" | cut -d ':' -f 2 | tr -d "[:space:]"`
GH_NAME=`cat $1.spec | grep "%global github_name" | awk {'print $3'}`
echo $GH_NAME

(
cp $1* ~/rpmbuild/SOURCES/
mv ~/rpmbuild/SOURCES/$1.spec ~/rpmbuild/SPECS/
cd ~/rpmbuild/SOURCES
curl -O -L https://github.com/fkooman/$GH_NAME/archive/$VERSION.tar.gz
cd ~/rpmbuild/SPECS/
rpmbuild -bs $1.spec
rpmlint ~/rpmbuild/SPECS/*.spec ~/rpmbuild/SRPMS/*.rpm
scp ~/rpmbuild/SPECS/*.spec ~/rpmbuild/SRPMS/*.rpm fedorapeople.org:~/public_html/$1/
)

