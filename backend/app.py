from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from static.myScripts.Format_MatchOBJ import createToken

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
@app.route('/loadStats', methods=['POST'])
def loadStats():
    print(str(request.get_json(force=True)['url']))
    if checkLink(str(request.get_json(force=True)['url'])):
        url = str(request.get_json(force=True)['url'])
        response = createToken(url)
        return response
    else:
        return


@app.route('/analyse')
def matchToGraphs():
    return


@app.route('/populategraph', methods=['POST'])
def funnyGuy():
    response = int(request.get_json(force=True)['graph_amount'])
    return response


if __name__ == '__main__':
    app.run()
