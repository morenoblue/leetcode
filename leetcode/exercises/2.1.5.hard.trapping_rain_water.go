// -----------------------
// Created     :7/11/2025
// Last Edited :7/11/2025 
// Topics      :
// Big O       :
// Problem Id  :2
// Source      :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func trap(height []int) int {
    res := 0
    l_m := 0
    r_m := 0
    l := 0
    r := len(height) - 1
    for l <= r {
        if l_m <= r_m {
            res += max(l_m - height[l], 0)
            if height[l] > l_m {
                l_m = height[l]
            }
            l += 1
        } else {
            res += max(r_m - height[r], 0)
            if height[r] > r_m {
                r_m = height[r]
            }
            r -= 1
        }
    }
    return res
    
}

func main() {
    fmt.Println(trap([]int{4,2,0,3,2,5}))
}
