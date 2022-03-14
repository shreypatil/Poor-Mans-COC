import numpy as np
from abc import ABC, abstractmethod

class Building(ABC):
    code = 0
    max_hp = 0
    dim = (0, 0)
    art = np.zeros(dim, dtype = object)
                
    @abstractmethod
    def set_art(self) :
        pass
    


class TownHall(Building) :
    
    max_hp = 100
    dim = (4, 3)
    art = np.zeros(dim, dtype = object)
    code = 1
    
    def __init__(self) :        
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self.code, ' ')
                
                
        self.art[0][0] = (self.code, ' ༼')
        self.art[0][1] = (self.code, '☤☤')
        self.art[0][2] = (self.code, '༽ ')
        self.art[1][0] = (self.code, '░░')
        self.art[1][1] = (self.code, '░░')
        self.art[1][2] = (self.code, '░░')
        self.art[2][0] = (self.code, '▒▒')
        self.art[2][1] = (self.code, '▒▒')
        self.art[2][2] = (self.code, '▒▒')
        self.art[3][0] = (self.code, '▓▓')
        self.art[3][1] = (self.code, '▓▓')
        self.art[3][2] = (self.code, '▓▓')
        



class Hut(Building) :
    
    max_hp = 25
    dim = (3, 3)
    art = np.zeros(dim, dtype = object)
    code = 2
    
    def __init__(self) :        
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self.code, ' ')
                
        
        self.art[0][0] = (self.code, '༼‾')
        self.art[0][1] = (self.code, '‾‾')
        self.art[0][2] = (self.code, '‾༽')
        self.art[1][0] = (self.code, '░░')
        self.art[1][1] = (self.code, '░░')
        self.art[1][2] = (self.code, '░░')
        self.art[2][0] = (self.code, '▒▒')
        self.art[2][1] = (self.code, '▒▒')
        self.art[2][2] = (self.code, '▒▒')
        
        
        
        
class Cannon(Building) :
    
    max_hp = 100
    dim = (2, 1)
    art = np.zeros(dim, dtype = object)
    code = 3
    damage = 2
    
    def __init__(self) :        
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self.code, ' ')
                
        
        self.art[0][0] = (self.code, '╁ ')
        self.art[1][0] = (self.code, '☒ ')

        
        

class Wall(Building) :
    
    max_hp = 100
    dim = (1, 1)
    art = np.zeros(dim, dtype = object)
    code = 3
    
    def __init__(self) :        
        self.set_art()
        
        
    def set_art(self):
        self.art[0][0] = (self.code, '• ')
        
        
        
class SpawnPoint(Building) :
    
    dim = (1, 1)
    art = np.zeros(dim, dtype = object)
    code = 4
    
    
    def __init__(self, subcode) : 
        self.subcode = subcode       
        self.set_art()
        
        
    def set_art(self):
        art_dict = {'J': '🅙 ',
                    'K': '🅚 ',
                    'L': '🅛 '}
        self.art[0][0] = (self.code, art_dict[self.subcode])