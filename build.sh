#!/bin/bash

SOURCE="materjalid"
rm -rf $SOURCE

git clone https://github.com/taltech-coding/javadoc.git $SOURCE

source ../py/bin/activate

sphinx-build -b html $SOURCE /javadoc
