import random
import time    
import json

random.seed(time.time())

#User language traduccion al idioma del usuario usando IA.
experienceRangeModifier = 10
characterUpgradeModifier = 2

class Character:
    def __init__(self,name,description,image) -> None:
        self.name = name
        self.level = 1
        self.description = description
        self.experience = 0
        self.experieceToNextLevel = 100
        self.numberOfAdventures = 0
        self.currentImage = image
        #Add the first image to the image list
        self.images = [image]
        self.nextCharacterUpgrade = 30
        self.journal = ""
        self.abilities = ""
        self.inventory = ""
        self.skills = ""
        self.mainWeapon = ""
        self.goals = ""
        self.fears = ""
        self.personality = ""

    def __init__(self,input) -> None:
        self.name = input.get("name")
        self.level = input.get("level")
        self.description = input.get("description")
        self.experience = input.get("experience")
        self.experieceToNextLevel = input.get("experieceToNextLevel")
        self.numberOfAdventures = input.get("numberOfAdventures")
        self.currentImage = input.get("image")
        #Add the first image to the image list
        self.images = input.get("images")
        self.nextCharacterUpgrade = input.get("nextCharacterUpgrade")
        self.journal = input.get("journal")
        self.abilities = input.get("abilities")
        self.inventory = input.get("inventory")
        self.skills = input.get("skills")
        self.mainWeapon = input.get("mainWeapon")
        self.goals = input.get("goals")
        self.fears = input.get("fears")
        self.personality = input.get("personality")

    def stringToPrompt(self):
        return f'''Name:{self.name} LEVEL:{self.level} EXP:{self.experience} ADVENTURES:{self.numberOfAdventures}
                Experience to Next Level: {self.experieceToNextLevel}
                Description:{self.description} Inventory:{self.inventory} Journal:{self.journal}
                Abilities:{self.abilities} MainWeapon:{self.mainWeapon} Skills:{self.skills}
                Goals:{self.goals} Fears:{self.fears} Personality:{self.personality}'''

    def printUser(self):
        print(f"""Name:{self.name} LEVEL:{self.level} EXP:{self.experience} ADVENTURES:{self.numberOfAdventures}
                Experience to Next Level: {self.experieceToNextLevel}
                Description:{self.description}
                Image:{self.currentImage}\n""")
        
    def printStats(self):
        print(f"""Name:{self.name} LEVEL:{self.level} EXP:{self.experience} ADVENTURES:{self.numberOfAdventures}\n"
              Experience to Next Level: {self.experieceToNextLevel}\n""")
        
    def completeAdventure(self,journalEntry):
        self.journal += journalEntry
        self.numberOfAdventures += 1
        self.experience += random.randint(self.experieceToNextLevel-experienceRangeModifier,self.experieceToNextLevel+experienceRangeModifier)
        if(self.experience >= self.experieceToNextLevel):
            self.levelUp()

    def levelUp(self):
        #Use the image generator each 10 levels to upgrade the photo.
        self.level += 1
        self.experience -= self.experieceToNextLevel
        if(self.level >= self.nextCharacterUpgrade):
            #Generate an updated image
            #Generate an updated description with the hournal entries
            self.nextCharacterUpgrade += self.nextCharacterUpgrade/2 * 3
    
    def levelUpMessage(self):
        print(f"Congratulations you LVL UP")
        self.printStats()
    
    def setTraits(self,jsonTraits):
        try:
            traits = json.loads(jsonTraits)
        except:
            print("Error with JSON LOAD")
        try:
            self.abilities = traits["abilities"]
            self.inventory = traits["inventory"]
            self.skills = traits["skills"]
            self.mainWeapon = traits["mainWeapon"]
            self.goals = traits["goals"]
            self.fears = traits["fears"]
            self.personality = traits["personality"]
        except:
            print("Error reading the dictionary")
        
    def toJSON(self):
        return json.dumps(self.__dict__)