from flask import Flask, request, jsonify, make_response
from typing import List
import markdown
import markdown.extensions.fenced_code

app = Flask(__name__)


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


@app.route('/relationship', methods=['POST'])
def relationship():
    output = {}
    if request.json and request.json['node_ids']:
        get_info = request.json
        for node_id in get_info['node_ids']:
            output[node_id] = sorted(
                child_nodes_extract(get_info['relation'], node_id) + [node_id])
        return make_response(jsonify(output), 200)
    output['Error'] = "You have to send data"
    return make_response(jsonify(output), 404)


@app.route('/about', methods=['GET'])
def about():
    return make_response(
        jsonify({"info": "By Arun Sai vemana\n mobile:+91 9705504343"}), 200)


@app.route('/')
def home():
    readme_file = open("./readme.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string


if __name__ == '__main__':
    app.run(port=5001, debug=True)
