class Fano:
    c: dict

    def __init__(self, chars: str, values: str):
        chars = list(chars.split(" "))
        values = list(map(float, values.replace(",", ".").split(" ")))

        d = {key: value for key, value in zip(chars, values)}

        sorted_keys = sorted(d, key=d.get, reverse=True)
        self.values = [[x, d[x], ""] for x in sorted_keys]

        self.c = {}

    @staticmethod
    def __divide_list(l):
        if len(l) == 2:
            return [l[0]], [l[1]]
        else:
            n = 0
            for i in l:
                n += i[1]
            x = 0
            distance = abs(2 * x - n)
            j = 0
            for i in range(len(l)):  # shannon tree structure
                x += l[i][1]
                if distance < abs(2 * x - n):
                    j = i
        return l[0:j + 1], l[j + 1:]

    def __label_list(self, l):
        list1, list2 = self.__divide_list(l)
        for i in list1:
            i[2] += '0'
            self.c[i[0]] = i[2]
        for i in list2:
            i[2] += '1'
            self.c[i[0]] = i[2]
        if len(list1) == 1 and len(list2) == 1:  # assigning values to the tree
            return
        self.__label_list(list2)

    def get_values_codes(self):
        return self.__label_list(self.values)
