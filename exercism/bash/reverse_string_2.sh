#!/bin/bash

# -----------------------
# Created       : 20/11/2025
# Last Edited   : 20/11/2025
# Big O         :
# Topics        : 
# Source        : https://exercism.org/tracks/bash/exercises/reverse-string
# -----------------------

main() { 
    echo $@ | rev 
}

main $@


