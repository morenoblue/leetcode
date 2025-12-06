# -----------------------
# Created     : 05/12/2025
# Last Edited : 05/12/2025 
# Topics      : 
# Big O       :
# Problem Id  : 981. Time Based Key Value Store
# References  :
# Notes       :
#               
# -----------------------

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashset = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashset[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:

        if timestamp in self.hashset[key]:
                return self.hashset[key][timestamp] 
        
        keys = self.hashset[key].keys()
        l = 0
        r = len(keys) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if self.hashset[key][[keys][m]] < timestamp:
                res =  self.hashset[key][[keys][m]] 
                l = m + 1
            else:
                if res != "":
                    break
                r = m - 1
            
        return  res


timeMap = TimeMap();
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
print(timeMap.set("foo", "bar2", 4))
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))

