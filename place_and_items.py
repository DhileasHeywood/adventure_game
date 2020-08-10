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


class Place:

    _visited = False

    def enter(self):
        print("This place is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)