#!/bin/sh

# we build one item with mock, including the temp repo

GITHUB_OWNER=`cat $1.spec | grep "%global github_owner" | awk {'print $3'}`
GITHUB_NAME=`cat $1.spec | grep "%global github_name" | awk {'print $3'}`
GITHUB_COMMIT=`cat $1.spec | grep "%global github_commit" | awk {'print $3'}`
NAME=$1
VERSION=`cat $1.spec | grep "Version:" | cut -d ':' -f 2 | tr -d "[:space:]"`
GITHUB_SHORT=`echo ${GITHUB_COMMIT} | head -c 7`

mock $HOME/output/$NAME*.src.rpm


