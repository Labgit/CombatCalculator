

class Item:

    def __init__(self, itemType, **kwargs):

        # enum from Types.TypeItem
        self.itemType = itemType

        # enum from Types.TypeArmor
        self.armorType = kwargs.pop('armorType', None)

        # enum from Types.TypeWeapon
        self.weaponType = kwargs.pop('weaponType', None)

        # enum from Types.TypeTurn
        self.turnType = kwargs.pop('turnType', None)

        # description of the item from kwargs
        self.description = kwargs.pop('description', None)

        # weight of the item from kwargs
        self.weight = kwargs.pop('weight', None)

        # Dice object defining attack if item has attack
        self.damageDice = kwargs.pop('damageDice', None)

        # if item does damage, enum from Types.TypeDamage
        self.damageType = kwargs.pop('damageType', None)

        # if item has attack that can be countered with saving
        # throw, this is the number that the roll has to beat
        self.difficultyClass = kwargs.pop('difficultyClass', None)

        # stat for ability modifier that will effect saving throw
        self.savingStat = kwargs.pop('savingStat', None)

        # if item has action that requires range, parameter should
        # be provided in kwargs
        self.range = kwargs.pop('range', None)

        # the properties below define how this item can be used
        # when casting a spell, if a spell requires certain
        # components. If a spell requires a material (a physical
        # substance that would be used and expended, then isMaterial
        # would be true.

        self.isMaterial = kwargs.pop('isMaterial', False)
        self.isFocus = kwargs.pop('isFocus', False)
        self.isDivineFocus = kwargs.pop('isDivineFocus', False)
