from flask import Flask, g;

app = Flask(__name__);

# 다음은 모든 요청에 앞서 수행하는 함수다.
@app.before_request
def before_request():
    g.username = 'Michael'; # 어디서든 사용할 수 있는 global에 
                            # username이라는 이름으로 'Michael'저장했다.
# g는 global이다. 이것은 자바의 application과 같다.
# application의 자료형은 ServletContext이며 이것이 global이다.
@app.route("/test")
def test():
    return "Hello Flask!";

@app.route("/ex")
def ex():
    return "<h1>go for it! INCREPAS!</h1>";

@app.route("/ex1")
def ex1():
    str = '''
        <h1>연습입니다.</h1>
    ''';
    return str;

@app.route("/test2")
def test2():
    return "화이팅~ "+getattr(g, 'username');