
from abc import ABC, abstractmethod
import random

class Agent(ABC):

    def __init__(self, env: Environment = None) -> None:

        self.env = env
        self.posX = random.randint(0,self.env.sizeX - 1)
        self.posY = random.randint(0,self.env.sizeY - 1)
        self.performance = 0 # Cantidad de casillas limpiadas
        self.mov = 1000 # Cantidad limite de acciones

        self.env: Enviroment = env

    
    def up(self):
        if self.env.acceptAction("Arriba", self.posX , self.posY):
            self.posX += 1
        return
        
    def down(self):
        if self.env.acceptAction("Abajo", self.posX , self.posY):
            self.posX -= 1
        return
        
    def left(self):
        if self.env.acceptAction("Izquierda", self.posX , self.posY):
            self.posY -= 1       
        return    
    def right(self):
        if self.env.acceptAction("Derecha", self.posX , self.posY):
            self.posY += 1
        return
    
    def suck(self): # Limpia
        return self.env.acceptAction("Limpiar", self.posX , self.posY)
        
    def idle(self): #No hacer nada
        return
    
    @abstractmethod
    def think(self):
        pass #Metodo a ser implementado por las subclases

        
