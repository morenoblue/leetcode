package main
import "fmt"

func twoSum(nums []int, target int) []int {
    m := map[int]int{}
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
