import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # connecting to firestore
firebase = firebase.FirebaseApplication('https://DUNGEONIA.firebaseio.com', None)


def createUser(userName,characterJSON):
    try:
        db.collection('User').document(userName).set(
            {"character":characterJSON}
        )
    except:
        print("Error creating character in the database")

def readCharacter(userName):
    try:
        character = db.collection('User').document(userName).get()
    except:
        print("Error reading character in the database")
    return character

def updateCharacter(userName,characterJSON):
    try:
        character = db.collection('User').document(userName).update(
            {"character":characterJSON}
        )
    except:
        print("Error updating character in the database")
    return character

createUser("Polluelo","xdddddd")