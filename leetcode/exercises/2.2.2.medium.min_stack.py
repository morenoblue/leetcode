# -----------------------
# Created    : 18/11/2025
# Last Edited: 18/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 20
# -----------------------

class MinStack:

    def __init__(self):
        self.obj = []
        self.minvals = []
        

    def push(self, val: int) -> None:

        if not self.minvals:
            self.minvals.append(0)

        elif val < self.obj[self.minvals[-1]]:
            self.minvals.append(len(self.obj))

        else:
            self.minvals.append(self.minvals[-1])

        self.obj.append(val)

                                         
    def pop(self) -> None:               
        self.obj.pop()                   
        self.minvals.pop()               


    def top(self) -> int:
        return self.obj[-1]
        

    def getMin(self) -> int:
        return self.obj[self.minvals[-1]]


obj = MinStack()
print(obj.push(0))
print(obj.push(1))
print(obj.push(0))
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.push(-2))
print(obj.push(-1))
print(obj.push(-2))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
