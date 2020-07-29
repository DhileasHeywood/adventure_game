from random import randint
from textwrap import dedent

yes_answers = ["yes", "yup", "uhuh", "sure", "if i must", "definitely", "absolutely", "mhmm", "mmhmm", "yeah", "yeh",
               "ues", "ya", "ja", "si", "oui", "yar", "yah", "yarp", "yes please", "sure thing", "yes pls"]
no_answers = ["no", "nope", "nop", "nay", "nah", "no way"]
joke_answers = ["kill myself", "poop", "summon key", "knock knock", "wingardium leviosa"]
personal_answers = ["check items", "items", "what do i have", "what things am i carrying", "what are my things",
                    "what am i carrying", "what stuff do i have", "what things do i have", "whats my stuff",
                    "what weapons", "my weapons", "what weapons do i have", "what weapons have i got", "whats my weapons",
                    "weapons", "where are my weapons", "which weapons do i have", "which weapons have i got",
                    "what weapons am i carrying", "which weapons am i carrying", "do i have weapons", "do i have things",
                    "do i have a sword", "check weapons", "gold", "how much gold do i have", "how much do i have",
                    "how much gold am i carrying", "do i have money", "how much money do i have"]
companion_answers = ["who am i travelling with", "who am i with", "who is with me", "i'm with who", "who with"]




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

    def __init__(self):
        self.door_locked = True

    def enter(self):
        if self._visited is not True:
            self._visited = True

            print(dedent("""
            You wake up in a room. You're all alone.
            The room is almost empty with just the chair you're sitting on, and a chest in the corner of the room.
            You see a door directly in front of you. What do you do?
            """))

        elif self.door_locked is False:
            print(dedent("""
            You open the door and walk forward. 
            """))
            self.door_locked = True
            self._visited = False


            return "tree_room"

        else:
            print(dedent("What do you do?"))

        answer = input("> ")

        if "door" in answer:
            if "a key" in players_stuff.things:
                print(dedent("""
                            You walk up to the door. It's locked, but there is a keyhole. You think it might fit the key from the chest. 
                            You put the key in the hole and turn. It fits. Do you want to unlock it?
                            """))

                answer = input("> ")
                if answer in yes_answers:
                    self.door_locked = False
                    return "entry_room"

                elif answer in joke_answers:
                    print("Come on... Take this seriously!")
                    return "entry_room"

                elif answer in no_answers:
                    print("You don't unlock the door. Do you want to stay here forever or something? Be Brave!")
                    return "entry_room"

                elif answer in personal_answers:
                    players_stuff.query_all_things()
                    return "entry_room"

                elif answer in companion_answers:
                    players_stuff.who_with()
                    return "entry_room"

                else:
                    return "entry_room"

            elif answer in joke_answers:
                print("Come on... Take this seriously!")
                return "entry_room"

            elif answer in no_answers:
                return "entry_room"

            elif answer in personal_answers:
                players_stuff.query_all_things()
                return "entry_room"

            elif answer in companion_answers:
                players_stuff.who_with()
                return "entry_room"

            else:
                print(dedent("""
                    You walk up to the door. It's locked. If only there were a key...
                    """))
                # This will set 'next_place_name' to be "entry_room", so the game will take you back to the start of the
                # entry room. Since you've already visited the room, it'll ask what you want to do.
                return "entry_room"

        elif "chest" in answer:
            print(dedent("""
            You walk towards the chest. 
            You try to open it but the closing mechanism is rusty and stiff. It's proving tough to open. 
            You struggle for a few minutes but eventually you feel the latch give, and the chest opens up. You look inside. 
            You see a key, and a rusty sword. Would you like to take them?
            """))

            answer = input("> ")

            if answer in yes_answers:
                players_stuff.weapon = "a rusty sword"
                players_stuff.new_thing("a key")
                print(dedent("""
                The sword may be rusty, but you feel safer knowing that you have some way to protect yourself. 
                Who knows what might reside within these walls...
                The key feels heavy in your pocket. What might it open?
                """))
                return "entry_room"

            elif answer in joke_answers:
                print("Come on... Take this seriously!")
                return "entry_room"

            elif answer in no_answers:
                print("You don't unlock the door. Do you want to stay here forever or something? Be Brave!")
                return "entry_room"

            elif answer in personal_answers:
                players_stuff.query_all_things()
                return "entry_room"

            elif answer in companion_answers:
                players_stuff.who_with()
                return "entry_room"

            else:
                return "entry_room"

        elif answer in joke_answers:
            print("Come on... Take this seriously!")
            return "entry_room"

        elif answer in no_answers:
            return "entry_room"

        elif answer in personal_answers:
            players_stuff.query_all_things()
            return "entry_room"

        elif answer in companion_answers:
            players_stuff.who_with()
            return "entry_room"

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




class Finished(Place):

    def enter(self):
        print("Congratulations! You've won!")
        return "finished"

class Map:

    places = {
        "entry_room": EntryRoom(),
        "tree_room": TreeRoom(),
        "table_room": TableRoom(),
        "troll_room": TrollRoom(),
        "kobold_room": KoboldRoom(),
        "dragon_room": DragonRoom(),
        "corridor": Corridor(),
        "riddle_room": RiddleRoom(),
        "finished": Finished(),
        "death": Death()
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
        self.weapon = "no weapons"
        self.companion = "nobody"
        self.things = ["clothes"]

    def who_with(self):
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

players_stuff.query_all_things()
