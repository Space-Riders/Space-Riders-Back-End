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
        zergling = math.ceil(random() * 100)

        if zergling < 12:
            room.monster = Monster.objects.get(name='Larva').id
            room.save()
        elif zergling >= 12 and zergling < 24:
            room.monster = Monster.objects.get(name='Drone').id
            room.save()
        elif zergling >= 24 and zergling < 35:
            room.monster = Monster.objects.get(name='Roach').id
            room.save()
        elif zergling >= 35 and zergling < 48:
            room.monster = Monster.objects.get(name='Zergling').id
            room.save()
        elif zergling >= 48 and zergling < 66:
            room.monster = Monster.objects.get(name='Baneling').id
            room.save()
        elif zergling >= 66 and zergling < 80:
            room.monster = Monster.objects.get(name='Hydralisk').id
            room.save()
        elif zergling >= 80 and zergling < 89:
            room.monster = Monster.objects.get(name='Corruptor').id
            room.save()
        elif zergling >= 89 and zergling < 94:
            room.monster = Monster.objects.get(name='Ultralisk').id
            room.save()
        elif zergling >= 94 and zergling < 98:
            room.monster = Monster.objects.get(name='Viper').id
            room.save()
        else:
            room.monster = Monster.objects.get(name='Queen').id
            room.save()

def create_monsters():
    larva = Monster(name="Larva", description="Fiesty little bugger.",
                        xeritesGained=2, xeritesLost=1, xp=1, xpGained=1)
    larva.save()
    drone = Monster(name="Drone", description="Mindless worker, mind programmed to do one thing only.",
                        xeritesGained=10, xeritesLost=2, xp=10, xpGained=2)
    drone.save()
    roach = Monster(name="Roach", description="Hideous little freaks, with thick shell, and acid spewing capability that can dissolve neostell armor.",
                        xeritesGained=20, xeritesLost=3, xp=5, xpGained=2)
    roach.save()
    zergling = Monster(name="Zergling", description="A hybrid of 15 different strains, designed to do one thing only, be a perfect killing machine.",
                        xeritesGained=30, xeritesLost=20, xp=15, xpGained=4)
    zergling.save()
    baneling = Monster(name="Baneling", description="Mutated Zergling that comes with nasty package. Watch out for this one.",
                            xeritesGained=100, xeritesLost=45, xp=50, xpGained=8)
    baneling.save()
    hydralisk = Monster(name="Hydralisk", description="Siege Tanks of Zergs. Powerful monster that instill fears on those who confront it.",
                        xeritesGained=1000, xeritesLost=666, xp=250, xpGained=16)
    hydralisk.save()
    corruptor = Monster(name="Corruptor", description="Giant brain-like creatures, that can disrupt matter at its core. No armor is safe! BEWARE!",
                            xeritesGained=3000, xeritesLost=1000, xp=500, xpGained=32)
    corruptor .save()
    ultralisk = Monster(name="Ultralisk", description="Biggest baddest of Zerg, True Monster!, nothing can stand in its way. RUN WHILE YOU CAN!",
                        xeritesGained=10000, xeritesLost=2000, xp=1500, xpGained=64)
    ultralisk.save()
    viper = Monster(name="Viper", description="Perfect strategist!",
                        xeritesGained=25000, xeritesLost=11000, xp=5000, xpGained=128)
    viper.save()
    queen = Monster(name="Queen", description="Mother of Zergs!, Fiercest of all! No one has deafeted her through eons! YOU MIGHT AS WELL QUIT THE GAME!",
                            xeritesGained=100000, xeritesLost=10000, xp=10000, xpGained=500)
    queen.save()

def run():

    print("Deleting all Rooms")
    Room.objects.all().delete()
    print("Deleting all Monsters")
    Monster.objects.all().delete()
    
    print("Create Monsters")
    create_monsters()
    print("Creating Zerg World")
    zergworld = Grid()
    print("\t carving out grid")
    zergworld.carveGrid()
    print("\t linking rooms")
    zergworld.linkRooms()
    print("Fill Rooms with Monster")
    fill_rooms_with_monsters()
    
