from flask import Flask
from Adventurer import createCharacter,playerConnect,StartAdventure,NextTurn
from flask import request

app = Flask(__name__)

@app.route("/home")
def home():
    return {"response":"Hello! this is the main page <h1>HELLO<h1>"}

@app.route("/tryLogin",methods=["POST"], strict_slashes=False)
def tryLogin():
    userName = request.json['userName']
    return playerConnect(userName)

@app.route("/createCharacter",methods=["POST"], strict_slashes=False)
def createCharacterAPI():
    characterDescription = request.json['characterDescription']
    print(characterDescription)
    return createCharacter(characterDescription)


if __name__ == "__main__":
    app.run()