import numpy as np
from abc import ABC, abstractmethod
import gvars

class Troops(ABC) :
    code = 0
    dim = (1, 1)
    max_hp = 0
    
    art = np.zeros(dim, dtype = object)
                
    @abstractmethod
    def set_art(self) :
        pass
    
    @abstractmethod
    def move(self) :
        pass
    
class Barbarian(Troops) :
    
    def __init__(self) :
        self.max_hp = 50
        self.hp = self.max_hp
        
    def set_art(self):
        self.art[0][0] = (6, '♝ ')
        
    def move(self) :
        pass
        
    
    
    
class King(Troops) :
    
    def __init__(self, prev_conf) :
        self.max_hp = 100
        self.hp = self.max_hp
        self.loc = gvars.spawn_point_loc[prev_conf]
        self.prev_conf = prev_conf
        self.path = self.find_path()
        
    def find_path(self, village) :
        pass
        
    def set_art(self):
        self.art[0][0] = (5, '🨀 ')
        
    def move(self) :
        pass
    