import math
from random import random
from adventure.models import Monster


# class Bee():
#     def __init__(self, name):
#         self.name = name
#         self.honeyGained = 2
#         self.honeyLost = 1
#         self.xp = 1

#     def initializeBee(self):
#         # Determine a difficulty for the monster
#         multiplier = self.getDifficulty()

#         # Use that difficulty to calculate a honey gained, lost and xp
#         self.honeyGained = multiplier * 5
#         self.honeyLost = multiplier * 2
#         self.xp = multiplier

#     # helper method
#     def getDifficulty(self):
#         difficulty = math.ceil(random() * 100)

#         if difficulty < 50:
#             return 3
#         elif difficulty >= 50 and difficulty < 80:
#             return 6
#         elif difficulty >= 80 and difficulty < 95:
#             return 8
#         else:
#             return 10

#     def getName():
#         names = ['Venus Fly Trap', 'Killer Bee', 'Bumble Bee', 'Carpenter Bee', 'Yellow Jacket',
#                  'Queen Bee', 'Honey Bee', 'Digger Bee', 'Mining Bee', 'LeafCutter Bee']


# class VenusFlyTrap(Bee):
#     def __init__(self, name="Venus Fly Trap"):
#         super().__init__(name)


# name = models.CharField(max_length=50, default="Venus Fly Trap")
# description = models.CharField(
#     max_length=500, default="An angry little bugger")
# honeyGained = models.IntegerField(default=2)
# honeyLost = models.IntegerField(default=1)
# xp = models.IntegerField(default=1)
# xpGained = models.IntegerField(default=1)

venusFlyTrap = Monster(name="Venus Fly Trap", description="An angry little bugger",
                       honeyGained=2, honeyLost=1, xp=1, xpGained=1)
venusFlyTrap.save()

miningBee = Monster(name="Mining Bee", description="The guy likes to find treasure",
                    honeyGained=10, honeyLost=2, xp=10, xpGained=2)
miningBee.save()

carpenterBee = Monster(name="Carpenter Bee", description="He really likes wood",
                       honeyGained=20, honeyLost=3, xp=5, xpGained=2)
carpenterBee.save()

diggerBee = Monster(name="Digger Bee", description="You'll find him under stuff... maybe even you.",
                    honeyGained=30, honeyLost=20, xp=15, xpGained=4)
diggerBee.save()

leafCutterBee = Monster(name="LeafCutter Bee", description="You better Leaf or he'll cut you.",
                        honeyGained=100, honeyLost=45, xp=50, xpGained=8)
leafCutterBee.save()

bumbleBee = Monster(name="Bumble Bee", description="This bee can get you some really hot potential suitors.",
                    honeyGained=1000, honeyLost=666, xp=250, xpGained=16)
bumbleBee.save()

honeyBee = Monster(name="Honey Bee", description="Sweeter than Maple, better than Canada.",
                        honeyGained=3000, honeyLost=1000, xp=500, xpGained=32)
honeyBee.save()

yellowJacket = Monster(name="Yellow Jacker", description="Don't get confused. Not only will he sting you, but his clothing is spectacular.",
                       honeyGained=10000, honeyLost=2000, xp=1500, xpGained=64)
yellowJacket.save()

killerBee = Monster(name="Killer Bee", description="He's always confused why everyone is scared of him. He's only killed 1000 people",
                    honeyGained=25000, honeyLost=11000, xp=5000, xpGained=128)
killerBee.save()

queenBee = Monster(name="Queen Bee", description="Queen of queens. Bee of bees. Bow down before your master!",
                        honeyGained=100000, honeyLost=10000, xp=10000, xpGained=500)
queenBee.save()


