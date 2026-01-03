class StackList:
    def __init__(self, size):
        self.size = size
        self.__data = [None] * size

    def pop(self):
        result = self.__data[index := StackList.__find_last_not_none(self.__data)]
        self.__data[index] = None
        return result

    def push(self, value):
        self.__data[StackList.__find_last_not_none(self.__data) + 1] = value

    @staticmethod
    def __find_last_not_none(lst):
        for i, v in enumerate(lst):
            if v is not None: continue
            if v is None:
                return i - 1
        return None
