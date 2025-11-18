// -----------------------
// Created    : 18/11/2025
// Last Edited: 18/11/2025 
// Topics     : 
// Big O      :
// Problem Id : 20
// -----------------------

package main

import (
    "fmt"
)

type MinStack struct {
    obj []int
    minvals []int
    
}


func Constructor() MinStack {
    return MinStack{}
    
}


func (this *MinStack) Push(val int)  {
    if len(this.obj) == 0 {
        this.minvals = append(this.minvals, 0)
    } else if val < this.obj[this.minvals[len(this.minvals) - 1]] {
        this.minvals = append(this.minvals, len(this.obj))
    } else {
        this.minvals = append(this.minvals, this.minvals[len(this.minvals) - 1])
    }
    this.obj = append(this.obj, val)
    
}


func (this *MinStack) Pop()  {
    this.minvals = this.minvals[:len(this.minvals)-1]
    this.obj = this.obj[:len(this.obj)-1]
    
}


func (this *MinStack) Top() int {
    return this.obj[len(this.obj) - 1]
}


func (this *MinStack) GetMin() int {
    return this.obj[this.minvals[len(this.minvals) - 1]]
}

func main() {

    obj := Constructor();
    obj.Push(0);
    obj.Push(1);
    obj.Push(0);
    fmt.Println(obj.GetMin())
    obj.Pop();
    fmt.Println(obj.GetMin())
    obj.Pop();
    fmt.Println(obj.GetMin())
    obj.Pop();
    obj.Push(-2)
    obj.Push(-1)
    obj.Push(-2)
    fmt.Println(obj.GetMin())
    obj.Pop();
    fmt.Println(obj.Top())
    fmt.Println(obj.GetMin())
    obj.Pop();
    fmt.Println(obj.GetMin())
    obj.Pop();

}
