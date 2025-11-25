// -----------------------
// Created     : 25/11/2025
// Last Edited : 25/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 84
// References  : https://www.youtube.com/watch?v=zx5Sw9130L0
// Notes       : 
// -----------------------

package main

import (
    "fmt"
)

func largestRectangleArea(heights []int) int {
    stack := [][]int{}
    max_area := 0
    h := 0
    for i := range len(heights)+1 {

        if i < len(heights) {
            h = heights[i]
        } else {
            h = 0
        }

        if len(stack) == 0 || h >= stack[len(stack)-1][1]{
            stack = append(stack, []int{i, h})
        } else {
            start := 0
            area := 0
            for (len(stack) > 0) && (stack[len(stack)-1][1] > h) {
                area = (i - stack[len(stack)-1][0]) * stack[len(stack)-1][1]
                max_area = max(area, max_area)
                start = stack[len(stack)-1][0]
                stack = stack[:len(stack)-1]
            }
            stack = append(stack, []int{start, h})
        }
    }

    return max_area
}

func main() {
    fmt.Println(largestRectangleArea([]int{2,4}))
}




