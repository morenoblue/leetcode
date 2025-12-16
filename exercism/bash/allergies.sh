#!/usr/bin/env bash

# -----------------------
# Created       : 16/12/2025
# Last Edited   : 16/12/2025
# Big O         :
# Topics        : 
# Source        : https://exercism.org/tracks/bash/exercises/allergies
# -----------------------


allergic_to () {
    allergic="$2"
    score="$1"
    count=1
    allergies=(
        
        eggs 
        peanuts 
        shellfish 
        strawberries 
        tomatoes 
        chocolate 
        pollen 
        cats
        
    )

    for allergen in "${allergies[@]}"; do
        if [[ $allergic = $allergen ]]; then
            if (( score & count )); then
                echo "true"
            else
                echo "false"
            fi
            return
        fi
        (( count <<= 1 ))
    done
}

list () {
    score="$1"
    allergies=(
        
        eggs 
        peanuts 
        shellfish 
        strawberries 
        tomatoes 
        chocolate 
        pollen 
        cats
        
    )
    count=1
    res=()

    for allergen in "${allergies[@]}"; do
        (( score & count )) && res+=( "$allergen" )
        (( count <<= 1 ))
    done
    echo "${res[@]}"
}

main () {

    "$2" "$1" "$3"
}


main "$@"


