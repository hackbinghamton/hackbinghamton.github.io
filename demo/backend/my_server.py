from flask import Flask, request
app = Flask("my_server")

@app.route("/")
def home():
    return "<html><h1>Hello World</h1></html>"


@app.route("/name")
def name():
    personName = request.args["person"]
    return "Hello " + personName + "!"


app.run(host='0.0.0.0', debug=True)
