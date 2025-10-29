#! /bin/bash

main() {
string=$1
rev=""
for((i=${#string}-1; i >= 0; i--)); do
    rev+=${string:i:1}
done

echo "${rev}"
}

main "$@"

