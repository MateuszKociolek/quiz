from flask import Flask, render_template
from flask_socketio import SocketIO
from tools.usefullFunctions import *
import uuid

app = Flask(__name__)
socketio = SocketIO(app)

playersPoints = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/phone')
def renderPhone():
    userId = str(uuid.uuid4())
    print(f"User (id: {userId}) has joined!")
    newRecord = {
        "username" : "testTest",
        "points" : 0
    }
    playersPoints[userId] = newRecord

    return render_template('phoneView.html', id=userId)

@app.route('/pcView')
def renderPc():
    return render_template('pcView.html')

@socketio.on("startQuiz")
def sendQuestion():
    playersPoints = {}
    socketio.emit("sendQuestions", getQuestionsJson())

@socketio.on("setUsername")
def setUsername(data):
    playersPoints[data["id"]]["username"] = data["username"]
    # printPoints(playersPoints)


@socketio.on('answer')
def getAnswer(data):
    # print(f"User {data['userId']} answered: {data['answer']}")
    if data['answer']:
        if data['userId'] in playersPoints:
            playersPoints[data['userId']]["points"] += 100


@socketio.on("end")
def endOfQuiz():
    socketio.emit("end", sortJson(playersPoints))


@socketio.on('nextQuestion')
def nextQuestion(data):
    socketio.emit('nextQuestion', {"questionId" : data["id"], "base": getQuestionsJson()})
    # printPoints(playersPoints)

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=5000 , debug=True)
