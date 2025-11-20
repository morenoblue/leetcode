#!/bin/bash

# -----------------------
# Created       : 29/10/2025
# Last Edited   : 14/11/2025
# Big O         :
# Topics        : 
# Source        : https://exercism.org/tracks/bash/exercises/reverse-string
# -----------------------

main() {
string=$1
rev=""
for((i=${#string}-1; i >= 0; i--)); do
    rev+=${string:i:1}
done

echo "${rev}"
}

main "$@"

