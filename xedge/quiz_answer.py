from typing import List

data = [
['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ], ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'], ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam'],
 ]

def participate_daily(data:List[list]):
    _out = set()
    for j in data[0]:
        daily = True
        for i in data[1:]:
            if j not in i:
                daily = False
                break
        if daily:
            _out.add(j)
    return list(_out)

def participate_once(data:List[list]):
    _out = {}
    for day in data:
        for name in day:
            if _out.get(name):
                _out[name] = _out[name]+1
            else:
                _out[name] = 1
    return list(dict(filter(lambda x:x[1]==1,_out.items())).keys())


def participate_firstDay(data:List[list]):
    _out = set()
    for name in data[0]:
        only_once = True
        for day in data[1:]:
            if name in day:
                only_once = False
        if only_once:
            _out.add(name)
    return list(_out)


if __name__ == '__main__':
    print("participated daily",participate_daily(data))
    print("participated only once",participate_once(data))
    print("participated on the first day and never participated again",participate_firstDay(data))