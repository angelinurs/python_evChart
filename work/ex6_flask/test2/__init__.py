from flask import Flask, jsonify;
from flask_cors import CORS;

app = Flask(__name__);
CORS(app);

@app.route("/")
def main():
    str = '''
        <h1>인크레파스 교육센터</h1>
        <h2>개발자를 꿈꾸는 곳</h2>
        <h2>너도 할 수 있어</h2>
    ''';
    return str;