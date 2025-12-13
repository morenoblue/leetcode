// -----------------------
// Created     : 13/12/2025
// Last Edited : 13/12/2025 
// Topics      : 
// Big O       :
// Problem Id  : 981. Time Based Key Value Store
// References  :
// Notes       :
// -----------------------

type Entry struct {
    value string
    timestamp int
}

type TimeMap struct {
    data map[string][]Entry
}


func Constructor() TimeMap {
    return TimeMap{
        data: make(map[string][]Entry),
    }
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    this.data[key] = append(this.data[key], Entry{value: value, timestamp:timestamp})
}


func (this *TimeMap) Get(key string, timestamp int) string {
    size := len(this.data[key])
    res := ""

    if size == 0 { return res }

    l := 0
    r := size - 1
    m := 0
    for l <= r {
        m = l + (r - l) / 2
        if this.data[key][m].timestamp == timestamp { return this.data[key][m].value }

        if this.data[key][m].timestamp < timestamp {
            res = this.data[key][m].value
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return res
}

