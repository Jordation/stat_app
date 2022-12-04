from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from static.myScripts.Format_MatchOBJ import createToken

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



@app.route('/loadStats', methods=['POST'])
def loadStats():
    req = str(request.get_json(force=True)['url'])
    y_field = str(request.get_json(force=True)['y_field'])
    print(y_field)
    if checkLink(req):
        url = req
        token = createToken(url)['data']
        xy = returnXY({'mapnum': '1',
                       'x': 'Player',
                       'y': y_field},
                      token)

        params = {
            'x': xy[0],
            'y': xy[1],
            'type': 'bar',
        }
        return params
    else:
        return


if __name__ == '__main__':
    app.run()
