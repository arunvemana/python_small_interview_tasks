# Required Packages
import os
from itertools import islice


def words_count(filename: str, output_name: str = "wc_report.txt"):
    total_count = 0
    unique = {}
    try:
        if os.path.isfile(filename):
            print("filename exist")
            # reading the file name
            with open(filename, 'r') as data:
                file_data = data.readlines()

            for line in file_data:
                words = line.lower().split()
                total_count = total_count + len(words)
                for word in words:
                    word = ''.join(w for w in word if w.isalnum())
                    if unique.get(word):
                        unique[word] = unique[word] + 1
                    else:
                        unique[word] = 1
            # sorting the dict on the values in reverse order.
            sorted_dict = {k: v for k, v in sorted(unique.items(),
                                                   key=lambda item: item[1], reverse=True)}
            data_to_write = "Decreased order of words and there count\n"
            # taking only first 10 records.
            for value in list(islice(sorted_dict.items(), 10)):
                data_to_write = data_to_write + f'{value[0]}:{value[1]}\n'

                # taking the unique words count from the dict
            data_to_write = f'{data_to_write}Total No.of words = {total_count}\n' \
                            f'Total No.of Unquie Words = {len(unique.keys())}'

            with open(output_name, 'w') as write_file:
                write_file.write(data_to_write)

        else:
            raise Exception("Filename is not exist")
    except Exception as _:
        print(_)


words_count("test1.txt")
