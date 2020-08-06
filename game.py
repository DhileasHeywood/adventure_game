
import entry_room
import tree_room
import table_room
import death
import finished

yes_answers = ["yes", "yup", "uhuh", "sure", "if i must", "definitely", "absolutely", "mhmm", "mmhmm", "yeah", "yeh",
               "ues", "ya", "ja", "si", "oui", "yar", "yah", "yarp", "yes please", "sure thing", "yes pls"]
no_answers = ["no", "nope", "nop", "nay", "nah", "no way"]
joke_answers = ["kill myself", "poop", "summon key", "knock knock", "wingardium leviosa", "lick fresco"]
personal_answers = ["check items", "items", "what do i have", "what things am i carrying", "what are my things",
                    "what am i carrying", "what stuff do i have", "what things do i have", "whats my stuff",
                    "what weapons", "my weapons", "what weapons do i have", "what weapons have i got", "whats my weapons",
                    "weapons", "where are my weapons", "which weapons do i have", "which weapons have i got",
                    "what weapons am i carrying", "which weapons am i carrying", "do i have weapons", "do i have things",
                    "do i have a sword", "check weapons", "gold", "how much gold do i have", "how much do i have",
                    "how much gold am i carrying", "do i have money", "how much money do i have"]
companion_answers = ["who am i travelling with", "who am i with", "who is with me", "i'm with who", "who with"]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''




class Place:

    _visited = False

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



class Map:

    places = {
        "entry_room": entry_room.EntryRoom(),
        "tree_room": tree_room.TreeRoom(),
        "tree_in_tree_room": tree_room.TreeInTreeRoom(),
        "table_room": table_room.TableRoom(),
        "table_room_far_side": table_room.TableRoomFarSide(),
        "table_room_skeleton": table_room.TableRoomSkeleton(),
        "troll_room": troll_room.TrollRoom(),
        "kobold_room": kobold_room.KoboldRoom(),
        "dragon_room": dragon_room.DragonRoom(),
        "corridor": corridor.Corridor(),
        "riddle_room": riddle_room.RiddleRoom(),
        "finished": finished.Finished(),
        "death": death.Death()
    }

    def __init__(self, start_place):
        self.start_place = start_place

    def next_place(self, place_name):
        val = Map.places.get(place_name)
        return val

    def opening_place(self):
        return self.next_place(self.start_place)


class Items:
    def __init__(self):
        self.gold = 0
        self.weapon = None
        self.companion = "nobody"
        self.things = ["clothes"]
        self.poisoned = False

    def who_with(self):
        if self.companion == "nobody":
            print("You're not travelling with anyone.")

        else:
            print(f"You're travelling with {self.companion}")

    def query_all_things(self):
        print(f"You're carrying {self.gold} gold, {self.weapon}, and you have", ', '.join(self.things[0:len(self.things)-1]), "and", f"{self.things[-1]}.")

    def add_gold(self, amount):
        self.gold = self.gold + amount

    def new_thing(self, thing):
       self.things.append(thing)


players_stuff = Items()
a_map = Map("entry_room")
a_game = Engine(a_map)
a_game.play()
