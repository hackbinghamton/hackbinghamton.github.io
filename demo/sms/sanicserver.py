from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

q = [] #Global queue will hold incoming messages until they're fetched

@app.route("/") #Twilio requests here to send a new message
async def index(request):
    msg = {"message": request.args.get("Body"), "number": request.args.get("From")}
    q.append(msg)
    print(q) #debug
    response = json({"response": "ok"})
    return response


@app.route("/pop") #Browser requests here to get any new messages
async def pop(request):
    response = json(q)
    response.headers["Access-Control-Allow-Origin"] = "*" #allow demo from local file
    q.clear()
    return response



app.run(host="0.0.0.0", port=8000)

