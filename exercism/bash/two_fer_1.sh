#!/bin/bash

# -----------------------
# Created       : 21/11/2025
# Last Edited   : 21/11/2025
# Big O         :
# Topics        : 
# Source        : https://exercism.org/tracks/bash/exercises/two-fer
# -----------------------

main() {

    if [ "$1" = "" ]; then
        echo "One for you, one for me."
    else
        echo "One for $1, one for me."
    fi

}

main "$@"
