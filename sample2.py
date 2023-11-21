from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "This is my input from URL {}".format(data)
#Link is https://orange-lawyer-mcgoq.pwskills.app:5000/input_url?x=Bangalore

@app.route("/func2")
def test1():
    a=99*22
    return "Value of a is {}".format(a)
#Link for this is - https://orange-lawyer-mcgoq.pwskills.app:5000/func2

    
if __name__=="__main__":
    app.run(host="0.0.0.0")