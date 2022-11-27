from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from Format_MatchOBJ import createToken

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False


@app.route('/getstatz', methods=['POST'])
def returnData():
    # from_scraper = ScrapeMatch(request.get_json(force=True)['match_url']).match
    # ready_data = unpackAndJSON(from_scraper)
    # response = jsonify({"data": ready_data})
    searched_map = str(request.get_json(force=True)['map_name'])
    result = stmttest(searched_map)
    # response = jsonify({"data": result})
    response = {'data': result}
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


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
        response = createToken(url)['data']
        xy = returnXY({'mapnum': '1', 'x': 'Player', 'y': y_field}, response)
        params = {
            'x': xy[0],
            'y': xy[1],
            'type': 'bar',
        }
        return params
    else:
        return




@app.route('/populategraph', methods=['POST'])
def funnyGuy():
    response = int(request.get_json(force=True)['graph_amount'])
    return response


if __name__ == '__main__':
    app.run()
