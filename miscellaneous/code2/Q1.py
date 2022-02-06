# fix: missed the point.
import re
import enum
from itertools import zip_longest


def str_to_byte8(cha: str) -> str:
    """
    Converting of string into 8-bit binary bits
    Adding prefix of zero if the binary is not the
    legth of the 8
    """
    bin_data = bin(ord(cha)).replace("b", "")
    if len(bin_data) != 8:
        missing = 8 - len(bin_data)
        for _ in range(0, missing):
            bin_data = '0' + bin_data
    return bin_data


def byte_to_int(cha: str) -> int:
    """
    Gives the integer value equivalent to given bytes
    """
    return int(cha, 2)


def grouper(value: str, byte: int, fill_value: int = '0') -> zip_longest:
    """
    Divided the value into given number of equal parts
    and added fill_value to match the equal_parts
    """
    args = [iter(value)] * byte
    return zip_longest(*args, fillvalue=fill_value)


def mapping():
    """
    Generation of mapping data/info
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v',
                'w', 'x', 'y', 'z']
    numbers = list(range(0, 10))
    symbols = ['+', '/']
    upper_alphabet = [_.upper() for _ in alphabet]
    mapping = alphabet + upper_alphabet + numbers + symbols
    _dict = {}
    for i, x in zip(range(len(mapping)), mapping):
        _dict[str(i)] = str(x)
    return _dict


def zip_longest_to_str(value: zip_longest) -> list[str]:
    """
    take zip_longest type(list of tuples) to list of str
    """
    _tem = []
    for v in value:
        _tem.append("".join(_ for _ in v))
    return _tem


def let_run(check_string: str):
    """
    Main function
    """
    print(f"Given string is {check_string}")
    data = re.search(r'[^\w/\d+]', check_string)
    if not data:
        print("Only contain what char we want")
        bit8_list = [str_to_byte8(c) for c in check_string]
        bit8_list = "".join(bit8_list)
        value = grouper(bit8_list, 6)
        _tem = zip_longest_to_str(value)

        data = [byte_to_int(c) for c in _tem]
        data = [MAPPING_INFO[str(v)].value for v in data]
        return ''.join(data)
    else:
        print(-1)


if __name__ == "__main__":
    _dict = mapping()
    MAPPING_INFO = enum.Enum("MAPPING_INFO", _dict)

    # passing case
    Input_string = "ab7+/"
    print(let_run(Input_string))

    # failing case
    Input_string = "ab7+/$"
    print(let_run(Input_string))
