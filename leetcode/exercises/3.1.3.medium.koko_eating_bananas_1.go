// -----------------------
// Created     : 01/12/2025
// Last Edited : 01/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 
// References  : https://www.youtube.com/watch?v=U2SozAs9RzA
// Notes       : 
// -----------------------

package main

import (
    "fmt"
    "slices"
    "math"
)

func minEatingSpeed(piles []int, h int) int {
    l := 1
    r := slices.Max(piles)
    res := 0
    for l <= r {
        k := l + (r - l) / 2

        s := 0
        for _, p := range piles {
            s += int(math.Ceil(float64(p)/float64(k)))
        }

        if s <= h {
            res = k
            r = k - 1
        } else {
            l = k + 1
        }

    }
    return res
    
}

func main() {
    fmt.Println(minEatingSpeed([]int{1, 10, 2, 5, 4, 3}, 10))
}
