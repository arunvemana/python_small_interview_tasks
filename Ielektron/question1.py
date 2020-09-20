import re

def check_parentheses(expr):
    s = []
    for c in expr:
        if c in '(':
            s.append(c)
        elif c in ')':
            if not len(s):
                break
            else:
                s.pop()
    else:
        return not len(s)
    return False
    

# this test case example will fail because give sample
# output main condition has dict has value not list 
# so not consider this test case "((A=2 && B=3) || (C=4 && D=5) && (C=4 && D=5))"

testing_inputs = ["((A=2 && B=3) || (C=4 && D=5))",
"((A=5 && B=3 || (C=4 && D=5))","A=6 && B=3","(A=2 && B=3","(A=10 && B=13) && (C=4 && D=5)"]
temp_output= {}

def _And_Or(condition_str:str):
    if condition_str == '||':
        return "or"                     
    elif condition_str =='&&':
        return "and"
def _key_value(key_value_str :str):
    _key_value_split = key_value_str.split('=')
    return [_key_value_split[0],_key_value_split[1]]

for index,i in enumerate(testing_inputs):
    if check_parentheses(i):
        temp_output[i]={}
        temp_output[i]["query"] = {}
        if re.findall(r'(\({2})',i) or re.findall(r'(\){1}\s\W\W\s\({1})',i): # check inside sub condition is there not. 
            # print(re.findall(r'(\){1}\s\W\W\s\({1})',i))
            for value in re.findall(r'(\){1}\s\W\W\s\({1})',i):
                _temp = value[1:-1].strip()
                condition_str = _And_Or(_temp)
                temp_output[i]["query"][condition_str]=[]
                # working on inside condition
                for index_split, value in enumerate(re.split(r'\){1}\s\W\W\s',i)):
                    _temp = value.replace('(','').replace(')','')
                    _sub_split = re.split(r'(\s\W\W\s)',_temp)
                    sub_condition_str = _And_Or(_sub_split[1].strip())
                    condition_value1 = _key_value(_sub_split[0])
                    condition_value2 = _key_value(_sub_split[2])
                    _sub_dict = {sub_condition_str:{condition_value1[0]:condition_value1[1],condition_value2[0]:condition_value2[1]}}
                    temp_output[i]["query"][condition_str].append(_sub_dict)

        else:
            # just one parent condition is there
            # only one condition test case because output structure has dict not list
            value = re.findall(r'\s\W\W\s',i)
            _temp = value[0][1:-1].strip()
            condition_str = _And_Or(_temp)
            temp_output[i]["query"][condition_str]=[]
            # divide key and value 
            condition_split = i.split(value[0].strip())
            div_key_value1 = _key_value(condition_split[0].strip())
            div_key_value2 = _key_value(condition_split[1].strip())
            temp_output[i]["query"][condition_str]={div_key_value1[0]:div_key_value1[1], div_key_value2[0]:div_key_value2[1]}

    else:
        temp_output[i] = {"error":"SYNTAX INVALID"}

print("Total output:-")
print(temp_output)
print("-"*20)
print("printing each test case and it's value")
for i in temp_output.keys():
    print(f"test_case :-{i} output:-{temp_output[i]}")


