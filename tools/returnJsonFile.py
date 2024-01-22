import json

def getQuestionsJson():
    with open("questions.json", "r") as js:
        jsonToReturn = json.load(js)
    return jsonToReturn