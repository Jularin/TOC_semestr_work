from fano import Fano


def decode():
    res = ""
    buff = ""
    for num in encoded:
        buff = buff + num
        if code_str_mapping.get(buff) is not None:
            res = res + code_str_mapping.get(buff)
            buff = ""
    return res


if __name__ == '__main__':
    chars = input("Enter chars ")
    values = input("Enter values ")
    encoded = input("Enter encoded values ")
    f = Fano(chars, values)

    encoded_values = f.get_values_codes()

    code_str_mapping = {encoded_values[x]: x for x in encoded_values}
