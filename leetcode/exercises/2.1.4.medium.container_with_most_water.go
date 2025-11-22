// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :1
// Source      :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func maxArea(height []int) int {
    l := 0
    r := len(height) - 1
    max_height := 0
    base := 0
    h := 0
    for i := 0; i < len(height); i++ {
        base = max((r - l), -(r - l))
        h = min(height[l], height[r])
        max_height = max(max_height, base*h)
        if height[l] < height[r] {
            l++
        } else if height[l] > height[r] {
            r--
        } else {
            l++
            r--
        }
    }
    return max_height
}

func main() {
    fmt.Print(maxArea([]int{1,2,1}));
}

