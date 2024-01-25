from flask import Flask, render_template
from flask_socketio import SocketIO
from tools.returnJsonFile import getQuestionsJson
import uuid


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/phone')
def renderPhone():
    userId = str(uuid.uuid4())
    print(f"User (id: {userId}) has joined!")
    return render_template('phoneView.html', id=userId)

@app.route('/pcView')
def renderPc():
    return render_template('pcView.html')

@socketio.on("startQuiz")
def sendQuestion():
    socketio.emit("sendQuestions", getQuestionsJson())

@socketio.on('answer')
def getAnswer(data):
    print(f"User {data['userId']} answered: {data['answer']}")

@socketio.on('nextQuestion')
def nextQuestion(data):
    socketio.emit('nextQuestion', {"questionId" : data["id"], "base": getQuestionsJson()})

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=5000 , debug=True)
