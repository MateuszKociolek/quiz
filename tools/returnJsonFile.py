import json

def getQuestionsJson():
    with open("questions.json", "r" ,encoding='utf-8') as js:
        jsonToReturn = json.load(js)
    return jsonToReturn