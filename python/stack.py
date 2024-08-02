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

        if self.isempty():
            return

        elemento = self.__items[self.__top - 1]
        del self.__items[self.__top - 1]
        self.__top -= 1
        return elemento
    
    def peek(self):
        return self.__items[self.__top - 1]
    
    def isempty(self):
        return self.__top == 0
    
    def clear(self):
        self.__items = []

    def size(self):
        return self.__top
    
    def __str__(self) -> str:
        if self.__items[0] == None:
            return None
        lista = '{}'.format(self.__items[0])

        for n in range(1, len(self.__items)):
            if self.__items[n] == None:
                break
            lista += ', {}'.format(self.__items[n])

        return lista
