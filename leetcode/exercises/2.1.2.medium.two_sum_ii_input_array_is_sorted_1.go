// -----------------------
// Created    : 13/11/2025
// Last Edited: 13/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 167
// -----------------------

package main

import (
    "fmt"
)

func twoSum(numbers []int, target int) []int {
    l := 0
    r := len(numbers) - 1
    sum := 0
    for l < r {
        sum = numbers[l] + numbers[r]
        if sum == target { return []int{l+1, r+1} }
        if sum < target {
            l++
        } else {
            r--
        }
    }
    return []int{0, 0}
}

func main() {
    fmt.Println(twoSum([]int{2,7,11,15},13))
}
