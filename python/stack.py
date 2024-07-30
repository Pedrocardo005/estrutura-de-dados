class Stack:
    
    def __init__(self):
        self.__items = [None]
        self.top = 0

    def push(self, elemento):
        if len(self.__items) >= self.top:
            items2 = [None] * len(self.__items)
            self.__items += items2
        
        self.__items[self.top] = elemento

        self.top += 1
