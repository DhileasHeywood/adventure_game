class Place:

    def enter(self):
        print("This place is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine:

    def __init__(self, place_map):
        self.place_map = place_map


    # This function is what runs the game. Every time you run this method, you 'play' the game.
    def play(self):
        # first we set where the current place is, by specifying it. We create an object of class Map, with the name of the opening place.
        # We then use that object when making an object of class Engine. So the resulting Engine object will also have a dict of all the scenes
        # dict of all the scenes, and will have a couple of methods, such as 'opening_place()' and 'next_place'
        current_place = self.place_map.opening_place()
        last_place = self.place_map.next_place("finished")

        while current_place != last_place:
            next_place_name = current_place.enter()
            current_scene = self.place_map.next_place(next_place_name)

        current_place.enter()

#class Map:
#
 #   def __init__(self, start_place):
#        pass
#
 #   def next_place(self, place_name):
 #       pass
#
 #   def opening_place(self):
 #       pass

a_map = Map("entry_room")
a_game = Engine(a_map)
a_game.play()


class Death(Place):

    def enter(self):
        pass

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