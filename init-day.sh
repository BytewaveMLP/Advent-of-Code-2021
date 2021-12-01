#!/bin/sh

set -eu

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <day-number>"
	exit 1
fi

DAYNO="$1"

DAYDIR="Day $(printf %02d $DAYNO)"

mkdir "$DAYDIR"

cp -r .template/* "$DAYDIR"

echo "$DAYDIR created. GO GO GO!"
