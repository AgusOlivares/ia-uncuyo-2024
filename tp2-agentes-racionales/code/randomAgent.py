import agent as a
import random


class randomAgent(a.Agent): 

    def __init__(self, env):
        super().__init__(env)

    def random_move(self):
        movements = {
            0: self.up,
            1: self.down,
            2: self.left,
            3: self.right,
            4: self.clean,
            5: self.idle
        }
        random_move = random.randint(0, 5)
        movements[random_move]()

    def clean(self):
        if self.suck():  
            self.performance += 1

    def think(self):
        necessaryMoves = 0
        while self.mov != 0:
            if self.env.get_dirty() != 0:
                necessaryMoves += 1 
            self.random_move()
            self.mov -= 1
        return self.performance , necessaryMoves 