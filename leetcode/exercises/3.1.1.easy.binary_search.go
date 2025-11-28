// -----------------------
// Created     : 28/11/2025
// Last Edited : 28/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 704
// References  : 
// Notes       : 
// -----------------------

package main

import (
    "fmt"
)

func search(nums []int, target int) int {
    l := 0
    r := len(nums)
    m := 0
    for l < r {
        m = l + (r-l)/2
        if target == nums[m] {
            return m
        } else if target < nums[m] {
            r = m
        } else {
            l = m + 1
        }
    }
    return -1
}

func main() {
    fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7, 8}, 4))
}
