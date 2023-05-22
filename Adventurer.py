import IAContact
from Character import Character

turnsInAdventure = 5
adventure = ""

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

#Use a prompt to get the main sentence of the adventure to add it to the player Journal
#Updaate the player Journal/Description/Image


#Create a new history with the player request or random (params to adjust the history).
def createAdventure():
    #get_response()
    pass

#Next Event (The IA generate the next Event and the player reaacts to it. It modifies the course of the history)

#Create a new description for the player when he levels using the journal
#Create a new image for the player when he levels using the journal


#Character creation
#Create a JSON to store some traits for the caracter
userCreationPrompt1 = "Create a fantastic new character for D&D that use the previous description as base Add some interesting details"
userCreationPrompt2 = """fill the JSON using the text
history:{
    abilities:
    inventory:
    skills:
    mainWeapon:
    goals:
    fears:
    personallity:
}
"""
def createCharacter(characterName,userPrompt):
    characterDescription = IAContact.get_response(f"The Character name is: {characterName} "+userPrompt+userCreationPrompt1)
    characterTraits = IAContact.get_response(characterDescription+userCreationPrompt2)
    imagePrompt = characterDescription
    if len(imagePrompt) > 1000:
        imagePrompt = imagePrompt[0:1000]
    image = IAContact.get_image(imagePrompt)
    createdCharacter = Character(characterName,characterDescription,image)
    createdCharacter.printUser()

createCharacter("Bobito","He is a brave dog knight that lives in the forest, he eat everything that he encounters in there. Had an injury in his leg but he is a good fighter.")