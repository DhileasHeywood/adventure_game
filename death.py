import game
from random import randint

class Death(game.Place):


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
            if char not in game.punctuations:
                answer = answer + char

        if answer == "yes":
            # I need to figure out how to restart the game, but I'll put it here.
            return "entry_room"

        else:
            exit(1)
