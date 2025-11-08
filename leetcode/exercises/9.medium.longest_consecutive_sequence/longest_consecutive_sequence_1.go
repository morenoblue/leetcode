// -----------------------
// Created    : 08/11/2025
// Last Edited: 08/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 238
// -----------------------

package main
import (
    "fmt"
)

func longestConsecutive(nums []int) int {

    set := make(map[int]struct{})
    for _, i := range nums {
        set[i] = struct{}{}
    }

    longest := 0
    size := 0
    for v, _ := range set {
        if _, ok := set[v-1]; !ok {
            size = 1
            for {
                if _, ok := set[v+size]; !ok {
                    break
                }
                size++
            }
        }
        longest = max(longest, size)
    }

    return longest

}

func main() {
    fmt.Print(longestConsecutive([]int{100,4,200,1,3,2}))
}
