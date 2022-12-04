class LZW:
    s: str
    last_index: int
    dictionary: dict

    def __init__(self, s=str):
        self.s = s

        file_set = sorted(set(s))
        self.last_index = len(file_set)
        self.dictionary = {x: ord(x) for x in file_set}

    def encode(self):
        result = []
        s = ""

        for i in range(len(self.s)):
            char = self.s[i]

            if self.dictionary.get(s + char) is not None:
                s = s + char
            else:
                result.append(self.dictionary[s])
                self.dictionary[s + char] = self.last_index
                s = char
                self.last_index += 1

        result.append(self.dictionary[s])
        return list(format(x, 'b') for x in result)
