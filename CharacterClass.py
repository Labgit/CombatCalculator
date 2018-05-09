import Types
import Character
import Dice


class CharacterClass:

    def __init__(self, character, classType):
        self.character = character
        self.classType = classType

    def applyClassTemplate(self):
        if self.classType == Types.TypeClass.Barbarian:

            self.character.proficiencies.append(Types.TypeArmor.Light)
            self.character.proficiencies.append(Types.TypeArmor.Medium)

            # apply hit die for Barbarian
            self.character.hitDie.add(12)

            # modify stat priority
            self.character.setStatPriority(Types.TypeStat.Strength, 0)
            self.character.setStatPriority(Types.TypeStat.Constitution, 1)
            self.character.setStatPriority(Types.TypeStat.Dexterity, 2)
            self.character.setStatPriority(Types.TypeStat.Wisdom, 3)
            self.character.setStatPriority(Types.TypeStat.Charisma, 4)
            self.character.setStatPriority(Types.TypeStat.Intelligence, 5)

            # add warrior saving throws
            self.character.savings.append(Types.TypeStat.Strength)
            self.character.savings.append(Types.TypeStat.Constitution)

            self.skills = []

            

