from bwt import BWT
from lzw import LZW


def main():
    s = input("Enter encoding string")
    bwt = BWT(s)
    index = bwt.index_getter()
    s = s + str(index)
    lzw = LZW(s)
    result = lzw.encode()
    print(" ".join(result))


if __name__ == '__main__':
    main()
