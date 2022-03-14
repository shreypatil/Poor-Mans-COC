import numpy as np
from abc import ABC, abstractmethod
import gvars
import village as vlg
import buildings as bldg



class Building(ABC):
    code = 0
    max_hp = 0
    dim = (0, 0)
    
                
    @abstractmethod
    def set_art(self) :
        pass
    


class TownHall(Building) :
    
    max_hp = 100
    dim = (4, 3)
    code = 1
    
    def __init__(self) : 
        self.art = np.zeros(self.dim, dtype = object)
        self.hp = self.max_hp       
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self, ' ')
                
                
        self.art[0][0] = (self, ' ༼')
        self.art[0][1] = (self, '☤☤')
        self.art[0][2] = (self, '༽ ')
        self.art[1][0] = (self, '░░')
        self.art[1][1] = (self, '░░')
        self.art[1][2] = (self, '░░')
        self.art[2][0] = (self, '▒▒')
        self.art[2][1] = (self, '▒▒')
        self.art[2][2] = (self, '▒▒')
        self.art[3][0] = (self, '▓▓')
        self.art[3][1] = (self, '▓▓')
        self.art[3][2] = (self, '▓▓')
        



class Hut(Building) :
    
    max_hp = 75
    dim = (3, 3)
    code = 2
    
    def __init__(self) :
        self.art = np.zeros(self.dim, dtype = object)
        self.hp = self.max_hp        
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self, ' ')
                
        
        self.art[0][0] = (self, '༼‾')
        self.art[0][1] = (self, '‾‾')
        self.art[0][2] = (self, '‾༽')
        self.art[1][0] = (self, '░░')
        self.art[1][1] = (self, '░░')
        self.art[1][2] = (self, '░░')
        self.art[2][0] = (self, '▒▒')
        self.art[2][1] = (self, '▒▒')
        self.art[2][2] = (self, '▒▒')
        
        
        
        
class Cannon(Building) :
    
    max_hp = 100
    dim = (2, 1)
    code = 3
    damage = 2
    
    def __init__(self) : 
        self.art = np.zeros(self.dim, dtype = object)
        self.hp = self.max_hp       
        self.set_art()
        
        
    def set_art(self):
        
        for i in range(self.dim[0]) :
            for j in range(self.dim[1]) :
                self.art[i][j] = (self, ' ')
                
        
        self.art[0][0] = (self, '╁ ')
        self.art[1][0] = (self, '☒ ')
        
    def attack(self, pos, village) :
        if(self.hp <= 0) : return
        
        for troop, posit in village.troops.items() :
            
            if (gvars.euc_distance(pos, posit) < 10) :
                troop.hp -= 3
                if (troop.hp <= 0) and (village.live_troops.__contains__(troop)) :
                    village.live_troops.remove(troop)
                break;

        
        

class Wall(Building) :
    
    max_hp = 50
    dim = (1, 1) 
    code = 3
    
    def __init__(self) : 
        self.hp = self.max_hp     
        self.set_art()
        
        
    def set_art(self):
        self.art = np.zeros(self.dim, dtype = object)
        self.art[0][0] = (self, 'x ')
        
        
        
class SpawnPoint(Building) :
    
    dim = (1, 1)
    code = 4
    
    
    def __init__(self, subcode) : 
        self.subcode = subcode       
        self.set_art()

        
        
    def set_art(self):
        self.art = np.zeros(self.dim, dtype = object)
        art_dict = {'J': '🅙 ',
                    'K': '🅚 ',
                    'L': '🅛 '}

        self.art[0][0] = (self, art_dict[self.subcode])