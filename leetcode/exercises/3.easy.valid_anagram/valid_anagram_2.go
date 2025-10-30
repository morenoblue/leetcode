package main

import (
    "fmt"
)

func a(s, t string) bool {
    if len(s) != len(t) { return false }

    m := make(map[byte]int)
    for i := 0; i < len(s); i++ {
        m[s[i]]++
        m[t[i]]--
    }

    for _,v := range m {
        if  v != 0 { return false}
    }
    return true

}


func main() {
    fmt.Println(a("oooii", "ioioo"))
}
