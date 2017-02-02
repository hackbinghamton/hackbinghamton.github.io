from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

q = []

@app.route("/")
async def index(request):
    msg = {"message": request.args.get("Body"), "number": request.args.get("From")}
    q.append(msg)
    print(q)
    response = json({"sanicresponse": "ok"})
    return response


@app.route("/pop")
async def pop(request):
    global q
    temp = q
    q = []
    response = json(temp)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response



app.run(host="0.0.0.0", port=8000)
