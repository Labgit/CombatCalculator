import Dice
import Types
import Classes.PlayerClass as pc


class Barbarian(pc.PlayerClass):

    def __init__(self, level):

        # ability scores are generated within the parent class
        # TODO: possibility of of adding the option to go with a default stat set
        super(Barbarian, self).__init__(level, Types.TypeClass.Barbarian)

        # set proficiency bonus
        self._setProficiencyBonus()

        # barbarian hit die = 1d12
        self.hitDie.add(12)


    def _setProficiencyBonus(self):

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

    def _set