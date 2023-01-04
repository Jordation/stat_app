from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from stat_api_scripts.QuereyV2 import processQuerey
app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

def checkLink(link):
    if 'vlr.gg' in link:
        return True
    else:
        return False

def returnXY(fields, data):
    def forEach(inner_data, param):
        t1 = [i[param] for i in inner_data['t1_c']]
        t2 = [i[param] for i in inner_data['t2_c']]
        t1.extend(t2)
        return t1

    mapnum = f"m{fields['mapnum']}_data"
    ret_x = forEach(data[mapnum], fields['x'])
    ret_y = forEach(data[mapnum], fields['y'])
    return ret_x, ret_y



@app.route('/processQuereyFromClient', methods=['POST'])
def processQuereyFromClient():
    
    querey = request.get_json(force=True)["querey"]
    print(querey)
    graph_data = processQuerey(querey)
    
    return jsonify(graph_data)


@app.route('/t3appa', methods=['POST'])
def t3appa():
    print(request.get_json(force=True)['data'])
    
    return jsonify({'data': 'plugged and played'})


@app.route('/randQuerey', methods=['POST'])
def randQuerey():
    print(request.get_json(force=True)["querey"])
    res = processQuerey()

    return jsonify(res)

if __name__ == '__main__':
    app.run()
