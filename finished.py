import place_and_items

class Finished(place_and_items.Place):

    def enter(self):
        print("Congratulations! You've won!")
        return "finished"

