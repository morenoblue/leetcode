// -----------------------
// Created     :9/11/2025
// Last Edited :9/11/2025 
// Topics      :
// Big O       :
// Problem Id  :50
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
    "strings"
    "strconv"
)

func evalRPN(tokens []string) int {
    stack := []int{}
    res := 0
    for _, v := range tokens {
        if !strings.Contains("+-/*", v) {
            i, err := strconv.Atoi(v)
            if err != nil {
                panic(err)
            }
            stack = append(stack, i)        
            continue
        } else if v == "-" {
            res = stack[len(stack) - 2] - stack[len(stack) - 1]
        } else if v == "*" {
            res = stack[len(stack) - 2] * stack[len(stack) - 1]
        } else if v == "/" {
            res = stack[len(stack) - 2] / stack[len(stack) - 1]
        } else {
            res = stack[len(stack) - 2] + stack[len(stack) - 1]
        }
        stack = stack[:len(stack)-2]
        stack = append(stack, res)
    }
    return stack[0]
}

func main() {
    fmt.Println(evalRPN([]string{"4","13","5","/","+"}))
}
