class BWT:
    """
    Burrows–Wheeler transform algorithm
    """
    s: str
    arr: list
    index: int

    def __init__(self, s):
        self.s = s
        self.arr = self.__generate_sorted_circular_shifts()
        self.index = self.__find_string()

    def __generate_sorted_circular_shifts(self) -> list:
        arr = []
        length = len(self.s)
        for i in range(1, length + 1):
            arr.append(self.s[-i:] + self.s[:length - i])
        return sorted(arr)

    def __find_string(self):
        for index, string in enumerate(self.arr):
            if string == self.s:
                return index
        raise ValueError("Искомая строка не найдена!")

    def index_getter(self):
        return self.index
