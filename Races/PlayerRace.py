import Types


class PlayerRace:

    def __init__(self):

        self.abilityScoreIncrease = {
            Types.TypeStat.Charisma: 0,
            Types.TypeStat.Constitution: 0,
            Types.TypeStat.Dexterity: 0,
            Types.TypeStat.Intelligence: 0,
            Types.TypeStat.Strength: 0,
            Types.TypeStat.Wisdom: 0
        }

        # these are abilities that take up an action
        self.actives = []

        # these are abilities that modify stats
        self.passives = []

        # these abilities honestly shouldn't effect much
        self.senses = []
        self.resiliences = []
        self.proficiencies = []
        self.languages = []
        self.speed = 0

        self.descriptionAge = ""
        self.descriptionAlignment = ""
        self.descriptionSize = ""
