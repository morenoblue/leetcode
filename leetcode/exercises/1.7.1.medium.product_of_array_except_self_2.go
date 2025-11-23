// -----------------------
// Created     :7/11/2025
// Last Edited :7/11/2025 
// Topics      :
// Big O       :
// Problem Id  :38
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func productExceptSelf(array []int) []int {

    res := []int{1}

    prefix := 1
    for i := 0; i < len(array)-1; i++ {
        res = append(res, prefix*array[i])
        prefix *= array[i]
    }

    postfix := 1
    for i := len(array)-1; i > -1; i-- {
        res[i] *= postfix
        postfix *= array[i]
    }

    return res

}

func main () {
    fmt.Println(productExceptSelf([]int{1,2,3,4}))
}
