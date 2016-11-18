from flask import Flask, request, render_template, json
from pymongo import MongoClient

app = Flask("mywebsite", template_folder=".")


database_client = MongoClient(
    "mongodb://DBuser:password123@ds139327.mlab.com:39327/hackbudemo"
    )

database = database_client.hackbudemo
collection = database.jack_collection


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/loaditems')
def loaditems():
  final_list = []
  for item_object in collection.find():
    final_list.append(item_object['item'])
  return json.dumps(final_list)

@app.route('/saveitem')
def saveitem():
  item = request.args["item"]
  item_object = {'item': item}
  collection.insert_one(item_object)
  return "item '%s' inserted!" % item


if __name__ == "__main__":
    app.run(debug=True)

