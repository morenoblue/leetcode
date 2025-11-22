// -----------------------
// Created     : 30/10/2025
// Last Edited : 30/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 217
// Source      :
// Notes       :
// -----------------------

package main

import "fmt"
import "sort"

func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := 1; i < len(nums); i++ {
        if nums[i-1] == nums[i] { return true }
    }
    return false
}

func main() {
    fmt.Println(containsDuplicate([]int{5, 2, 3, 10, 8, 1}))
}
