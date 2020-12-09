import requests
import json
def index():
    s = requests.Session()
    resp = json.loads(s.get("https://apibots-937d3.firebaseio.com/Botmanager/Confg.json").text)
    indices = [x for x in resp]
    return resp[indices[0]]