// -----------------------
// Created     :3/11/2025
// Last Edited :3/11/2025 
// Topics      :
// Big O       :
// Problem Id  :25
// Source      :
// Notes       :
// -----------------------

package main

import (
    "fmt"
)

func isPalindrome(s string) bool {

    isalnum := func(c byte) bool {
        return (97 <= c && c <= 122) ||
               (65 <= c && c <= 90) ||
               (48 <= c && c <= 57)
    }

    bytetolower := func(c byte) byte {
        if 65 <= c && c <= 90 { 
            return c + 97 - 65
        } else {
            return c
        }
    }

    l := 0;
    r := len(s) - 1;
    for l < r {
        for !isalnum(s[l]) {
            l++
            if l == len(s) { return true }
        }
        for !isalnum(s[r]) {
            r--
        }

        if bytetolower(s[r]) != bytetolower(s[l]) { return false }
        l++
        r--
    }
    return true
}

func main() {
    fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
}

