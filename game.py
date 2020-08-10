import place_and_items
import entry_room
import tree_room_
#import table_room
import death
import finished


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



class Map:

    places = {
        "entry_room": entry_room.entry_room,
        "tree_room": tree_room_.tree_room,
        "tree_in_tree_room": tree_room_.tree_in_tree_room,
        #"table_room": table_room.TableRoom(),
        #"table_room_far_side": table_room.TableRoomFarSide(),
        #"table_room_skeleton": table_room.TableRoomSkeleton(),
        #"troll_room": troll_room.TrollRoom(),
        #"kobold_room": kobold_room.KoboldRoom(),
        #"dragon_room": dragon_room.DragonRoom(),
        #"corridor": corridor.Corridor(),
        #"riddle_room": riddle_room.RiddleRoom(),
        "finished": finished.finished,
        "death": death.death
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
