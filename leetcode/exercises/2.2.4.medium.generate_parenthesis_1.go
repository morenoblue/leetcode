// -----------------------
// Created     : 26/11/2025
// Last Edited : 26/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 150
// References  : https://www.youtube.com/watch?v=s9fokUqJ76A
// Notes       : Man this backtracking stuff is tuff
// -----------------------

package main

import (
    "fmt"
)

func generateParenthesis(n int) []string {

    res := []string{}
    stack := []rune{}

    var backtracking func(open, closed int)
    backtracking = func(open int, closed int) {

        if open == n && closed == n {
            current := ""
            for _, v := range stack {
                current += string(v)
            }
            res = append(res, current)
            return
        }

        if open < n {
            stack = append(stack, '(')
            backtracking(open + 1, closed)
            stack = stack[:len(stack)-1]
        }

        if closed < open {
            stack = append(stack, ')')
            backtracking(open, closed+1)
            stack = stack[:len(stack)-1]
        }

    }

    backtracking(0, 0)
    return res
}


func main() {
    fmt.Println(generateParenthesis(3))
}


