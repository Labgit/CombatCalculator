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

        # stat priority by stat, this will be reassigned in each class
        self.priorityByStat = {
            Types.TypeStat.Strength: 0,
            Types.TypeStat.Dexterity: 1,
            Types.TypeStat.Constitution: 2,
            Types.TypeStat.Intelligence: 3,
            Types.TypeStat.Wisdom: 4,
            Types.TypeStat.Charisma: 5
        }

        self.statByPriority = {
            0: Types.TypeStat.Strength,
            1: Types.TypeStat.Dexterity,
            2: Types.TypeStat.Constitution,
            3: Types.TypeStat.Intelligence,
            4: Types.TypeStat.Wisdom,
            5: Types.TypeStat.Charisma
        }

    def getStatPriority(self, statType):
        return self.priorityByStat[statType]

    def setStatPriority(self, statType, newPriority):
        # get current stat priority
        currentPriority = self.priorityByStat[statType]

        # unassign stat from priority slot and reset stat priority
        self.statByPriority[self.priorityByStat[statType]] = Types.TypeStat.Unassigned
        self.priorityByStat[statType] = -1

        # get next stat and priority to reassign recursively
        nextStat = self.statByPriority[newPriority]
        nextPriority = newPriority + (-1 if newPriority > currentPriority else 1)

        # assign statType to priority slot
        self.statByPriority[newPriority] = statType

        # assign priority to stat
        self.priorityByStat[statType] = newPriority

        # if we need to shuffle, let's do it
        if nextStat != -1:
            self.setStatPriority(nextStat, nextPriority)

    def getAbilityScore(self, abilityType):
        return self.statMap[abilityType]

    def setAbilityScore(self, abilityType, abilityScore):
        self.statMap[abilityType] = abilityScore

    @staticmethod
    def generateAbilityScore():
        d = Dice.Dice()

        # generate four six sided die
        for side in range(4):
            d.add(6)

        # take the highest three of four rolls
        d.roll()
        highest = d.highestLastRoll(3)

        # return the sum of the highest three rolls
        return sum(highest)

    @staticmethod
    def calculateAbilityModifier(abilityScore):
        return int((abilityScore - 10) / 2)






