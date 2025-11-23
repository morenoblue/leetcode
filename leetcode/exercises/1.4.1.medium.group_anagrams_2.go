// -----------------------
// Created     : 02/11/2025
// Last Edited : 02/11/2025
// Topics      : 
// Big O       :
// Problem Id  : 49
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
    "maps"
    "slices"
)

func groupAnagrams(strs []string) [][]string {

    m := make(map[[26]int][]string) 

    for _, v := range strs {

        key := [26]int{}
        for i := 0; i < len(v); i++ {
            key[v[i] - 'a'] = key[v[i] - 'a'] + 1
        }
        m[key] = append(m[key], v)
    }

    vals := maps.Values(m)

    return slices.Collect(vals)
}

func main() {
    fmt.Println(groupAnagrams([]string{"eat","tea","tan","ate","nat","bat"}))
}
