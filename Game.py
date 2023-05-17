class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def move(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

class Character:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def move(self, direction):
        next_room = self.current_room.move(direction)
        if next_room is not None:
            self.current_room = next_room
            print(f"{self.name} has moved to {self.current_room.description}")
        else:
            print("You can't go that way!")

# Create rooms
kitchen = Room("Kitchen")
living_room = Room("Living Room")
bedroom = Room("Bedroom")

# Connect rooms
kitchen.add_exit("south", living_room)
living_room.add_exit("north", kitchen)
living_room.add_exit("west", bedroom)
bedroom.add_exit("east", living_room)

# Create character
player = Character("Player", kitchen)

# Game loop
while True:
    command = input("What do you want to do? ")
    if command in ["north", "south", "east", "west"]:
        player.move(command)
    elif command == "quit":
        break
    else:
        print("Invalid command!")
