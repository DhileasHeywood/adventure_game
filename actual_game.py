from random import randint
from textwrap import dedent


class Place:

    def enter(self):
        print("This place is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine:

    # place_map MUST be a Map object, or the play function won't work. DO NOT FORGET THIS.
    def __init__(self, place_map):
        self.place_map = place_map


    # This function is what runs the game. Every time you run this method, you 'play' the game.
    def play(self):
        # first we set where the current place is, by specifying it. We create an object of class Map, with the name of the opening place.
        # We then use that object when making an object of class Engine. (composition and all)

        # current_place will be equal to self.place_map with the opening_place() method applied. This will be written later.
        # What it will do is run the place class with the key "place_map"
        current_place = self.place_map.opening_place()
        # final_place will be the Finished() place class. What happens when you win!
        final_place = self.place_map.next_place("finished")

        # Here we're setting up the game loop. This means that when you've not won or died, the game will keep running whichever room you're in.
        while current_place != final_place:
            next_place_name = current_place.enter()
            current_place = self.place_map.next_place(next_place_name)

        # This is just to make sure that the last scene runs, because we'll be out of the game loop if we get there.
        current_place.enter()


class Death(Place):

    quips = [
        "You died. You suck at this!",
        "You're such a loser",
        "Git gud, scrub!",
        "Even my kittens are better than this!",
        "You're worse than Dhileas's jokes!",
        "Fatality",
        "WASTED",
        "They say when you fall off your horse, you should get back on it... People are often wrong though.",
        "If at first you don't succeed, try, try again.",
        "Maybe next time.... Or the time after..?"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        print("Start again?")
        answer = input("> ").lower()

        if answer == "yes":
            # I need to figure out how to restart the game, but I'll put it here.
            return "entry_room"

        else:
            exit(1)

class EntryRoom(Place):

    def enter(self):
        print(dedent("""
        You wake up in a room. You're all alone.
        The room is almost empty, with just the chair you're sitting on, and a chest in the corner of the room.
        You see a door directly in front of you. What do you do?
        """))

        action = input("> ")

        if "door" in action:
            print(dedent("""
                You walk up to the door. It's locked. If only there were a key...
                """))

            # Not sure if this function is going to work or not, but I want to go back to the start of the function.
            return "entry_room"


        elif "chest" in action:
            print(dedent("""
            You walk towards the chest. 
            You try to open it, but the closing mechanism is rusty and stiff. It's proving tough to open. 
            You struggle for a few minutes, but eventually, you feel the latch give, and the chest opens up. You look inside. 
            You see a key, and a rusty sword. You take the key and the sword. 
            It might be rusty, but you feel safer knowing that you have some way to protect yourself. 
            Who knows what might reside within these walls...
            
            You walk up to the door. It's locked, but there is a keyhole. You think it might fit the key from the chest. 
            You put the key in the hole and turn. You hear a click. You open the door and walk forward. 
            """))

            return "finished"
        else:
            print("Input not recognised")
            return "entry_room"

class RiddleRoom(Place):

    def enter(self):
        pass

class Corridor(Place):

    def enter(self):
        pass

class DragonRoom(Place):

    def enter(self):
        pass

class KoboldRoom(Place):

    def enter(self):
        pass

class TrollRoom(Place):

    def enter(self):
        pass

class TableRoom(Place):

    def enter(self):
        pass

class TreeRoom(Place):

    def enter(self):
        pass

class Finished(Place):

    def enter(self):
        print("Congratulations! You've won!")
        return "finished"


class Map:

    places = {
        "entry_room" : EntryRoom(),
        "tree_room" : TreeRoom(),
        "table_room" : TableRoom(),
        "troll_room" : TrollRoom(),
        "kobold_room" : KoboldRoom(),
        "dragon_room" : DragonRoom(),
        "corridor" : Corridor(),
        "riddle_room" : RiddleRoom(),
        "finished" : Finished()
    }
    def __init__(self, start_place):
        self.start_place = start_place

    def next_place(self, place_name):
        val = Map.places.get(place_name)
        return val

    def opening_place(self):
        return self.next_place(self.start_place)

a_map = Map("entry_room")
a_game = Engine(a_map)
a_game.play()