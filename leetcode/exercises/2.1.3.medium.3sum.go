// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :5  
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
    "sort"
)

func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    triplets := [][]int{}
    for i := 0; i < len(nums); i++ {
        if (i > 0) && (nums[i - 1] == nums[i]) { continue } 

        l := i + 1
        r := len(nums) - 1
        sum := 0

        for l < r {

            sum = nums[i] + nums[l] + nums[r]
            if sum < 0 {
                l++

            } else if sum > 0 {
                r--

            } else {
                triplets = append(triplets, []int{nums[i], nums[l], nums[r]})

                l++
                for (l < r) && (nums[l] == nums[l-1]) {
                    l++
                }

                // note(@morenoblue): we could comment this code paragraph 
                //                    and it would still work.
                r--
                for (l < r) && (nums[r] == nums[r+1]) {
                    r--
                }

            }
        }
    }
    return triplets     
}

func main() {
    fmt.Println(threeSum([]int{2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10}))
}
