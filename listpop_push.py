class Stack:
    
    def __init__(self,items):
        self.items = items
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self,r):
        
        for i in range(len(self.items)):
            r.append(self.items.pop())
        return r
        

item = Stack([])
item.push("H")
item.push("E")
item.push("L")
item.push("L")
item.push("O")

print(item.pop([]))
