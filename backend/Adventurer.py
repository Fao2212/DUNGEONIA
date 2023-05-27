import firebase
import IAContact
import FirebaseContact
import json
from Character import Character

turnsInAdventure = 5
currentTurn = 1
theuser = ""
adventure = ""
character = None

#Create a new description for the player when he levels using the journal
#Create a new image for the player when he levels using the journal


#Character creation
#Create a JSON to store some traits for the caracter
userCreationPrompt1 = "Create a fantastic new character for D&D that use the previous description as base Add some interesting details"
userCreationPrompt2 = """fill the JSON using the text
{
    "abilities":
    "inventory":
    "skills":
    "mainWeapon":
    "goals":
    "fears":
    "personality":
}
"""
#Creation of a character using the user prompt. Generates a description, an image and a new object of Character class to be stored in the DB. 
def createCharacter(userPrompt):
    characterDescription = IAContact.get_response(f"{userCreationPrompt1} The Character name is: {theuser} Character description:{userPrompt}",theuser)
    characterTraits = IAContact.get_response(characterDescription+userCreationPrompt2,theuser)
    imagePrompt = characterDescription
    if len(imagePrompt) > 1000:
        imagePrompt = imagePrompt[0:1000]
    image = IAContact.get_image(imagePrompt,theuser)
    global character
    character = Character(theuser,characterDescription,image)
    print(characterTraits)
    character.setTraits(characterTraits)
    character.printUser()
    #Save character in the database
    return {"created":FirebaseContact.createUser(theuser,character.toJSON())}
    

#Get the player from the database
def playerConnect(providedUsername):
    global theuser
    theuser = providedUsername
    global character
    document = FirebaseContact.readCharacter(theuser) 
    characterJSON = {"exist":False,"character":""}
    if(document != None):
        character = Character.createFromJSON(json.loads(document.get("character")))
        characterJSON = {"exist":True,"character":character.toJSON()}
    return characterJSON


#Create the main history. Then use this history to describe the events to interact with the player.
adventureSAUCE = """
Create a D&D history using the description points provide. Make the history engaging and define the next things into it. Create a paragraph dont divide the text.
    allies,
    nameOfThePlaceWhereTheAdventureDevelop,
    enemies,
    mainQuest
"""

#Use a prompt to get the main sentence of the adventure to add it to the player Journal
#Create a new history with the player request or random (params to adjust the history).
def StartAdventure(userPrompt):
    global currentTurn
    global character
    currentTurn = 1
    global adventure
    adventure = IAContact.get_response(f"{adventureSAUCE} Protagonist of the history:{character.stringToPrompt()} History Initial Plot: {userPrompt}",theuser)
    print(adventure)
    userPrompt = input("Enter next action")
    NextTurn(userPrompt)


eventString = "Create a continuation to this history. Using this caracter information"

#Updaate the player Journal/Description/Image
#Next Event (The IA generate the next Event and the player reaacts to it. It modifies the course of the history)
def NextTurn(playerResponse):
    global currentTurn
    global adventure
    global character
    global theuser
    currentTurn += 1
    characterJson = character.toJSON()
    nextTurnStr = f"{eventString}  character:{characterJson}  current history:{adventure} playerResponse:{playerResponse}"
    adventure += " " + IAContact.get_response(nextTurnStr,theuser)
    if(currentTurn == 5):
        character.completeAdventure(adventure)
        characterJson = character.toJSON()
        FirebaseContact.updateCharacter(theuser,characterJson)
        return
    userPrompt = input("Enter next action")
    NextTurn(userPrompt)

def getCharacter():
    return {"characterInfo":character.toJSON()}