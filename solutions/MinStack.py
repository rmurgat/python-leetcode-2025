class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.minimums.append(val)

    def pop(self) -> None:
        if self.stack[len(self.stack)-1]==self.minimum:
            self.minimums.pop()
            if len(self.minimums)==0:
               self.minimum = float("inf")
            else:
                self.minimum = min(self.minimums)           
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if len(self.stack)==0: return None
        return self.minimum
    
    def print(self) -> None:
        print("stack: [ ",end="")
        for i in range(len(self.stack)):
            if self.stack[i] is None: 
                print (" None, ", end="")
            else:
                print (f"{self.stack[i]}, ",end="")
        print(" ]")
