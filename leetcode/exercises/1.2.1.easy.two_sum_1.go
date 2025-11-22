// -----------------------
// Created     : 30/10/2025
// Last Edited : 30/10/2025
// Topics      : 
// Big O       :
// Problem Id  : 1
// Source      :
// Notes       :
// -----------------------

package main
import "fmt"

func twoSum(nums []int, target int) []int {
    m := make(map[int]int{})
    for i, v := range nums {
        complement := target - v
        _, ok := m[complement] 
        if ok { return []int{m[complement], i} }
        m[v] = i
    }
    return []int{0,0}
}

func main() {
    fmt.Println(twoSum([]int{1,5,6,2,2,8}, 11))
}
