import game

class Finished(game.Place):

    def enter(self):
        print("Congratulations! You've won!")
        return "finished"

