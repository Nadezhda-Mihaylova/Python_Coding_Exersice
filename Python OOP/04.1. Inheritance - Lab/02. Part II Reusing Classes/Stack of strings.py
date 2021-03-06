class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        result = self.__data.pop()
        return result

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0

    def __str__(self):
        return str(self.__data[::-1])