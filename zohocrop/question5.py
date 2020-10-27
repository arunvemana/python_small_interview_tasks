def family_tree(input_list: list):
    _temp_dict = {}
    for i in input_list:
        if i[1] not in _temp_dict:
            _temp_dict[i[1]] = []
            _temp_dict[i[1]].append(i[0])
        else:
            _temp_dict[i[1]].append(i[0])

    return _temp_dict


def grandchild_count(tree: dict, grandfather_name: str):
    if grandfather_name in tree:
        # taking his child from the tree.
        child = tree[grandfather_name]
        # length of the child-- child gives the grandchildern count.
        try:
            return_out = len(tree[child[0]])
        except KeyError:
            return_out = "no grandchildern for him"
    else:
        return_out = "He is not in this family"
    return return_out

sample_input = [["luke", 'shaw'], ["wayne", "rooney"],
                ["rooney", "ronaldo"], ["shaw", "rooney"]]
input_list = []
for i in range(0, int(input(
                            "Enter the count of the array as input:"))):
    """give input sample is--> luke,shaw  """
    input_list.append(input(
                        'give the strings with comma seperate:-').split(','))

grandfather_name = input("Provide the Grand Father name:")
print(family_tree(input_list))
tree = family_tree(sample_input)
print(grandchild_count(tree, grandfather_name))

# Below is the Excuting input and output
# Enter the count of the array as input:4
# give the strings with comma seperate:-luke,shaw
# give the strings with comma seperate:-wayne,rooney
# give the strings with comma seperate:-rooney,ronaldo
# give the strings with comma seperate:-shaw,rooney
# {'shaw': ['luke'], 'rooney': ['wayne', 'shaw'], 'ronaldo': ['rooney']}
# 2
