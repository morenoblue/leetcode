// -----------------------
// Created     : 03/11/2025
// Last Edited : 03/11/2025
// Topics      : 
// Big O       :
// Problem Id  : 347
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func topKFrequent(nums []int, k int) []int {

    counts := make(map[int]int)
    for _,v := range nums {
        if _, ok := counts[v]; !ok{
        counts[v] = -1
        }
        counts[v]++
    }

    freq := make([][]int, len(nums))
    for k,v := range counts {
        freq[v] = append(freq[v], k)
    }

    result := []int{}
    for i := len(freq) - 1; i >= 0; i-- {
        for _, v := range freq[i] {
            result = append(result, v)
            if len(result) == k { return result }
        }
    }

    return result
    
}

func main() {
    fmt.Println(topKFrequent([]int{1, 1, 3, 1, 3, 2, 10, 10, 9}, 3))
}
