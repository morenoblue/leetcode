// -----------------------
// Created     : 04/12/2025
// Last Edited : 04/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 33. Search in Rotated Sorted Array
// References  : https://www.youtube.com/watch?v=U8XENwh8Oy8
// Notes       : Damn, got absolutely rekt by this one. No problem though, 
//               Neetcode for the rescue
// -----------------------

package main
import (
    "fmt"
)

func search(nums []int, target int) int {
    l := 0
    r := len(nums) - 1

    for l <= r {
        m := l + (r - l) / 2
        if target == nums[m] { return m }
        if nums[l] <= nums[m] {
            if target < nums[l] || target > nums[m] {
                l = m + 1 
            } else {
                r = m - 1
            }
        } else {
            if target > nums[r] || target < nums[m] {
                r = m - 1
            } else {
                l = m + 1 
            }
        }
    }
    return -1
}

func main() {
    fmt.Println(search([]int{4,5,6,7,0,1,2}, 0))
}
