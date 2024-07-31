class Stack:
    
    def __init__(self):
        self.__items = [None]
        self.__top = 0

    def push(self, elemento):
        if len(self.__items) >= self.__top:
            items2 = [None] * len(self.__items)
            self.__items += items2
        
        self.__items[self.__top] = elemento

        self.__top += 1

    def pop(self):
        elemento = self.__items[self.__top - 1]
        del self.__items[self.__top - 1]
        self.__top -= 1
        return elemento
    
    def peek(self):
        return self.__items[self.__top - 1]
    
    def isempty(self):
        return self.__top == 0
