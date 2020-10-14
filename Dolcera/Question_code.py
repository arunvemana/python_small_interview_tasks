# Question 1:-

import itertools

info = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'],
        'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
        'a': ['doc2'], 'developer': ['doc2']}
result = []
len_sort = sorted(data.items(), key=lambda k: len(k[1]))
for k, v in itertools.groupby(len_sort, lambda item: len(item[1])):
    result.extend(sorted(v))
print(result)

# Question 2:-
corpus = {'doc1': 'hello! my name is james',
          'doc2': 'james is a developer'}


def invert(corpus):
    inverted = {}
    for key, value in corpus.items():
        value_split = value.split()
        for each_value in value_split:
            if each_value in inverted:
                inverted[each_value].extend([key])
            else:
                inverted[each_value] = [key]
    return inverted


data = invert(corpus)

# Question 3:-
 # NOT FOUND
 
# Question 4:-
def test_funct(file_name: str):
    filepath = open(file_name)
    while True:
        yield filepath.readline()


var = test_funct('test.txt')
print(next(var))
print(next(var))
print(next(var))

Question 5:-
# pending
