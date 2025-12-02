// -----------------------
// Created     : 02/12/2025
// Last Edited : 02/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 153. Find Minimum in Rotated Sorted Array
// References  : My brain 😏
// Notes       : Self Solved. I so proud rn. This is my first exercise that I 
//               solve by myself with the solution actually being optimal! I 
//               thought about the solution in the shower.
// -----------------------

package main

import (
    "fmt"
)

func findMin(nums []int) int {
    l := 0
    r := len(nums) - 1
    for l <= r {
        m := l + (r -l) / 2
        if nums[l] < nums[r] { return nums[l] }

        if nums[l] <= nums[m] {
            l = m + 1
        } else {
            r = m
        }
    }
    return nums[r]
}

func main() {
    fmt.Println(findMin([]int{4,5,6,7,1,2}))
}
