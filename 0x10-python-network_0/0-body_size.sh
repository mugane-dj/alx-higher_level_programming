#!/bin/bash
# This script displays the size of the body of the response
CURL='/usr/bin/curl'
GREP='/usr/bin/grep'
$CURL -sI "$1" | $GREP -i 'content-length' | awk '{print $2}'
