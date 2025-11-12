package main

import (
    "fmt"
)

func binary_search(array []int, target int) bool {
    start := 0
    end := len(array)
    for start < end {
        middle := start + (end-start)/2

        if array[middle] == target { return true }

        if array[middle] > target { 
            end = middle 
        } else { 
            start = middle + 1 
        }

    }
    return false
}

func main() {
    fmt.Println(binary_search([]int{1, 3, 11, 12, 14, 18, 18, 19}, 14))
}
