from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/Hello2")
def hello_world2():
    return "Helllloooo, World!!"

@app.route("/Hello3")
def hello_world3():
    return "Helllllloooooo, World!!!"

@app.route("/Hello4")
def hello_world4():
    return "Helllllllloooo, World!!!!"
    
if __name__=="__main__":
    app.run(host="0.0.0.0")