import firebase
import IAContact
from Character import Character


firebaseConfig = '''{
  apiKey: "AIzaSyBhaNwwTFDvdGx44D7PQYiObdRBAW6trf0",
  authDomain: "dungeonia-deeec.firebaseapp.com",
  projectId: "dungeonia-deeec",
  storageBucket: "dungeonia-deeec.appspot.com",
  messagingSenderId: "105276791363",
  appId: "1:105276791363:web:087cbfac44ca4962b692f6"
}'''

turnsInAdventure = 5
adventure = ""
#Use a prompt to get the main sentence of the adventure to add it to the player Journal
#Updaate the player Journal/Description/Image




#Next Event (The IA generate the next Event and the player reaacts to it. It modifies the course of the history)

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
def createCharacter(username,characterName,userPrompt):
    characterDescription = IAContact.get_response(f"The Character name is: {characterName} "+userPrompt+userCreationPrompt1,username)
    characterTraits = IAContact.get_response(characterDescription+userCreationPrompt2,username)
    imagePrompt = characterDescription
    if len(imagePrompt) > 1000:
        imagePrompt = imagePrompt[0:1000]
    image = IAContact.get_image(imagePrompt,username)
    createdCharacter = Character(characterName,characterDescription,image)
    print(characterTraits)
    createdCharacter.setTraits(characterTraits)
    createdCharacter.printUser()
    #Save character in the database

#Get the player from the database
def playerConnect(username):
    #from username get the character from database
    #return player
    pass

#Create the main history. Then use this history to describe the events to interact with the player.
adventureSAUCE = """
Create a D&D history using the previous description of the adventure. Make the history engaging
history:{
    allies:
    nameOfThePlaceWhereTheAdventureDevelop:
    enemies:
    mainQuest:
    inventory:
}
"""

#Create a new history with the player request or random (params to adjust the history).
def createAdventure():
    characterDescription = IAContact.get_response(f"The Character name is: {characterName} "+userPrompt+userCreationPrompt1)
    pass

createCharacter("Bonito","Bobito","He is a brave dog knight that lives in the forest, he eat everything that he encounters in there. Had an injury in his leg but he is a good fighter.")