from textwrap import dedent

# need to start by making the classes and figuring out what goes in each. What do they need to do?
game_running = True
class Player:
    # needs to hold details about the character.
    def __init__(self, player_name):
        self.player_name = player_name
        self.place_on_map = 0
        self.place_in_room_location = 0


class Place:
    def __init__(self, room):
        self.room = room

    def describe(self, room_location):
        print(self.descriptors[room_location])

    def evaluate(self, input):




#class Item:
#   def __init__(self, item_name, quantity):
#      self.item_name = item_name
#     self.quantity = quantity
#



entry_room = {
    0 : dedent("""
                    You wake up in a room. You're all alone.
                    The room is almost empty, with just the chair you're sitting on, and a chest in the corner of the room.
                    You see a door directly in front of you. What do you do?
                    """),
    1 : dedent("""
                    You walk towards the chest. You try to open it, but the closing mechanism is rusty and stiff. It's 
                    proving tough to open. You struggle for a few minutes, but eventually, you feel the latch give, and the
                    chest opens up. You look inside. You see a key, and a rusty sword. Do you want to take them?
                    """),
    2 : dedent("""
                    You take the key and the sword. It might be rusty, but you feel safer knowing that you have some way to
                    protect yourself. Who knows what might reside within these walls... What would you like to do next?
                    """),
    3 : dedent("""
                            You walk up to the door. It's locked. If only there were a key...
                            """),
    4 : dedent("""
                        You walk up to the door. It's locked, but there is a keyhole. You think it might fit the key 
                        from the chest. You put the key in the hole and turn. You hear a click. You open the door and 
                        walk forward. 
                        """)
}


room_1 = Place(entry_room)

room_1.describe("entry chest")



map = [riddle_room = Place("Riddle Room"), corridor, dragon_room, kobold_room, troll_room, table_room, tree_room)

def entry():
    name = input("what is your name? \n> ")
    player = Player(name)
    #while game_running is True:
        # display the correct game text
        # ask user for input
        # react to the input

    map[player.place_location].describe(player.room_location)

entry()