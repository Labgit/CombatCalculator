import Types


class Character:

    def __init__(self, charClass, charLevel):
        self.charName = ""
        self.charRace = ""
        self.charBackground = ""
        self.charClass = charClass
        self.charAlignment = Types.TypeAlignment.Neutral
        self.charLevel = charLevel

        '''I thin that we need to combine stats generated
        from the class of the character as well as the benefits
        granted from the chosen race. Those combined stats will
        form the final stat listed here'''

        self.charExperience = 0
        self.charStrength = 0
        self.charDexterity = 0
        self.charConstitution = 0
        self.charIntelligence = 0
        self.charWisdom = 0
        self.charCharisma = 0



