from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import uuid


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/phone')
def renderPhone():
    return render_template('phoneView.html', id=generateUserId())

@app.route('/pcView')
def renderPc():
    return render_template('pcView.html')

@socketio.on("startQuiz")
def sendQuestion():
    qs = getQuestionsJson()
    for i in range(len(qs)):
        print(qs[i]['question'])

@socketio.on('answer')
def getAnswer(data):
    print(f"Answer is: {data['answer']}")

def getQuestionsJson():
    with open("questions.json", "r") as js:
        jsonToReturn = json.load(js)
    return jsonToReturn

def generateUserId():
    return str(uuid.uuid4())

if __name__ == "__main__":
    socketio.run(app, debug=True)