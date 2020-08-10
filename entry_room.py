import place_and_items
from textwrap import dedent
from game import players_stuff

class EntryRoom(place_and_items.Place):

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
            if char not in place_and_items.punctuations:
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
                    if char not in place_and_items.punctuations:
                        answer = answer + char

                if answer in place_and_items.yes_answers:
                    self.door_locked = False
                    return "entry_room"

                elif answer in place_and_items.joke_answers:
                    print("Come on... Take this seriously!")
                    return "entry_room"

                elif answer in place_and_items.no_answers:
                    print("You don't unlock the door. Do you want to stay here forever or something? Be Brave!")
                    return "entry_room"

                elif answer in place_and_items.personal_answers:
                    players_stuff.query_all_things()
                    return "entry_room"

                elif answer in place_and_items.companion_answers:
                    players_stuff.who_with()
                    return "entry_room"

                else:
                    return "entry_room"

            elif answer in place_and_items.joke_answers:
                print("Come on... Take this seriously!")
                return "entry_room"

            elif answer in place_and_items.no_answers:
                return "entry_room"

            elif answer in place_and_items.personal_answers:
                players_stuff.query_all_things()
                return "entry_room"

            elif answer in place_and_items.companion_answers:
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
                if char not in place_and_items.punctuations:
                    answer = answer + char

            if answer in place_and_items.yes_answers:
                players_stuff.weapon = "a rusty sword"
                players_stuff.new_thing("a key")
                print(dedent("""
                The sword may be rusty, but you feel safer knowing that you have some way to protect yourself. 
                Who knows what might reside within these walls...
                The key feels heavy in your pocket. What might it open?
                """))
                return "entry_room"

            elif answer in place_and_items.joke_answers:
                print("Come on... Take this seriously!")
                return "entry_room"

            elif answer in place_and_items.no_answers:
                print("You don't unlock the door. Do you want to stay here forever or something? Be Brave!")
                return "entry_room"

            elif answer in place_and_items.personal_answers:
                players_stuff.query_all_things()
                return "entry_room"

            elif answer in place_and_items.companion_answers:
                players_stuff.who_with()
                return "entry_room"

            else:
                return "entry_room"

        elif answer in place_and_items.joke_answers:
            print("Come on... Take this seriously!")
            return "entry_room"

        elif answer in place_and_items.no_answers:
            return "entry_room"

        elif answer in place_and_items.personal_answers:
            players_stuff.query_all_things()
            return "entry_room"

        elif answer in place_and_items.companion_answers:
            players_stuff.who_with()
            return "entry_room"

        else:
            print("Input not recognised")
            return "entry_room"