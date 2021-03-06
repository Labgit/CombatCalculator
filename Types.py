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
    Shield = 3


# This need to be expanded
class TypeWeapon(Enum):
    SimpleMelee = 0
    SimpleRange = 1
    MartialMelee = 2
    MartialRange = 3


class TypeTurn(Enum):
    Nothing = 0
    Effect = 1
    Action = 2


class TypeDamage(Enum):
    Acid = 0


class TypeItem(Enum):
    Abacus = 0
    Acid = 1
    Adamantine_Armor = 2
    Alchemists_Fire = 3
    Alchemists_Supplies = 4
    Amulet = 5
    Amulet_of_Health = 6
    Amulet_of_Proof_against_Detection_and_Location = 7
    Amulet_of_the_Planes = 8
    Animated_Shield = 9
    Antitoxin = 10
    Apparatus_of_the_Crab = 11
    Armor_of_Invulnerability = 12
    Armor_of_Vulnerability = 13
    Arrow_of_Slaying = 14
    Arrow_Catching_Shield = 15
    Arrows = 16
    Arrows_1 = 17
    Arrows_2 = 18
    Arrows_3 = 19
    Backpack = 20
    Bag_of_Beans = 21
    Bag_of_Devouring = 22
    Bag_of_Holding = 23
    Bag_of_Tricks = 24
    Bagpipes = 25
    Ball_bearings = 26
    Barrel = 27
    Basic_poison = 28
    Basket = 29
    Battleaxe = 30
    Battleaxe_1 = 31
    Battleaxe_2 = 32
    Battleaxe_3 = 33
    Bead_of_Force = 34
    Bedroll = 35
    Bell = 36
    Belt_of_Dwarvenkind = 37
    Belt_of_Giant_Strength = 38
    Berserker_Axe = 39
    Blanket = 40
    Block_and_tackle = 41
    Blowgun = 42
    Blowgun_1 = 43
    Blowgun_2 = 44
    Blowgun_3 = 45
    Blowgun_Needles = 46
    Book = 47
    Boots_of_Elvenkind = 48
    Boots_of_Levitation = 49
    Boots_of_Speed = 50
    Boots_of_Striding_and_Springing = 51
    Boots_of_the_Winterlands = 52
    Bowl_of_Commanding_Water_Elementals = 53
    Bracers_of_Archery = 54
    Bracers_of_Defense = 55
    Brazier_of_Commanding_Fire_Elementals = 56
    Breastplate = 57
    Breastplate_1 = 58
    Breastplate_2 = 59
    Breastplate_3 = 60
    Breastplate_of_Acid_Resistance = 61
    Breastplate_of_Cold_Resistance = 62
    Breastplate_of_Fire_Resistance = 63
    Breastplate_of_Force_Resistance = 64
    Breastplate_of_Lightning_Resistance = 65
    Breastplate_of_Necrotic_Resistance = 66
    Breastplate_of_Poison_Resistance = 67
    Breastplate_of_Psychic_Resistance = 68
    Breastplate_of_Radiant_Resistance = 69
    Breastplate_of_Thunder_Resistance = 70
    Brewers_Supplies = 71
    Brooch_of_Shielding = 72
    Broom_of_Flying = 73
    Bucket = 74
    Bullseye_lantern = 75
    Burglars_Pack = 76
    Calligraphers_Supplies = 77
    Caltrops = 78
    Candle = 79
    Candle_of_Invocation = 80
    Cape_of_the_Mountebank = 81
    Carpenters_Tools = 82
    Carpet_of_Flying = 83
    Cartographers_Tools = 84
    Censer_of_Controlling_Air_Elementals = 85
    Chain = 86
    Chain_Mail = 87
    Chain_Mail_1 = 88
    Chain_Mail_2 = 89
    Chain_Mail_3 = 90
    Chain_Mail_of_Acid_Resistance = 91
    Chain_Mail_of_Cold_Resistance = 92
    Chain_Mail_of_Fire_Resistance = 93
    Chain_Mail_of_Force_Resistance = 94
    Chain_Mail_of_Lightning_Resistance = 95
    Chain_Mail_of_Necrotic_Resistance = 96
    Chain_Mail_of_Poison_Resistance = 97
    Chain_Mail_of_Psychic_Resistance = 98
    Chain_Mail_of_Radiant_Resistance = 99
    Chain_Mail_of_Thunder_Resistance = 100
    Chain_Shirt = 101
    Chain_Shirt_1 = 102
    Chain_Shirt_2 = 103
    Chain_Shirt_3 = 104
    Chain_Shirt_of_Acid_Resistance = 105
    Chain_Shirt_of_Cold_Resistance = 106
    Chain_Shirt_of_Fire_Resistance = 107
    Chain_Shirt_of_Force_Resistance = 108
    Chain_Shirt_of_Lightning_Resistance = 109
    Chain_Shirt_of_Necrotic_Resistance = 110
    Chain_Shirt_of_Poison_Resistance = 111
    Chain_Shirt_of_Psychic_Resistance = 112
    Chain_Shirt_of_Radiant_Resistance = 113
    Chain_Shirt_of_Thunder_Resistance = 114
    Chalk = 115
    Chest = 116
    Chime_of_Opening = 117
    Circlet_of_Blasting = 118
    Climbers_kit = 119
    Cloak_of_Arachnida = 120
    Cloak_of_Displacement = 121
    Cloak_of_Elvenkind = 122
    Cloak_of_Protection = 123
    Cloak_of_the_Bat = 124
    Cloak_of_the_Manta_Ray = 125
    Club = 126
    Club_1 = 127
    Club_2 = 128
    Club_3 = 129
    Cobblers_Tools = 130
    Common_clothes = 131
    Component_pouch = 132
    Cooks_utensils = 133
    Costume_clothes = 134
    Crossbow_bolt_case = 135
    Crossbow_bolts = 136
    Crowbar = 137
    Crystal = 138
    Crystal_Ball = 139
    Cube_of_Force = 140
    Cubic_Gate = 141
    Dagger = 142
    Dagger_1 = 143
    Dagger_2 = 144
    Dagger_3 = 145
    Dagger_of_Venom = 146
    Dancing_Sword = 147
    Dart = 148
    Dart_1 = 149
    Dart_2 = 150
    Dart_3 = 151
    Decanter_of_Endless_Water = 152
    Deck_of_Illusions = 153
    Deck_of_Many_Things = 154
    Defender = 155
    Demon_Armor = 156
    Dice_set = 157
    Dimensional_Shackles = 158
    Diplomats_Pack = 159
    Disguise_kit = 160
    Dragon_Scale_Mail = 161
    Dragon_Slayer = 162
    Drum = 163
    Dulcimer = 164
    Dungeoneers_Pack = 165
    Dust_of_Disappearance = 166
    Dust_of_Dryness = 167
    Dust_of_Sneezing_and_Choking = 168
    Dwarven_Plate = 169
    Dwarven_Thrower = 170
    Efficient_Quiver = 171
    Efreeti_Bottle = 172
    Elemental_Gem = 173
    Elven_Chain = 174
    Embelm = 175
    Emblem = 176
    Entertainers_Pack = 177
    Eversmoking_Bottle = 178
    Explorers_Pack = 179
    Eyes_of_Charming = 180
    Eyes_of_Minute_Seeing = 181
    Eyes_of_the_Eagle = 182
    Feather_Token = 183
    Figurine_of_Wondrous_Power = 184
    Fine_clothes = 185
    Fishing_tackle = 186
    Flail = 187
    Flail_1 = 188
    Flail_2 = 189
    Flail_3 = 190
    Flame_Tongue = 191
    Flask = 192
    Flute = 193
    Folding_Boat = 194
    Forgery_kit = 195
    Frost_Brand = 196
    Gauntlets_of_Ogre_Power = 197
    Gem_of_Brightness = 198
    Gem_of_Seeing = 199
    Giant_Slayer = 200
    Glaive = 201
    Glaive_1 = 202
    Glaive_2 = 203
    Glaive_3 = 204
    Glamoured_Studded_Leather = 205
    Glass_bottle = 206
    Glassblowers_Tools = 207
    Gloves_of_Missile_Snaring = 208
    Gloves_of_Swimming_and_Climbing = 209
    Goggles_of_Night = 210
    Grappling_hook = 211
    Greataxe = 212
    Greataxe_1 = 213
    Greataxe_2 = 214
    Greataxe_3 = 215
    Greatclub = 216
    Greatclub_1 = 217
    Greatclub_2 = 218
    Greatclub_3 = 219
    Greatsword = 220
    Greatsword_1 = 221
    Greatsword_2 = 222
    Greatsword_3 = 223
    Halberd = 224
    Halberd_1 = 225
    Halberd_2 = 226
    Halberd_3 = 227
    Half_Plate = 228
    Half_Plate_Armor_1 = 229
    Half_Plate_Armor_2 = 230
    Half_Plate_Armor_3 = 231
    Half_Plate_Armor_of_Acid_Resistance = 232
    Half_Plate_Armor_of_Cold_Resistance = 233
    Half_Plate_Armor_of_Fire_Resistance = 234
    Half_Plate_Armor_of_Force_Resistance = 235
    Half_Plate_Armor_of_Lightning_Resistance = 236
    Half_Plate_Armor_of_Necrotic_Resistance = 237
    Half_Plate_Armor_of_Poison_Resistance = 238
    Half_Plate_Armor_of_Psychic_Resistance = 239
    Half_Plate_Armor_of_Radiant_Resistance = 240
    Half_Plate_Armor_of_Thunder_Resistance = 241
    Hammer = 242
    Hammer_of_Thunderbolts = 243
    Hand_Crossbow = 244
    Hand_Crossbow_1 = 245
    Hand_Crossbow_2 = 246
    Hand_Crossbow_3 = 247
    Handaxe = 248
    Handaxe_1 = 249
    Handaxe_2 = 250
    Handaxe_3 = 251
    Handy_Haversack = 252
    Hat_of_Disguise = 253
    Headband_of_Intellect = 254
    Healers_kit = 255
    Heavy_Crossbow = 256
    Heavy_Crossbow_1 = 257
    Heavy_Crossbow_2 = 258
    Heavy_Crossbow_3 = 259
    Helm_of_Brilliance = 260
    Helm_of_Comprehending_Languages = 261
    Helm_of_Telepathy = 262
    Helm_of_Teleportation = 263
    Hempen_rope = 264
    Herbalism_kit = 265
    Hide_Armor = 266
    Hide_Armor_1 = 267
    Hide_Armor_2 = 268
    Hide_Armor_3 = 269
    Hide_Armor_of_Acid_Resistance = 270
    Hide_Armor_of_Cold_Resistance = 271
    Hide_Armor_of_Fire_Resistance = 272
    Hide_Armor_of_Force_Resistance = 273
    Hide_Armor_of_Lightning_Resistance = 274
    Hide_Armor_of_Necrotic_Resistance = 275
    Hide_Armor_of_Poison_Resistance = 276
    Hide_Armor_of_Psychic_Resistance = 277
    Hide_Armor_of_Radiant_Resistance = 278
    Hide_Armor_of_Thunder_Resistance = 279
    Holy_Avenger = 280
    Holy_Water = 281
    Hooded_lantern = 282
    Horn = 283
    Horn_of_Blasting = 284
    Horn_of_Valhalla = 285
    Horseshoes_of_Speed = 286
    Horseshoes_of_a_Zephyr = 287
    Hourglass = 288
    Hunting_trap = 289
    Immovable_Rod = 290
    Ink = 291
    Ink_pen = 292
    Instant_Fortress = 293
    Ioun_Stone = 294
    Iron_Bands_of_Binding = 295
    Iron_Flask = 296
    Iron_pot = 297
    Iron_spikes = 298
    Javelin = 299
    Javelin_1 = 300
    Javelin_2 = 301
    Javelin_3 = 302
    Javelin_of_Lightning = 303
    Jewelers_Tools = 304
    Jug = 305
    Ladder = 306
    Lamp = 307
    Lance = 308
    Lance_1 = 309
    Lance_2 = 310
    Lance_3 = 311
    Lantern_of_Revealing = 312
    Leather_Armor = 313
    Leather_Armor_1 = 314
    Leather_Armor_2 = 315
    Leather_Armor_3 = 316
    Leather_Armor_of_Acid_Resistance = 317
    Leather_Armor_of_Cold_Resistance = 318
    Leather_Armor_of_Fire_Resistance = 319
    Leather_Armor_of_Force_Resistance = 320
    Leather_Armor_of_Lightning_Resistance = 321
    Leather_Armor_of_Necrotic_Resistance = 322
    Leather_Armor_of_Poison_Resistance = 323
    Leather_Armor_of_Psychic_Resistance = 324
    Leather_Armor_of_Radiant_Resistance = 325
    Leather_Armor_of_Thunder_Resistance = 326
    Leatherworkers_Tools = 327
    Light_Crossbow = 328
    Light_Crossbow_1 = 329
    Light_Crossbow_2 = 330
    Light_Crossbow_3 = 331
    Light_Hammer = 332
    Lock = 333
    Longbow = 334
    Longbow_1 = 335
    Longbow_2 = 336
    Longbow_3 = 337
    Longsword = 338
    Longsword_1 = 339
    Longsword_2 = 340
    Longsword_3 = 341
    Luck_Blade = 342
    Lute = 343
    Lyre = 344
    Mace = 345
    Mace_1 = 346
    Mace_2 = 347
    Mace_3 = 348
    Mace_of_Disruption = 349
    Mace_of_Smiting = 350
    Mace_of_Terror = 351
    Magnifying_glass = 352
    Manacles = 353
    Mantle_of_Spell_Resistance = 354
    Manual_of_Bodily_Health = 355
    Manual_of_Gainful_Exercise = 356
    Manual_of_Golems = 357
    Manual_of_Quickness_of_Action = 358
    Map_or_scroll_case = 359
    Marvelous_Pigments = 360
    Masons_Tools = 361
    Maul = 362
    Maul_1 = 363
    Maul_2 = 364
    Maul_3 = 365
    Medallion_of_Thoughts = 366
    Merchants_scale = 367
    Mess_kit = 368
    Miners_pick = 369
    Mirror_of_Life_Trapping = 370
    Mithral_Armor = 371
    Morningstar = 372
    Morningstar_1 = 373
    Morningstar_2 = 374
    Morningstar_3 = 375
    Navigators_Tools = 376
    Necklace_of_Adaptation = 377
    Necklace_of_Fireballs = 378
    Necklace_of_Prayer_Beads = 379
    Net = 380
    Net_1 = 381
    Net_2 = 382
    Net_3 = 383
    Nine_Lives_Stealer = 384
    Oathbow = 385
    Oil = 386
    Oil_of_Etherealness = 387
    Oil_of_Sharpness = 388
    Oil_of_Slipperiness = 389
    Orb = 390
    Orb_of_Dragonkind = 391
    Padded_Armor = 392
    Padded_Armor_1 = 393
    Padded_Armor_2 = 394
    Padded_Armor_3 = 395
    Padded_Armor_of_Acid_Resistance = 396
    Padded_Armor_of_Cold_Resistance = 397
    Padded_Armor_of_Fire_Resistance = 398
    Padded_Armor_of_Force_Resistance = 399
    Padded_Armor_of_Lightning_Resistance = 400
    Padded_Armor_of_Necrotic_Resistance = 401
    Padded_Armor_of_Poison_Resistance = 402
    Padded_Armor_of_Psychic_Resistance = 403
    Padded_Armor_of_Radiant_Resistance = 404
    Padded_Armor_of_Thunder_Resistance = 405
    Painters_Supplies = 406
    Pan_flute = 407
    Paper = 408
    Parchment = 409
    Pearl_of_Power = 410
    Perfume = 411
    Periapt_of_Health = 412
    Periapt_of_Proof_against_Poison = 413
    Periapt_of_Wound_Closure = 414
    Philter_of_Love = 415
    Pike = 416
    Pike_1 = 417
    Pike_2 = 418
    Pike_3 = 419
    Pipes_of_Haunting = 420
    Pipes_of_the_Sewers = 421
    Piton = 422
    Piwafwi_of_Fire_Resistance_Cloak_of_Elvenkind = 423
    Plate_Armor = 424
    Plate_Armor_1 = 425
    Plate_Armor_2 = 426
    Plate_Armor_3 = 427
    Plate_Armor_of_Acid_Resistance = 428
    Plate_Armor_of_Cold_Resistance = 429
    Plate_Armor_of_Etherealness = 430
    Plate_Armor_of_Fire_Resistance = 431
    Plate_Armor_of_Force_Resistance = 432
    Plate_Armor_of_Lightning_Resistance = 433
    Plate_Armor_of_Necrotic_Resistance = 434
    Plate_Armor_of_Poison_Resistance = 435
    Plate_Armor_of_Psychic_Resistance = 436
    Plate_Armor_of_Radiant_Resistance = 437
    Plate_Armor_of_Thunder_Resistance = 438
    Playing_card_set = 439
    Poisoners_kit = 440
    Pole = 441
    Portable_Hole = 442
    Portable_ram = 443
    Potion_of_Acid_Resistance = 444
    Potion_of_Animal_Friendship = 445
    Potion_of_Clairvoyance = 446
    Potion_of_Climbing = 447
    Potion_of_Cold_Resistance = 448
    Potion_of_Diminution = 449
    Potion_of_Fire_Resistance = 450
    Potion_of_Flying = 451
    Potion_of_Force_Resistance = 452
    Potion_of_Gaseous_Form = 453
    Potion_of_Giant_Strength = 454
    Potion_of_Growth = 455
    Potion_of_Healing = 456
    Potion_of_Heroism = 457
    Potion_of_Invisibility = 458
    Potion_of_Invulnerability = 459
    Potion_of_Lightning_Resistance = 460
    Potion_of_Mind_Reading = 461
    Potion_of_Necrotic_Resistance = 462
    Potion_of_Poison = 463
    Potion_of_Poison_Resistance = 464
    Potion_of_Psychic_Resistance = 465
    Potion_of_Radiant_Resistance = 466
    Potion_of_Speed = 467
    Potion_of_Thunder_Resistance = 468
    Potion_of_Water_Breathing = 469
    Potters_Tools = 470
    Pouch = 471
    Priests_Pack = 472
    Quarterstaff = 473
    Quarterstaff_1 = 474
    Quarterstaff_2 = 475
    Quarterstaff_3 = 476
    Quiver = 477
    Rapier = 478
    Rapier_1 = 479
    Rapier_2 = 480
    Rapier_3 = 481
    Rations = 482
    Reliquary = 483
    Restorative_Ointment = 484
    Ring_Mail = 485
    Ring_Mail_1 = 486
    Ring_Mail_2 = 487
    Ring_Mail_3 = 488
    Ring_Mail_of_Acid_Resistance = 489
    Ring_Mail_of_Cold_Resistance = 490
    Ring_Mail_of_Fire_Resistance = 491
    Ring_Mail_of_Force_Resistance = 492
    Ring_Mail_of_Lightning_Resistance = 493
    Ring_Mail_of_Necrotic_Resistance = 494
    Ring_Mail_of_Poison_Resistance = 495
    Ring_Mail_of_Psychic_Resistance = 496
    Ring_Mail_of_Radiant_Resistance = 497
    Ring_Mail_of_Thunder_Resistance = 498
    Ring_of_Acid_Resistance = 499
    Ring_of_Animal_Influence = 500
    Ring_of_Cold_Resistance = 501
    Ring_of_Djinni_Summoning = 502
    Ring_of_Elemental_Command = 503
    Ring_of_Evasion = 504
    Ring_of_Feather_Falling = 505
    Ring_of_Fire_Resistance = 506
    Ring_of_Force_Resistance = 507
    Ring_of_Free_Action = 508
    Ring_of_Invisibility = 509
    Ring_of_Jumping = 510
    Ring_of_Lightning_Resistance = 511
    Ring_of_Mind_Shielding = 512
    Ring_of_Necrotic_Resistance = 513
    Ring_of_Poison_Resistance = 514
    Ring_of_Protection = 515
    Ring_of_Psychic_Resistance = 516
    Ring_of_Radiant_Resistance = 517
    Ring_of_Regeneration = 518
    Ring_of_Shooting_Stars = 519
    Ring_of_Spell_Storing = 520
    Ring_of_Spell_Turning = 521
    Ring_of_Swimming = 522
    Ring_of_Telekinesis = 523
    Ring_of_Three_Wishes = 524
    Ring_of_Thunder_Resistance = 525
    Ring_of_Warmth = 526
    Ring_of_Water_Walking = 527
    Ring_of_X_ray_Vision = 528
    Ring_of_the_Ram = 529
    Robe_of_Eyes = 530
    Robe_of_Scintillating_Colors = 531
    Robe_of_Stars = 532
    Robe_of_Useful_Items = 533
    Robe_of_the_Archmagi = 534
    Robes = 535
    Rod = 536
    Rod_of_Absorption = 537
    Rod_of_Alertness = 538
    Rod_of_Lordly_Might = 539
    Rod_of_Rulership = 540
    Rod_of_Security = 541
    Rope_of_Climbing = 542
    Rope_of_Entanglement = 543
    Sack = 544
    Scale_Mail = 545
    Scale_Mail_1 = 546
    Scale_Mail_2 = 547
    Scale_Mail_3 = 548
    Scale_Mail_of_Acid_Resistance = 549
    Scale_Mail_of_Cold_Resistance = 550
    Scale_Mail_of_Fire_Resistance = 551
    Scale_Mail_of_Force_Resistance = 552
    Scale_Mail_of_Lightning_Resistance = 553
    Scale_Mail_of_Necrotic_Resistance = 554
    Scale_Mail_of_Poison_Resistance = 555
    Scale_Mail_of_Psychic_Resistance = 556
    Scale_Mail_of_Radiant_Resistance = 557
    Scale_Mail_of_Thunder_Resistance = 558
    Scarab_of_Protection = 559
    Scholars_Pack = 560
    Scimitar = 561
    Scimitar_1 = 562
    Scimitar_2 = 563
    Scimitar_3 = 564
    Scimitar_of_Speed = 565
    Sealing_wax = 566
    Shawm = 567
    Shield = 568
    Shield_1 = 569
    Shield_2 = 570
    Shield_3 = 571
    Shield_of_Missile_Attraction = 572
    Shortbow = 573
    Shortbow_1 = 574
    Shortbow_2 = 575
    Shortbow_3 = 576
    Shortsword = 577
    Shortsword_1 = 578
    Shortsword_2 = 579
    Shortsword_3 = 580
    Shovel = 581
    Sickle = 582
    Sickle_1 = 583
    Sickle_2 = 584
    Sickle_3 = 585
    Signal_whistle = 586
    Signet_ring = 587
    Silk_rope = 588
    Sledge_hammer = 589
    Sling = 590
    Sling_1 = 591
    Sling_2 = 592
    Sling_3 = 593
    Sling_bullets = 594
    Slippers_of_Spider_Climbing = 595
    Smiths_Tools = 596
    Soap = 597
    Sovereign_Glue = 598
    Spear = 599
    Spear_1 = 600
    Spear_2 = 601
    Spear_3 = 602
    Spell_Scroll = 603
    Spellbook = 604
    Spellguard_Shield = 605
    Sphere_of_Annihilation = 606
    Spiked_Armor_of_Acid_Resistance = 607
    Spiked_Armor_of_Cold_Resistance = 608
    Spiked_Armor_of_Fire_Resistance = 609
    Spiked_Armor_of_Force_Resistance = 610
    Spiked_Armor_of_Lightning_Resistance = 611
    Spiked_Armor_of_Necrotic_Resistance = 612
    Spiked_Armor_of_Poison_Resistance = 613
    Spiked_Armor_of_Psychic_Resistance = 614
    Spiked_Armor_of_Radiant_Resistance = 615
    Spiked_Armor_of_Thunder_Resistance = 616
    Splint_Armor = 617
    Splint_Armor_1 = 618
    Splint_Armor_2 = 619
    Splint_Armor_3 = 620
    Splint_Armor_of_Acid_Resistance = 621
    Splint_Armor_of_Cold_Resistance = 622
    Splint_Armor_of_Fire_Resistance = 623
    Splint_Armor_of_Force_Resistance = 624
    Splint_Armor_of_Lightning_Resistance = 625
    Splint_Armor_of_Necrotic_Resistance = 626
    Splint_Armor_of_Poison_Resistance = 627
    Splint_Armor_of_Psychic_Resistance = 628
    Splint_Armor_of_Radiant_Resistance = 629
    Splint_Armor_of_Thunder_Resistance = 630
    Sprig_of_mistletoe = 631
    Spyglass = 632
    Staff = 633
    Staff_of_Charming = 634
    Staff_of_Fire = 635
    Staff_of_Frost = 636
    Staff_of_Healing = 637
    Staff_of_Power = 638
    Staff_of_Striking = 639
    Staff_of_Swarming_Insects = 640
    Staff_of_Thunder_and_Lightning = 641
    Staff_of_Withering = 642
    Staff_of_the_Magi = 643
    Staff_of_the_Python = 644
    Staff_of_the_Woodlands = 645
    Steel_mirror = 646
    Stone_of_Controlling_Earth_Elementals = 647
    Stone_of_Good_Luck = 648
    Studded_Leather_Armor = 649
    Studded_Leather_Armor_1 = 650
    Studded_Leather_Armor_2 = 651
    Studded_Leather_Armor_3 = 652
    Studded_Leather_Armor_of_Acid_Resistance = 653
    Studded_Leather_Armor_of_Cold_Resistance = 654
    Studded_Leather_Armor_of_Fire_Resistance = 655
    Studded_Leather_Armor_of_Force_Resistance = 656
    Studded_Leather_Armor_of_Lightning_Resistance = 657
    Studded_Leather_Armor_of_Necrotic_Resistance = 658
    Studded_Leather_Armor_of_Poison_Resistance = 659
    Studded_Leather_Armor_of_Psychic_Resistance = 660
    Studded_Leather_Armor_of_Radiant_Resistance = 661
    Studded_Leather_Armor_of_Thunder_Resistance = 662
    Sun_Blade = 663
    Sword_of_Life_Stealing = 664
    Sword_of_Sharpness = 665
    Sword_of_Wounding = 666
    Talisman_of_Pure_Good = 667
    Talisman_of_Ultimate_Evil = 668
    Talisman_of_the_Sphere = 669
    Tent = 670
    Thieves_Tools = 671
    Tinderbox = 672
    Tinkers_Tools = 673
    Tome_of_Clear_Thought = 674
    Tome_of_Leadership_and_Influence = 675
    Tome_of_Understanding = 676
    Torch = 677
    Totem = 678
    Travelers_clothes = 679
    Trident = 680
    Trident_1 = 681
    Trident_2 = 682
    Trident_3 = 683
    Trident_of_Fish_Command = 684
    Universal_Solvent = 685
    Vial = 686
    Vicious_Battleaxe = 687
    Vicious_Blowgun = 688
    Vicious_Club = 689
    Vicious_Dagger = 690
    Vicious_Dart = 691
    Vicious_Flail = 692
    Vicious_Glaive = 693
    Vicious_Greataxe = 694
    Vicious_Greatclub = 695
    Vicious_Greatsword = 696
    Vicious_Halberd = 697
    Vicious_Hand_Crossbow = 698
    Vicious_Handaxe = 699
    Vicious_Heavy_Crossbow = 700
    Vicious_Javelin = 701
    Vicious_Lance = 702
    Vicious_Light_Crossbow = 703
    Vicious_Light_Hammer = 704
    Vicious_Longbow = 705
    Vicious_Longsword = 706
    Vicious_Mace = 707
    Vicious_Maul = 708
    Vicious_Morningstar = 709
    Vicious_Pike = 710
    Vicious_Quarterstaff = 711
    Vicious_Rapier = 712
    Vicious_Scimitar = 713
    Vicious_Shortbow = 714
    Vicious_Shortsword = 715
    Vicious_Sickle = 716
    Vicious_Sling = 717
    Vicious_Spear = 718
    Vicious_Trident = 719
    Vicious_War_Pick = 720
    Vicious_Warhammer = 721
    Vicious_Whip = 722
    Viol = 723
    Vorpal_Greatsword = 724
    Vorpal_Longsword = 725
    Vorpal_Scimitar = 726
    Wand = 727
    Wand_of_Binding = 728
    Wand_of_Enemy_Detection = 729
    Wand_of_Fear = 730
    Wand_of_Fireballs = 731
    Wand_of_Lightning_Bolts = 732
    Wand_of_Magic_Detection = 733
    Wand_of_Magic_Missiles = 734
    Wand_of_Paralysis = 735
    Wand_of_Polymorph = 736
    Wand_of_Secrets = 737
    Wand_of_Web = 738
    Wand_of_Wonder = 739
    Wand_of_the_War_Mage_1 = 740
    Wand_of_the_War_Mage_2 = 741
    Wand_of_the_War_Mage_3 = 742
    War_Pick = 743
    War_Pick_1 = 744
    War_Pick_2 = 745
    War_Pick_3 = 746
    Warhammer = 747
    Warhammer_1 = 748
    Warhammer_2 = 749
    Warhammer_3 = 750
    Waterskin = 751
    Wave = 752
    Weavers_Tools = 753
    Well_of_Many_Worlds = 754
    Whelm = 755
    Whetstone = 756
    Whip = 757
    Whip_1 = 758
    Whip_2 = 759
    Whip_3 = 760
    Wind_Fan = 761
    Winged_Boots = 762
    Wings_of_Flying = 763
    Woodcarvers_Tools = 764
    Wooden_staff = 765
    Yew_wand = 766
