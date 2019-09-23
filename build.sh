#!/bin/bash

CLONED_JAVADOC_LOCATION="materjalid"
rm -rf $CLONED_JAVADOC_LOCATION

git clone https://github.com/taltech-coding/javadoc.git $CLONED_JAVADOC_LOCATION

source ./materjalid/setup.sh
