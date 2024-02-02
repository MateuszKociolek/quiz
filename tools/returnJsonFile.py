import json

def getQuestionsJson():
    with open("questions.json", "r" ,encoding='utf-8') as js:
        jsonToReturn = json.load(js)
    return jsonToReturn

def printPoints(pointsList):
    for i in pointsList:
        print(pointsList[i]["username"], pointsList[i]["points"])

def deleteUser(userId, points):
    if userId in points:
        del points[userId]
        return points
    print("No user in file")
