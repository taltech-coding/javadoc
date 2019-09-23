#!/bin/bash

CLONED_JAVADOC_LOCATION="materjalid"

source ../py/bin/activate

sphinx-build -b html $CLONED_JAVADOC_LOCATION /javadoc
