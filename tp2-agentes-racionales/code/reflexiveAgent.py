import random
import agent as a

class reflexiveAgent(a.Agent): 

    def __init__(self, env):
        super().__init__(env)


    def perceive(self): 
        return self.env.is_dirty(self.posX, self.posY)

    def clean(self):
        self.suck()
        self.performance += 1

    def random_move(self):
        movements = {
            0: self.up,
            1: self.down,
            2: self.left,
            3: self.right,
            4: self.idle
        }
        random_move = random.randint(0, 4)
        movements[random_move]()

    def think(self):
        necessary_moves = 0
        while self.mov > 0:  
            if self.env.get_dirty() > 0:  # revisa que al menos exista una casilla sucia
                necessary_moves += 1

            if self.perceive():
                self.clean()
            else:
                self.random_move()
            self.mov -= 1
        return self.performance, necessary_moves