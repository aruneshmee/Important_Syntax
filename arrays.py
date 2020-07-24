# Dynamic Arrays

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    # Check length
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        
        return self.A[k]
    #ADD item
    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) 
            
        self.A[self.n] = ele
        self.n += 1
        
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object)()
    
def anag(s1,s2):
    
    s1 = s1.replace(' ', '').lower()
    #print(s1)
    s2 = s2.replace(' ', '').lower()
    
    # Edge Case
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1
            
    print(count)
    for k in count:
        print(k)
        if count[k] != 0:
            return False
        
    return True
