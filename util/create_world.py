import math
from random import random
from adventure.models import Room, Monster, Player
from util.templates import titleGenerator, descGenerator

class Grid:
    def __init__(self, dimensions=50, maxTunnels=500, maxLength=8):
        self.dimensions = dimensions
        self.maxTunnels = maxTunnels
        self.maxLength = maxLength
        self.grid = self.createGrid(dimensions)  # Create the grid

        self.currentRow = 25  # random start X
        self.currentCol = 25  # random start Y
        # top, right, bottom, left as [y, x] coordinates
        self.directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        self.lastDirection = [0, 0]  # save the last direction
        self.randomDirection = [0, 0]

    def createGrid(self, dimensions, num=0):
        # Temp: Delete all the existing Rooms
        Room.objects.all().delete()

        # Create an empty array and init with all "walls"
        a = []
        for i in range(0, dimensions):
            a.append([])
            for j in range(0, dimensions):
                a[i].append(num)
        return a

    # The Walker Algorithm "Carving out" the room as it walks
    def carveGrid(self):
        # while we haven't hit the max Tunnels allowed
        while self.maxTunnels > 0:

            # Check that the nextDirection is perpendicular to the lastDirection
            while (self.randomDirection[0] == -self.lastDirection[0] and self.randomDirection[1] == -self.lastDirection[1]) or (self.randomDirection[0] == self.lastDirection[0] and self.randomDirection[1] == self.lastDirection[1]):
                # Get a random direction
                self.randomDirection = self.directions[math.floor(
                    random() * 4)]

            # Move a random distance in a particular direction
            randomLength = math.ceil(random() * self.maxLength)
            tunnelLength = 0

            while tunnelLength < randomLength:
                # Check if about to run into any walls
                if not ((self.currentRow == 0 and self.randomDirection[0] == -1) or (self.currentCol == 0 and self.randomDirection[1] == -1) or (self.currentRow == self.dimensions - 1 and self.randomDirection[0] == 1) or (self.currentCol == self.dimensions - 1 and self.randomDirection[1] == 1)):

                    # DO NOT assign the room here
                    # This row / col combo may be "stepped" on many times and may
                    # create duplicate rooms = BAD
                    # See def saveAndLinkRooms

                    self.grid[self.currentRow][self.currentCol] = 1

                    self.currentRow += self.randomDirection[0]
                    self.currentCol += self.randomDirection[1]
                    tunnelLength += 1

                else:
                    break

            # tunnelLength should be at zero, so decrement the maxTunnels
            # set the last direction to the direcition we just went
            if tunnelLength >= 0:
                self.lastDirection = self.randomDirection
                self.maxTunnels -= 1

    # Helper method to get a coordinates neighbors
    def getNeighbors(self, y, x):
        neighbors = [None, None, None, None]  # Top, Right, Bottom, Left

        # Top Neighbor
        if not y - 1 < 0 and not self.grid[y - 1][x] == 0:
            neighbors[0] = self.grid[y - 1][x]

        # Right Neighbor
        if not x + 1 > self.dimensions - 1 and not self.grid[y][x + 1] == 0:
            neighbors[1] = self.grid[y][x + 1]

        # Bottom Neighbor
        if not y + 1 > self.dimensions - 1 and not self.grid[y + 1][x] == 0:
            neighbors[2] = self.grid[y + 1][x]

        # Left Neighbor
        if not x - 1 < 0 and not self.grid[y][x - 1] == 0:
            neighbors[3] = self.grid[y][x - 1]

        return neighbors

    # Helper method to get the direction
    def getDirection(self, i):
        switcher = {
            0: 'n',
            1: 'e',
            2: 's',
            3: 'w'
        }
        return switcher.get(i)

    def createAndSaveRooms(self):
        for y in range(0, self.dimensions):
            for x in range(0, self.dimensions):

                if not self.grid[y][x] == 0:
                    # Create and Save the room HERE
                    #import pdb; pdb.set_trace()
                    self.grid[y][x] = Room(
                        title=titleGenerator(), description=descGenerator(), x_coor=x, y_coor=y)
                    currentRoom = self.grid[y][x]
                    currentRoom.save()

    # Link the Rooms to their associated neighbors
    def linkRooms(self):
        # Create and save Rooms
        self.createAndSaveRooms()

        # Loop through each grid item
        for y in range(0, self.dimensions):
            for x in range(0, self.dimensions):

                if not self.grid[y][x] == 0:
                    neighbors = self.getNeighbors(y, x)

                    for i in range(0, len(neighbors)):
                        if neighbors[i] is not None:

                            # Connect the Rooms here
                            self.grid[y][x].connectRooms(
                                neighbors[i], self.getDirection(i))

def fill_rooms_with_monsters():

    rooms = Room.objects.all()

    for room in rooms:
        bee = math.ceil(random() * 100)

        if bee < 12:
            room.monster = Monster.objects.get(name='Venus Fly Trap').id
            room.save()
        elif bee >= 12 and bee < 24:
            room.monster = Monster.objects.get(name='Mining Bee').id
            room.save()
        elif bee >= 24 and bee < 35:
            room.monster = Monster.objects.get(name='Carpenter Bee').id
            room.save()
        elif bee >= 35 and bee < 48:
            room.monster = Monster.objects.get(name='Digger Bee').id
            room.save()
        elif bee >= 48 and bee < 66:
            room.monster = Monster.objects.get(name='LeafCutter Bee').id
            room.save()
        elif bee >= 66 and bee < 80:
            room.monster = Monster.objects.get(name='Bumble Bee').id
            room.save()
        elif bee >= 80 and bee < 89:
            room.monster = Monster.objects.get(name='Honey Bee').id
            room.save()
        elif bee >= 89 and bee < 94:
            room.monster = Monster.objects.get(name='Honey Bee').id
            room.save()
        elif bee >= 94 and bee < 98:
            room.monster = Monster.objects.get(name='Honey Bee').id
            room.save()
        else:
            room.monster = Monster.objects.get(name='Queen Bee').id
            room.save()

def create_monsters():
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

def run():

    print("Deleting all Rooms")
    Room.objects.all().delete()
    print("Deleting all Monsters")
    Monster.objects.all().delete()
    
    print("Create Monsters")
    create_monsters()
    print("Creating Bee World")
    beeworld = Grid()
    print("\t carving out grid")
    beeworld.carveGrid()
    print("\t linking rooms")
    beeworld.linkRooms()
    print("Fill Rooms with Monster")
    fill_rooms_with_monsters()
    
