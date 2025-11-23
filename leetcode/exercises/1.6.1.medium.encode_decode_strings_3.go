// -----------------------
// Created     : 03/11/2025
// Last Edited : 03/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 271
// References  :
// Notes       :
// -----------------------

package main

import (
    "fmt"
    "strconv"
)

type Solution struct{}

func (so *Solution) Encode(strs []string) string {
    encoded := string("")
    for _, v := range strs {
        encoded += fmt.Sprint(len(v)) + "#" + v
    }
    return encoded
}

func (so *Solution) Decode(s string) []string {
    decoded := []string{}
    i := 0
    for i < len(s) {

        current_length := ""
        for s[i] != '#' {
            current_length += string(s[i])
            i += 1
        }

        n, err := strconv.Atoi(current_length)
        if err != nil {
            panic(err)
        }

        decoded = append(decoded, s[i+1:i+1+n])

        i = i+1+n
    }
    return decoded
}

func main() {

    s := Solution{}
    fmt.Println(s.Encode([]string{"toma", "sai", "ova"}))
    fmt.Println(s.Decode(s.Encode([]string{"toma", "sai", "ova"})))

}

