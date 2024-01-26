import json

def getQuestionsJson():
    with open("questions.json", "r" ,encoding='utf-8') as js:
        jsonToReturn = json.load(js)
    return jsonToReturn

def printPoints(pointsList):
    for i in pointsList:
        print(pointsList[i]["username"], pointsList[i]["points"])

# Funkcja sortująca na podstawie punktów
def sort_by_points(user):
    return user[1]["points"]

def sortJson(json_data):
    # Posortuj dane na podstawie ilości punktów
    sorted_data = sorted(json_data.items(), key=sort_by_points, reverse=True)

    # Wynik
    return {k: v for k, v in sorted_data}
    