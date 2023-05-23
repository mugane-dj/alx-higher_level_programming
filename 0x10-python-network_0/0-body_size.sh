#!/bin/bash
#This script displays the size of the body of a curl response
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
