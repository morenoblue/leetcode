// -----------------------
// Created     : 28/11/2025
// Last Edited : 28/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 
// References  : 
// Notes       : Self Solved
// -----------------------

package main

import (
    "fmt"
)

func searchMatrix(matrix [][]int, target int)  bool {
    t := 0
    b := len(matrix)
    mr := 0
    for t < b {
        mr = t + (b - t) / 2
        if target > matrix[mr][0] && target < matrix[mr][len(matrix[mr]) - 1] {
            break
        } else if target < matrix[mr][0] {
            b = mr
        } else {
            t = mr + 1
        }
        if t >= b {
            return false
        }
    }

    l := 0
    r := len(matrix[0])
    mc := 0
    for l < r {
        mc = l + (r - l) / 2
        if target == matrix[mr][mc] {
            return true    
        } else if target < matrix[mr][mc] {
            r = mc
        } else {
            l = mc + 1
        }
    }
    return false
}

func main() {
    fmt.Println(searchMatrix([][]int{{1,3,5,7},{10,11,16,20},{23,30,34,60}}, 31))
}
