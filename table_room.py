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