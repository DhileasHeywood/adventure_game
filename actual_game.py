from random import randint

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
        # last_place will be the Finished() place class. What happens when you win!
        last_place = self.place_map.next_place("finished")

        # Here we're setting up the game loop. This means that when you've not won, the game will keep running whichever room you're in.
        while current_place != last_place:
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
        else:
            exit(1)

class Entry_room(Place):

    def enter(self):
        pass

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


class Map:

    def __init__(self, start_place):
        pass

    def next_place(self, place_name):
        pass

    def opening_place(self):
        pass

a_map = Map("entry_room")
a_game = Engine(a_map)
a_game.play()