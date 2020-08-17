class Deque(object):
    
    def __init__(self):
        self.items = []
        
    def isemp(self):
        return self.items == []
    
    def addfront(self, item):
        self.items.append(item)
        
    def addback(self, item):
        self.items.insert(0, item)
    
    def removeF(self):
        return self.items.pop()
    
    def removeB(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
