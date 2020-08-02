# Stack
class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
  
# Queue
class Queue(object):
    
    def __init__(self):
        self.items = []
    
    def enq(self, item):
        self.items.insert(0, item)
        
    def isEM(self):
        return self.items == []
    
    def deq(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
