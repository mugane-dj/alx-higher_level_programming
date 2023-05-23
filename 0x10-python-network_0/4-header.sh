#!/bin/bash
#This script sends a GET request to the url provided with a header
curl -sH 'X-School-User-Id: 98' "$1"
