package main
import "fmt"

func containsDuplicate(nums []int) bool {
    m := map[int]int{}
    for _, v := range nums {
        m[v] = m[v] + 1
        if (m[v] > 1) {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(containsDuplicate([]int{1,2,4,8,5,10}))
}
