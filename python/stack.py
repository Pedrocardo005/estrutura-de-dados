class Stack:
    
    def __init__(self):
        self.items = [None]
        self.top = 0

    def push(self, elemento):
        if len(self.items) >= self.top:
            items2 = [None] * len(self.items)
            self.items += items2
        
        self.items[self.top] = elemento

        self.top += 1
