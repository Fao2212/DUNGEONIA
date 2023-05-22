import random
import time    

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