
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