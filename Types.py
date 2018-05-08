from enum import Enum


class TypeClass(Enum):
    Unassigned = -1
    Barbarian = 0
    Bard = 1
    Cleric = 2
    Druid = 3
    Fighter = 4
    Monk = 5
    Paladin = 6
    Ranger = 7
    Rogue = 8
    Sorcerer = 9
    Warlock = 10
    Wizard = 11


class TypeRace(Enum):
    Dwarf = 0
    Elf = 1
    Halfling = 2
    Human = 3
    DragonBorn = 4
    Gnome = 5
    HalfElf = 6
    HalfOrc = 7
    Tiefling = 8


# only a few of the races above have subraces
class TypeSubRace(Enum):
    Unassigned = -1
    HillDwarf = 0
    MountainDwarf = 1
    HighElf = 2
    WoodElf = 3
    DarkElf = 4
    LightFoot = 5
    Stout = 6
    ForestGnome = 7
    RockGnome = 8


class TypeAlignment(Enum):
    LawfulGood = 0
    NeutralGood = 1
    ChaoticGood = 2
    LawfulNeutral = 3
    Neutral = 4
    ChaoticNeutral = 5
    LawfulEvil = 6
    NeutralEvil = 7
    ChaoticEvil = 8


class TypeStat(Enum):
    Unassigned = -1
    Charisma = 0
    Constitution = 1
    Dexterity = 2
    Intelligence = 3
    Strength = 4
    Wisdom = 5


# This need to be expanded
class TypeArmor(Enum):
    Light = 0
    Medium = 1
    Heavy = 2


# This need to be expanded
class TypeWeapon(Enum):
    SimpleMelee = 0
    SimpleRange = 1
    MartialMelee = 2
    MartialRange = 3

class TypeSense(Enum):
    DarkVision = 0
    BlindSight = 1
