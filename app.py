import json
from flask import Flask

app = Flask(__name__)

global_list = []

def handler(action, parameters):
    global global_list
    if action == "item.add":
        global_list.append(parameters['item'])
    elif action == "item.remove":
        global_list = [x for x in global_list if x != parameters['item']]

    return global_list


def parse(request):
    body = json.loads(request)
    return body["result"]["action"], body["result"]["parameters"]


@app.route('/', methods=['post', 'get'])
def index():
    return handle()
