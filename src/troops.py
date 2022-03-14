import numpy as np
from abc import ABC, abstractmethod
import gvars
import village as vlg
import buildings as bldg
import time

class Troops(ABC) :
    code = 0
    dim = (1, 1)
    max_hp = 0
    damage = 0
    
    art = np.zeros(dim, dtype = object)
                
    @abstractmethod
    def set_art(self) :
        pass
    
    @abstractmethod
    def move(self, pos, village, sig) :
        pass
    

    
class Barbarian(Troops) :
    max_hp = 50
    code = 6
    damage = 20

    
    
    def __init__(self, prev_conf) :
        self.art = np.zeros(self.dim, dtype = object)
        self.hp = self.max_hp
        self.prev_conf = prev_conf
        self.set_art()
        self.target = None
        print(self.art)
        
        
        
    def set_art(self):
        self.art[0][0] = (self, '♝ ')
        
        
    
    
    
    def find_target(self, pos, village) :

        distance = 100
                
        for building, posit in village.buildings.items() :
            if (isinstance(building, bldg.SpawnPoint) or isinstance(building, bldg.Wall) or (building.hp <= 0)) :
                continue 
            
            
            if gvars.mv_distance(posit, pos) < distance :
                distance = gvars.mv_distance(posit, pos)
                self.target = building
                
        # print(self.target)
        # print(village.buildings[self.target])
        # time.sleep(3)
            
            
    
    
    def move(self, pos, village, sig) :
        
        if (self.target is None) or (self.target.hp <= 0) :
            self.find_target(pos, village)

        target_pos = village.buildings[self.target]
        moves = [(pos[0], pos[1] + 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0] - 1, pos[1])]
            
        next = moves[0]
        dist = gvars.euc_distance(moves[0], target_pos)
        
        
        
            
        for mv in moves :
             if (gvars.euc_distance(mv, target_pos) < dist) :
                 next = mv
                 dist = gvars.euc_distance(mv, target_pos)
                #  print(mv)
                #  print(next)
                #  print(dist)
                #  exit()
        
        
        
        if (isinstance(village.map[next[0]][next[1]][0], bldg.Building) and 
            (not isinstance(village.map[next[0]][next[1]][0], bldg.SpawnPoint)) and 
            (village.map[next[0]][next[1]][0].hp > 0)) :
            
            village.map[next[0]][next[1]][0].hp -= self.damage
            building = village.map[next[0]][next[1]][0]
            if ((building.hp <=0) and village.live_builds.__contains__(building)) :
                    village.live_builds.remove(building)
        
        else :
            trp = village.map[pos[0]][pos[1]]
            village.map[pos[0]][pos[1]] = village.base_map[pos[0]][pos[1]]
            self.prev = village.map[next[0]][next[1]]
            village.map[next[0]][next[1]] = trp
            village.troops[self] = (next[0], next[1])
    
   
   
   
   
    
class King(Troops) :
    code = 5
    max_hp = 100
    damage = 25
    
    def __init__(self, prev_conf) :
        self.art = np.zeros((1, 1), dtype = object)
        self.direction = [1, 0]
        self.hp = self.max_hp
        self.set_art()
        # self.loc = gvars.spawn_point_loc[prev_conf[]]
        self.prev_conf = prev_conf
        
        
        
    def set_art(self):
        self.art[0][0] = (self, '🨀 ')
        
        

    def leviathan(self, pos, village) :
        
        for building, posit in village.buildings.items() :
            if (not isinstance(building, bldg.SpawnPoint)) and (gvars.euc_distance(pos, posit) < 10) :
                building.hp -= 10
                if ((building.hp <=0) and village.live_builds.__contains__(building)) :
                    village.live_builds.remove(building)
        
        
        
                
    def move(self, pos, village, sig) :
        if(self.hp <= 0) :
            return
        
        dirs = {'w': [-1, 0], 'a': [0, -1], 's': [1, 0], 'd': [0, 1],}
        
        if (sig in dirs.keys()) :
            self.direction = dirs[sig]
           
            
            if village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0] is None :
                return
            
            elif not ((isinstance(village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0], bldg.Building)) and 
                      (not isinstance(village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0], bldg.SpawnPoint)) and 
                      (village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0].hp > 0)) :
                
                
                # temp = (self, '🨀 ')
                # village.map[pos[0]][pos[1]] = self.prev_conf
                village.map[pos[0]][pos[1]] = village.base_map[pos[0]][pos[1]]
                
                self.prev_conf = village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0]
                
                village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]] = self.art[0][0]

                village.troops[self] = (pos[0] + self.direction[0], pos[1] + self.direction[1])
                
   
        elif sig == 'x' :
            self.leviathan(pos, village)
    
        elif sig == ' ' :
            if(isinstance(village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0], bldg.Building) and
               (not isinstance(village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0], bldg.SpawnPoint)) and 
               (village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0].hp > 0)) :
                
                building = village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0]
                village.map[pos[0] + self.direction[0]][pos[1] + self.direction[1]][0].hp -= self.damage
                if ((building.hp <=0) and village.live_builds.__contains__(building)) :
                    village.live_builds.remove(building)