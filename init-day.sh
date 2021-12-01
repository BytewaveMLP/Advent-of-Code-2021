#!/bin/sh

set -exu

DAYNO="$1"

if [ -z "$DAYNO" ]; then
	echo "Usage: $0 <day-number>"
	exit 1
fi

DAYDIR="Day $DAYNO"

mkdir "$DAYDIR"

cp -r template/* "$DAYDIR"
