import numpy as np
from colorama import init, Fore, Back, Style
import time
import os
import buildings as bldg 

class Village:
    m = 50
    n = 50
    
    
    def __init__(self, mode = 0) :
        
        self.bulidings = {}
        self.troops = []
        self.active_spawn_point = 'J'

        self.map = np.zeros((self.m, self.n), dtype=object)
        
        for i in range(self.m) :
            for j in range(self.n) :
                self.map[i][j] = (0, '  ')
        
        self.mk_border()
        
        self.default_map()
        
    
    
    
    def mk_border(self) :
        for i in range(self.n) :
            self.map[0][i] = (-1, '--')
            self.map[self.m-1][i] = (-1, '--')
            
        for j in range(self.m) :
            self.map[j][0] = (-1, '| ')
            self.map[j][self.n-1] = (-1, ' |')
            
        self.map[0][0] = (-1, '+-')
        # self.map[0][0][1] = '+'
        self.map[0][self.n-1] = (-1, '-+')
        self.map[self.m-1][0] = (-1, '+-')
        self.map[self.m-1][self.n-1] = (-1, '-+')
        
        
        
    def default_map(self) :
        self.place(bldg.TownHall(), (20, 25))
        self.place(bldg.Hut(), (10, 10))
        self.place(bldg.Hut(), (40, 17))
        self.place(bldg.Hut(), (22, 14))
        self.place(bldg.Hut(), (10, 10))
        self.place(bldg.Hut(), (16, 32))
        self.place(bldg.Hut(), (16, 36))
        self.place(bldg.Hut(), (36, 27))
        self.place(bldg.Cannon(), (21, 23))
        self.place(bldg.Cannon(), (21, 29))
        self.place(bldg.SpawnPoint(subcode='J'), (40, 40))
        self.place(bldg.SpawnPoint(subcode='K'), (5, 36))
        self.place(bldg.SpawnPoint(subcode='L'), (45, 6))
        
        for i in range(7, 40) :
            self.place(bldg.Wall(), (i, 5))
        
        for i in range(5, 42) :
            self.place(bldg.Wall(), (7, i))
            
        for i in range(7, 37) :
            self.place(bldg.Wall(), (i, 42))
            
        for i in range(13, 37) :
            self.place(bldg.Wall(), (46, i))
            
        for i in range(37, 43) :
            self.place(bldg.Wall(), (37, i))
            
        for i in range(37, 47) :
            self.place(bldg.Wall(), (i, 37))
            
        for i in range(5, 14) :
            self.place(bldg.Wall(), (40, i))
            
        for i in range(40, 47) :
            self.place(bldg.Wall(), (i, 13))
        
        #######################################
            
        for i in range(18, 26) :
            self.place(bldg.Wall(), (i, 22))
        
        for i in range(22, 30) :
            self.place(bldg.Wall(), (18, i))
            
        for i in range(18, 26) :
            self.place(bldg.Wall(), (i, 30))
            
        for i in range(22, 31) :
            self.place(bldg.Wall(), (26, i))
                
    
    def render(self) :
        # print(self.map)
        os.system('clear')
        
        terminal_sz = os.get_terminal_size()
        print(' ' * (44 + (terminal_sz.columns - 100) // 2 - 1), 'Terminal CoC', ' ' * 44)
        for i in self.map :
            row = []
            for j in i :
                row.append(Back.BLACK + j[1] + Back.RESET)
            
            print(' ' * ((terminal_sz.columns - 100) // 2 - 1), ''.join(row))
            
    
    
    def place(self, building, position) :
        
        self.bulidings.add(position, building)
        
        for i in range(building.dim[0]) :
            for j in range(building.dim[1]) :
                self.map[position[0]+i][position[1]+j] = building.art[i][j]