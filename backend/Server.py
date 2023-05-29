from flask import Flask
from Adventurer import createCharacter,playerConnect,StartAdventure,NextTurn,getCharacter
from flask import request
from flask_cors import CORS,cross_origin
from flask.helpers import send_from_directory

app = Flask(__name__,static_folder='./frontend/build',static_url_path='')


@app.route('/api',methods=["GET"])
@cross_origin
def index():
    return{
        "tutorial":"Flask react Heroku"
    }

@app.route("/home")
@cross_origin
def home():
    return {"response":"Hello! this is the main page <h1>HELLO<h1>"}

@app.route("/tryLogin",methods=["POST"], strict_slashes=False)
@cross_origin
def tryLogin():
    userName = request.json['userName']
    return playerConnect(userName)

@app.route("/createCharacter",methods=["POST"], strict_slashes=False)
@cross_origin
def createCharacterAPI():
    characterDescription = request.json['characterDescription']
    return createCharacter(characterDescription)

@app.route("/getCharacter")
@cross_origin
def getCharacterAPI():
    return getCharacter()

@app.route("/startAdventure",methods=["POST"], strict_slashes=False)
@cross_origin
def startAdventureAPI():
    adventureDescription = request.json['adventureDescription']
    return StartAdventure(adventureDescription)

@app.route("/nextTurn",methods=["POST"], strict_slashes=False)
@cross_origin
def nextTurnAPI():
    userEventDescription = request.json['userEventDescription']
    return NextTurn(userEventDescription)

@app.route('/')
@cross_origin
def serve():
    return send_from_directory(app.static_folder,'index.html')

if __name__ == "__main__":
    app.run()