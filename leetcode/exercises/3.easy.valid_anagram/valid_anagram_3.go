// -----------------------
// Created       : 30/10/2025
// Last Edited   : 30/10/2025
// Big O         :
// Topics        : 
// Problem Id    : 242
// -----------------------

package main

import (
    "fmt"
    "sort"
)

func isAnagram(s, t string) bool {
    sr := []rune(s)
    tr := []rune(t)

    sort.Slice(sr, func (i, j int) bool {
        return sr[i] < sr[j]
    })    
    sort.Slice(tr, func (i, j int) bool {
        return tr[i] < tr[j]
    })    

    return string(sr) == string(tr)
}

func main() {
    fmt.Println(isAnagram("oiii", "io"))
}
