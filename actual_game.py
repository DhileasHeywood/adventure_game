from random import randint
from textwrap import dedent

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
        raw_answer = input("> ").lower()
        answer = ""
        for char in raw_answer:
            if char not in punctuations:
                answer = answer + char

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

        raw_answer = input("> ").lower()
        answer = ""
        for char in raw_answer:
            if char not in punctuations:
                answer = answer + char

        if "door" in answer:
            if "a key" in players_stuff.things:
                print(dedent("""
                            You walk up to the door. It's locked, but there is a keyhole. You think it might fit the key from the chest. 
                            You put the key in the hole and turn. It fits. Do you want to unlock it?
                            """))

                raw_answer = input("> ").lower()
                answer = ""
                for char in raw_answer:
                    if char not in punctuations:
                        answer = answer + char

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

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

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


class TableRoomSkeleton(Place):

    def enter(self):

        if self._visited is not True:
            self._visited = True


            if players_stuff.weapon is not None:
                print(dedent(f"""
                You grip your {players_stuff.weapon} just in case as you step closer to the skeleton. In a quiet 
                voice, you call out 'hello!'. The silence is heavy. You step forward again and repeat 'hello!'. 
                For a second, you start to relax. Then all of a sudden, the skeleton jumps to its feet, its own sword
                drawn! Do you stand and fight?
                """))

            else:
                print(dedent("""
                You step closer to the skeleton. In a quiet voice, you call out 'hello!'. The silence is heavy. You 
                step forward again and repeat 'hello!'. For a second, you start to relax. Then all of a sudden, the 
                skeleton jumps to its feet, its own sword drawn! Do you stand and fight?
                """))

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                    if char not in punctuations:
                        answer = answer + char

            if answer in yes_answers:
                if players_stuff.weapon is not None:
                    die = randint(1, 3)
                    if die == 1:
                        print(dedent("""
                        The skeleton runs at you, sword drawn, at the last second, you manage to parry the attack,
                        but the skeleton is quick. You keep parrying its blows, but it keeps delivering them. You 
                        eventually begin to tire, and the skeleton makes a slash. It makes contact. You fall, and see
                        the skeleton looking over you with his sword ready to plunge into your heart.
                        """))
                        return "death"

                    else:
                        print(dedent("""
                        The skeleton runs at you, sword drawn, at the last second, you manage to parry the attack,
                        but the skeleton is quick. You keep parrying its blows, but it keeps delivering them. You 
                        eventually fall into a rhythm, and start to see the skeleton's pattern of attacks. You see 
                        and opening, and make your move. You slash at the skeleton's neck, and make contact, watch as
                        their whole body falls to pieces on the floor. 
                        """))
                        self.skeleton_alive = False
                        return "table_room"

                else:
                    print(dedent("""
                    You raise your fists in an attempt to fight off the skeleton, but as it readies its first blow, 
                    you realise what a horrible mistake you've made. What possessed you to fight a skeleton with a 
                    sword when you've nothing to defend yourself with?! 'I'm such a fool!' you think to yourself, as
                    you savour the last few moments of life before you get hacked to pieces.
                    """))
                    return "death"

            else:
                    print(dedent("""
                    You turn to flee. You're close to the door leading out of the room, so you make a break
                    for it, praying that it's not locked. You're in luck! It's open. You burst through, and 
                    slam the door behind you, keeping all of your weight against it. You hear the skeleton
                    banging against the door, but thankfully, after a tense few minutes, it seems to give up.
                    """))
                    return "finished"



        else:
            pass


class TableRoomFarSide(Place):

    def enter(self):

        print("What do you do?")

        if self.visited is False:
            self.visited = True

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

            if TableRoom.skeleton_alive == True:

                if "approach" in answer or "fight" in answer or "sword" in answer or ("draw" and "weapon" in answer):
                    return "table_room_skeleton"

                elif "talk" in answer or "introduce" in answer or "friend" in answer:
                    print(dedent("""
                    You introduce yourself to the skeleton. The skeleton turns its head in your direction and opens its
                    jaw to speak. 
                    'My name is Nigellus the Resolute of Ironpoint. What brings you to my halls?'
                    You look at him in astonishment and answer.
                    'I don't know. I'm trying to find my way home.'
                    Nigellus regards you for a second, seemingly thinking about what to do with you. He extends a hand with
                    a few gold coins, and extends his sword for you to take.
                    'You'll need these to reach the surface. I have long been isolated, trapped within these walls. I forget
                    why I came here in the first place. Take these, on the condition that you release me from this existence'
                    Do you take the gifts?
                    """))

                    raw_answer = input("> ").lower()
                    answer = ""
                    for char in raw_answer:
                        if char not in punctuations:
                            answer = answer + char

                    if answer in yes_answers:
                        players_stuff.add_gold(10)
                        players_stuff.weapon = "a gleaming longsword"
                        TableRoom.skeleton_alive = False
                        print(dedent("""
                        You take the gleaming longsword and the gold from Nigellus. You thank him for the gifts, and look 
                        down at the floor as you prepare yourself. You raise the sword and relieve Nigellus of his troubled
                        existence.
                        """))
                        return "table_room_far_side"

                elif "table" in answer or "eat" in answer or "food" in answer:
                    print("you can't do that yet, sorry")
                    return "table_room"

                elif "back" in answer or "flee" in answer or "run" in answer:
                    print(dedent("""
                    You turn around and hurry back to the door you just came from. But it's locked. How...? But there's
                    no time to worry about that. You run to the other door, and to your relief, it's unlocked. You 
                    turn around to see that the skeleton has gotten up, and is running towards you! You slip through
                    the door and hold it shut behind you, just as you hear the skeleton make contact with it. After 
                    a few tense minutes of banging, you sense that the skeleton has given up"""))
                    return "finished"

                elif answer in personal_answers:
                    players_stuff.query_all_things()
                    return "table_room_far_side"

                elif answer in companion_answers:
                    players_stuff.who_with()
                    return "table_room_far_side"

                else:
                    print("Input not recognised")
                    return "table_room_far_side"

            else:
                if "table" in answer or "eat" in answer or "food" in answer:
                    print("you can't do that yet, sorry")
                    return "table_room"

                elif answer in personal_answers:
                    players_stuff.query_all_things()
                    return "table_room_far_side"

                elif answer in companion_answers:
                    players_stuff.who_with()
                    return "table_room_far_side"

                else:
                    print("Input not recognised")
                    return "table_room_far_side"

        else:
            print(dedent("""
            You're standing next to the table. The table is laid, and there are doors behind you, and on the wall to 
            your left. What do you do?
            """))
            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

            if answer in personal_answers:
            players_stuff.query_all_things()
            return "table_room_far_side"

            elif answer in companion_answers:
            players_stuff.who_with()
            return "table_room_far_side"

            elif "table" in answer or "eat" in answer or "food" in answer:
            print("you can't do that yet, sorry")
            return "table_room"

            else:
            print("Input not recognised")
            return "table_room_far_side"


class TableRoom(Place):

    skeleton_alive = True

    def enter(self):
        if self._visited is not True:
            self._visited = True
            print(dedent("""
            You emerge into a long room. It looks a lot like the great halls of castles described in the fairytales 
            you were told as a child. There's a long table in the middle of the room, with places all laid out, and empty
            dishes. At the head of the table, in the biggest chair there's a figure wearing a crown, but with the
            roaring fire behind them, you can't make out any details. On the right wall, there's a door. What do you do?
            """))

        else:
            print(dedent("""
            You're standing at the foot of the table with a door behind you, and a door in the wall to your right. What 
            do you do?
            """))

        raw_answer = input("> ").lower()
        answer = ""
        for char in raw_answer:
            if char not in punctuations:
                answer = answer + char

        if "figure" in answer or "person" in answer or "crown" in answer or "introduce" in answer:
            print(dedent("""
            You walk around the table, and closer to the figure in the chair. You get a prickly feeling on the back of 
            your neck. Something's not right.....
            And suddenly, you see it! It's not a person! It's a skeleton! You stumble backwards in shock.
            """))
            return "table_room_far_side"

        elif "table" in answer or "food" in answer or "feast" in answer or "eat" in answer:
            pass

        elif "door" in answer:
            pass

        elif answer in personal_answers:
            players_stuff.query_all_things()
            return "table_room"

        elif answer in companion_answers:
            players_stuff.who_with()
            return "table_room"

        else:
            print("Input not recognised")
            return "table_room"


class TreeInTreeRoom(Place):

    def __init__(self):
        self.investigated = False

    def enter(self):
        if self._visited is not True and self.investigated is not True:
            self._visited = True
            print(dedent("""
            You've climbed the tree. You've made it all the way to the the top. From here you can see 
            the painting more clearly. One of the branches actually extends towards it. One of the torches on the wall 
            flickers, and you see a glint in the painting. Do you want to investigate?
            """))

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

            if answer in yes_answers:
                self.investigated = True
                print(dedent("""
                You carefully climb along the branch, which gets narrower as you get closer to the wall.
                You reach as far as you thing you can get, close enough to touch the wall. You notice that a portion of 
                the wall has been carved out over an area of treasure, and replaced with gold! You take the gold, and 
                climb back along the branch to safety. You glance back at the painting one last time, and climb back 
                down the tree.
                """))
                return "tree_room"

            elif answer in no_answers:
                print(dedent("""
                You look at the spot for a little longer, and don't see any more glints, so you write it
                off as a trick of the light and climb back down.
                """))
                return "tree_room"

            elif answer in personal_answers:
                players_stuff.query_all_things()
                return "tree_in_tree_room"

            elif answer in companion_answers:
                players_stuff.who_with()
                return "tree_in_tree_room"

            else:
                print("Input not recognised")
                return "tree_in_tree_room"

        elif self._visited is True and self.investigated is not True:
            print("You're at the top of the tree. What do you do?")

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

            if "glint" in answer or "investigate" in answer:
                self.investigated = True
                players_stuff.add_gold(30)
                print(dedent("""
                You carefully climb along the branch, which gets narrower as you get closer to the wall.
                You reach as far as you thing you can get, close enough to touch the wall. You notice that a portion of 
                the wall has been carved out over an area of treasure, and replaced with 30 gold coins! You take the 
                gold, and climb back along the branch to safety. You glance back at the painting one last time, and 
                climb back down the tree.
                """))
                return "tree_room"

            elif "down" in answer or "back" in answer:
                print(dedent("""
                You look at the spot where you saw the glint for a little longer, and don't see any more, 
                so you write it off as a trick of the light and climb back down.
                """))
                return "tree_room"

            elif answer in personal_answers:
                players_stuff.query_all_things()
                return "tree_in_tree_room"

            elif answer in companion_answers:
                players_stuff.who_with()
                return "tree_in_tree_room"

            else:
                print("Input not recognised")
                return "tree_in_tree_room"

        else:
            print(dedent("""You're at the top of the tree. What do you do?
            """))

            raw_answer = input("> ").lower()
            answer = ""
            for char in raw_answer:
                if char not in punctuations:
                    answer = answer + char

            if "glint" in answer or "investigate" in answer:
                self.investigated = True
                print(dedent("""
                You can't see any more spots that would hide gold, so you climb back down the tree. 
                """))
                fall = randint(1, 2)

                if fall == 1:
                    return "tree_room"

                else:
                    print("As you're climbing down, your foot sips off of a loose bit of bark. You fall.")
                    return "death"

            elif "down" in answer or "back" in answer:
                print(dedent("""
                You're not sure why you climbed the tree again... Is that what it feels like to have a moment of 
                madness...? Never mind, you climb back down again. 
                """))
                return "tree_room"

            elif answer in personal_answers:
                players_stuff.query_all_things()
                return "tree_in_tree_room"

            elif answer in companion_answers:
                players_stuff.who_with()
                return "tree_in_tree_room"

            else:
                print("Input not recognised")
                return "tree_in_tree_room"


class TreeRoom(Place):

    def enter(self):
        if self._visited is not True:
            self._visited = True

            print(dedent("""
            You walk into a large room with a high ceiling. Right in the centre of the room there is a tall oak tree. 
            You see a door on the wall to your left. On the wall in front of you
            there is a fresco of a knight battling a dragon on a huge pile of treasure. What do you do?
            """))

        else:
            print("What do you do?")

        raw_answer = input("> ").lower()
        answer = ""
        for char in raw_answer:
            if char not in punctuations:
                answer = answer + char

        if "left" in answer or "door" in answer:
            print(dedent("""
            You walk up to the door on the left. You turn the handle, fully expecting it to be locked. 
            To your surprise, it opens easily. You step through.
            """))
            return "table_room_skeleton"

        # elif "right" in answer:
        #    pass

        elif "tree" in answer:
            print(dedent("""
            You go up to the tree. You look at it for a second, and think to yourself 'I can climb that'. So you do.
            """))
            return "tree_in_tree_room"

        elif answer in joke_answers:
            print("Come on... Take this seriously!")
            return "tree_room"

        elif answer in no_answers:
            return "tree_room"

        elif answer in personal_answers:
            players_stuff.query_all_things()
            return "tree_room"

        elif answer in companion_answers:
            players_stuff.who_with()
            return "tree_room"

        else:
            print("Input not recognised")
            return "tree_room"


class Finished(Place):

    def enter(self):
        print("Congratulations! You've won!")
        return "finished"


class Map:

    places = {
        "entry_room": EntryRoom(),
        "tree_room": TreeRoom(),
        "tree_in_tree_room": TreeInTreeRoom(),
        "table_room": TableRoom(),
        "table_room_far_side": TableRoomFarSide(),
        "table_room_skeleton": TableRoomSkeleton(),
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
        self.weapon = None
        self.companion = "nobody"
        self.things = ["clothes"]

    def who_with(self):
        if self.companion is "nobody":
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
a_map = Map("table_room")
a_game = Engine(a_map)
a_game.play()
