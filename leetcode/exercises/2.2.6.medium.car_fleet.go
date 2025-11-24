// -----------------------
// Created     : 24/11/2025
// Last Edited : 24/11/2025 
// Topics      : 
// Big O       :
// Problem Id  : 853
// References  : https://www.youtube.com/watch?v=Pr6T-3yB9RM
// Notes       : 
// -----------------------

package main

import (
    "fmt"
    "sort"
)


type Sample struct {
    Position int
    Speed int
}

func carFleet(target int, positions []int, speeds []int) int {

    pairs := make([]Sample, len(positions))
    for i := range positions {
        pairs[i] = Sample{
            Position: positions[i],
            Speed: speeds[i],
        }
    }
    sort.Slice(pairs, func(i, j int) bool { return pairs[i].Position > pairs[j].Position})

    stack := []float64{}
    for _,v := range pairs {

        rs := float64(target - v.Position) / float64(v.Speed)

        if len(stack) == 0 {
            stack = append(stack, rs)    
            continue
        }

        if rs > stack[len(stack)-1] {
            stack = append(stack, rs)    
        }

    }

    return len(stack)
}

func main() {
    fmt.Println(carFleet(10, []int{6, 8}, []int{3, 2}))
}
