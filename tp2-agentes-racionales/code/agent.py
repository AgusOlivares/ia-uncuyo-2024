
from abc import ABC, abstractmethod
import random

class Agent(ABC):

    def __init__(self, env = None):

        self.env = env
        self.posX, self.posY = self.get_initial_position()
        self.performance = 0 # Cantidad de casillas limpiadas
        self.mov = 1000 # Cantidad limite de acciones

        self.env = env

    def get_initial_position(self):
        return random.randint(0, self.env.sizeX - 1), random.randint(0, self.env.sizeY - 1)


    
    def up(self):
        if self.env.acceptAction("Up", self.posX , self.posY):
            self.posX += 1
        return
        
    def down(self):
        if self.env.acceptAction("Down", self.posX , self.posY):
            self.posX -= 1
        return
        
    def left(self):
        if self.env.acceptAction("Left", self.posX , self.posY):
            self.posY -= 1       
        return    
    
    def right(self):
        if self.env.acceptAction("Right", self.posX , self.posY):
            self.posY += 1
        return
    
    def suck(self): # Limpia
        return self.env.acceptAction("Clean", self.posX , self.posY)
        
    def idle(self): #No hacer nada
        return
    
    @abstractmethod
    def think(self):
        pass #Metodo a ser implementado por las subclases

        

