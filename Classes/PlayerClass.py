import Dice
import Types


class PlayerClass:

    def __init__(self, level, classType):

        # player class currently set to none
        self.classType = classType

        # player level
        self.level = level

        # individual class will assign the HitDie
        self.hitDie = Dice.Dice()

        # primary abilities
        self.primaries = []

        # stats for saving throws
        self.savings = []

        # add to hit rolls
        self.proficiencyBonus = 0

        # different stats
        self.hitPoints = 0
        self.armorClass = 0

        # stat map: map type stat to stat variable
        self.statMap = {
            Types.TypeStat.Strength: 0,
            Types.TypeStat.Dexterity: 0,
            Types.TypeStat.Constitution: 0,
            Types.TypeStat.Intelligence: 0,
            Types.TypeStat.Wisdom: 0,
            Types.TypeStat.Charisma: 0
        }

        # stat priority, there will be a default setting per class
        # TODO: allow setting stat priority
        self.statPriority = {}

    def getAbilityScore(self, type):
        return self.statMap[type]

    def setAbilityScore(self, type, abilityScore):
        self.statMap[type] = abilityScore

    def generateAbilityScore(self):
        d = Dice.Dice()

        # generate four six sided die
        for side in range(4):
            d.add(6)

        # take the highest three of four rolls
        d.roll()
        highest = d.highestLastRoll(3)

        # return the sum of the highest three rolls
        return sum(highest)

    def getAbilityModifier(self, abilityScore):
        return int((abilityScore - 10) / 2)
