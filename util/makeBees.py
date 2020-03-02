import math
from random import random
from adventure.models import Room, Monster


def fillRoomsWithBees():

    rooms = Room.objects.all()

    for room in rooms:
        bee = math.ceil(random() * 100)

        if bee < 12:
            room.monster = Monster.objects.get(id=1)
            room.save()
        elif bee >= 12 and bee < 24:
            room.monster = Monster.objects.get(id=2)
            room.save()
        elif bee >= 24 and bee < 35:
            room.monster = Monster.objects.get(id=3)
            room.save()
        elif bee >= 35 and bee < 48:
            room.monster = Monster.objects.get(id=4)
            room.save()
        elif bee >= 48 and bee < 66:
            room.monster = Monster.objects.get(id=5)
            room.save()
        elif bee >= 66 and bee < 80:
            room.monster = Monster.objects.get(id=6)
            room.save()
        elif bee >= 80 and bee < 89:
            room.monster = Monster.objects.get(id=7)
            room.save()
        elif bee >= 89 and bee < 94:
            room.monster = Monster.objects.get(id=8)
            room.save()
        elif bee >= 94 and bee < 98:
            room.monster = Monster.objects.get(id=9)
            room.save()
        else:
            room.monster = Monster.objects.get(id=10)
            room.save()