# Todo: Task was in Q1 image.
import re
from itertools import zip_longest


def str_to_byte8(cha: str) -> str:
    bin_data = bin(ord(cha)).replace("b", "")
    if len(bin_data) != 8:
        missing = 8 - len(bin_data)
        for _ in range(0, missing):
            bin_data = '0' + bin_data
    return bin_data


def byte_to_str(cha: str) -> str:
    return str(chr(int(cha, 2)))


def grouper(value: str, byte: int, fill_value: int = '0') -> zip_longest:
    args = [iter(value)] * byte
    return zip_longest(*args, fillvalue=fill_value)


def let_run(check_string: str):
    print(f"Given string is {check_string}")
    data = re.search(r'[^\w/\d+]', check_string)
    if not data:
        print("Only contain what char we want")
        bit8_list = [str_to_byte8(c) for c in check_string]
        bit8_list = "".join(bit8_list)
        value = grouper(bit8_list, 6)
        _tem = []
        for v in value:
            _tem.append("".join(_ for _ in v))

        return "".join(
            [byte_to_str(c) for c in _tem]).encode("utf-8",
                                                   errors='ignore')
    else:
        print(-1)


if __name__ == "__main__":
    # passing case

    Input_string = "ab7+/"
    print(let_run(Input_string))

    # failing case
    Input_string = "ab7+/$"
    print(let_run(Input_string))
