// -----------------------
// Created    :  18/11/2025
// Last Edited:  18/11/2025
// Topics     : 
// Big O      :
// Problem Id : 20
// -----------------------

package main

import (
    "fmt"
)

func isValid(s string) bool {
    m := map[rune]rune{
        '}':'{',
        ')':'(',
        ']':'[',
    }
    stack := []rune{}
    for _, v := range s {
        if _, ok := m[v]; ok {
            if len(stack) == 0 || stack[len(stack)-1] != m[v] { return false }
            stack = stack[:len(stack)-1]
        } else {
         stack = append(stack, v)
        }
    }

    if len(stack) == 0 { 
        return true
    } else {
        return false
    }
    
}

func main() {
    fmt.Println(isValid("{}()()[]{([})}"))
}
