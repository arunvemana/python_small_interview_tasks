from typing import List, Union

data = [{"parent": "node_1", "child": "node_4"},
        {"parent": "node_2", "child": "node_4"},
        {"parent": "node_3", "child": "node_4"},
        {"parent": "node_4", "child": "node_5"},
        {"parent": "node_4", "child": "node_7"},
        {"parent": "node_6", "child": "node_5"}]


def child_nodes_extract(data: List[dict], node_name: str) -> List:
    output, loop = [], True
    node_names = [node_name]
    child = []
    while loop:
        for node_name in node_names:
            for each_dict in data:
                if each_dict['child'] == node_name:
                    child.append(each_dict['parent'])
            if not child:
                loop = False
            else:
                node_names = child
                output.extend(child)
                child = []

    return output


def relation_data(data: List[dict], node_ids: List[str]):
    output = {}
    for node_id in node_ids:
        output[node_id] = sorted(
            child_nodes_extract(data, node_id) + [node_id])
    return output


print(relation_data(data, ["node_5", "node_7", "node_4"]))
