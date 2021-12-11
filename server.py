from types import MethodType
from flask import Flask, request
from flask_cors import CORS
import hira


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
app.after_request(after_request)
CORS(app, supports_credentials=True)


@app.route('/', methods=['POST'])
def tran():
    orig = request.json.get("orig")
    orig_list = orig.split("\n")
    print("orig", orig_list)
    hira_list = hira.kanji2moe(orig_list)
    res = "\n".join(hira_list)
    print("res", hira_list)
    print("res", res)
    return {"hira": res}

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=41401,
        debug=True
    )
