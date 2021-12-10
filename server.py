from types import MethodType
from flask import Flask, request
import hira


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def tran():
    print(request)
    return "2"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=41401,
        debug=True
    )
