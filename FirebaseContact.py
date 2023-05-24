import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # connecting to firestore
firebase = firebase.FirebaseApplication('https://DUNGEONIA.firebaseio.com', None)

userStr = "User"


def createUser(userName,characterJSON):
    try:
        db.collection(userStr).document(userName).set(
            {"character":characterJSON}
        )
    except Exception as ex:
        template = "Cant create user in database. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

def readCharacter(userName):
    try:
        character = db.collection(userStr).document(userName).get()
        if(character != None and character.exists()):
            return character
        else:
            return None
    except Exception as ex:
        template = "Cant read user in database. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    

def updateCharacter(userName,characterJSON):
    try:
        character = db.collection(userStr).document(userName).update(
            {"character":characterJSON}
        )
    except Exception as ex:
        template = "Cant update user in database. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

