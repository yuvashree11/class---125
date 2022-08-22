
from flask import Flask,jsonify,request
app= Flask(__name__)
task = [
{
'id':1,
'title':'learn python',
'description':'find good tutoriale',
'done':False
}
]
@app.route("/")
def HELLO_WORLD():
 return 'HELLO WORLD'
@app.route("/add-data",methods = ["POST"])
def add_task():
 if not request.json:
  return jsonify({
   "status":"error",
   "message":"provide the data"},400)
 tasks = {
     'id': 2,
     'title': 'learn python',
     'description': 'find good tutoriale',
     'done': False}

 task.append(tasks)
 return jsonify({
   "status":"success",
   "message":"task added"})
@app.route("/get-data")
def get_task():
    return jsonify({
       "data":task
    })
if (__name__ == "__main__"):
    app.run(debug = True)