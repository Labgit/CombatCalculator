import Dice
import Types
import CharacterClass

class Character:

    def __init__(self, classType, raceType, level=1):

        self.name = "TestMe"
        self.background = "Background info goes here..."
        self.age = 20
        self.alignment = Types.TypeAlignment.Neutral

        self.level = level
        self.characterClass = CharacterClass.CharacterClass(self,classType)

        # individual class will assign the HitDie
        self.hitDie = Dice.Dice()

        # primary ability scores
        self.primaries = []

        # stats for saving throws
        self.savings = []

        # proficiencies for armor and weapons
        self.proficiencies = []

        # list of items include weapons and armor
        self.items = []

        # add to hit rolls
        self.proficiencyBonus = 0

        # different stats
        self.hitPoints = 0
        self.armorClass = 0
        self.experience = 0

        # ability score by stat
        self.abilityScoreByStat = {
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

        # stat by priority
        self.statByPriority = {
            0: Types.TypeStat.Strength,
            1: Types.TypeStat.Dexterity,
            2: Types.TypeStat.Constitution,
            3: Types.TypeStat.Intelligence,
            4: Types.TypeStat.Wisdom,
            5: Types.TypeStat.Charisma
        }

        # modify stat priority to match the character's class and other things come with the class
        self.characterClass.applyClassTemplate()

        # now that stat priorities have been reassigned, auto generate and assign ability scores
        self.autoAssignAbilityScores()

        # now that ability scores have been assigned, let's assign hit points
        self.autoAssignHitPoints()

    def setProficiencyBonus(self):
        if self.level < 5:
            self.proficiencyBonus += 2
        elif self.level < 9:
            self.proficiencyBonus += 3
        elif self.level < 13:
            self.proficiencyBonus += 4
        elif self.level < 17:
            self.proficiencyBonus += 5
        else:
            self.proficiencyBonus += 6

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
        return self.abilityScoreByStat[abilityType]

    def setAbilityScore(self, abilityType, abilityScore):
        self.abilityScoreByStat[abilityType] = abilityScore

    def autoAssignAbilityScores(self):
        abilityScores = []

        # generate ability score for every stat
        for x in range(len(self.abilityScoreByStat)):
            abilityScores.append(self.generateAbilityScore())

        # sort ability scores from greatest to least
        sorted(abilityScores, key=int, reverse=True)

        # for every priority, get stat and assign ability score
        for priority in range(len(self.statByPriority)):
            stat = self.statByPriority[priority]
            self.abilityScoreByStat[stat] = abilityScores[priority]

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

    # this should be done only after you've generatedAbilityScores and assigned a hit die
    def autoAssignHitPoints(self):
        self.hitPoints = self.generateHitPoints(
            self.level, self.hitDie, self.getAbilityScore(Types.TypeStat.Constitution))

    @staticmethod
    def generateHitPoints(self, level, hitDie, abilityScore):
        points = 0

        for x in range(level):
            points += hitDie.roll() + self.calculateAbilityModifier(abilityScore)

        return points








