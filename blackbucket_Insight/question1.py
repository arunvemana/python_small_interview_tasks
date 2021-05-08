def find_prime_list(upper, lower=1):
    list_ = []
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_.append(num)
    return list_


def into_single_digit(number):
    num = 0
    for i in str(number):
        num += int(i)
    if len(str(num)) > 1:
        return into_single_digit(num)
    else:
        return num


def get_index_vowel(input_):
    _out = ''
    for i in enumerate(input_):
        if i[1].lower() in "aeiou":
            data = i[0]*100
            total = find_prime_list(data)
            total = sum(total)
            single_number = into_single_digit(total)
            print(single_number)
            _out += str(single_number)
        else:
            _out += i[1]
    return _out


print(get_index_vowel("replace this"))
