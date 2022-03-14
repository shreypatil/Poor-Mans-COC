from multiprocessing.context import SpawnContext
import troops
import numpy as np
from colorama import init, Fore, Back, Style
import time
import os
import buildings as bldg 

class Village:
    m = 50
    n = 50
    max_barb_count = 2
    
    
    def __init__(self, mode = 0) :
        
        self.buildings = {}
        self.troops = {}
        self.active_spawn_point = None
        self.spawn_pts = {}
        self.barb_count = 0
        self.king_count = 0
        self.king = None
        self.live_troops = set()
        self.live_builds = set()
        self.deployed = 0
        

        self.map = np.zeros((self.m, self.n), dtype=object)
        self.base_map = np.zeros((self.m, self.n), dtype=object)
        
        for i in range(self.m) :
            for j in range(self.n) :
                self.map[i][j] = (0, '  ')
        
        self.mk_border()
        
        self.default_map()
        
    
    
    
    def mk_border(self) :
        for i in range(self.n) :
            self.map[0][i] = (None, '--')
            self.map[self.m-1][i] = (None, '--')
            
        for j in range(self.m) :
            self.map[j][0] = (None, '| ')
            self.map[j][self.n-1] = (None, ' |')
            
        self.map[0][0] = (None, '+-')
        # self.map[0][0][1] = '+'
        self.map[0][self.n-1] = (None, '-+')
        self.map[self.m-1][0] = (None, '+-')
        self.map[self.m-1][self.n-1] = (None, '-+')
        
        
        
    def default_map(self) :
        self.place(bldg.TownHall(), (20, 25))
        self.place(bldg.Hut(), (10, 10))
        self.place(bldg.Hut(), (40, 17))
        self.place(bldg.Hut(), (22, 14))
        self.place(bldg.Hut(), (16, 32))
        self.place(bldg.Hut(), (16, 36))
        self.place(bldg.Hut(), (36, 27))
        self.place(bldg.Cannon(), (21, 23))
        self.place(bldg.Cannon(), (21, 29))
        
        
        self.spawn_pts['J'] = bldg.SpawnPoint(subcode='J')
        print(self.spawn_pts['J'].art)
        self.spawn_pts['L'] = bldg.SpawnPoint(subcode='L')
        print(self.spawn_pts['L'].art)
        self.spawn_pts['K'] = bldg.SpawnPoint(subcode='K')
        print(self.spawn_pts['K'].art)
        

        
        self.active_spawn_point = self.spawn_pts['J']

        
        self.place(self.spawn_pts['J'], (40, 40))
        self.place(self.spawn_pts['K'], (5, 36))
        self.place(self.spawn_pts['L'], (45, 6))
        
        
        
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
            
        for i in range(18, 26) :
            self.place(bldg.Wall(), (i, 22))
        
        for i in range(22, 30) :
            self.place(bldg.Wall(), (18, i))
            
        for i in range(18, 26) :
            self.place(bldg.Wall(), (i, 30))
            
        for i in range(22, 31) :
            self.place(bldg.Wall(), (26, i))
            
        for i in range(self.m) :
            for j in range(self.n) :
                self.base_map[i][j] = self.map[i][j]
            
            
            
    def set_color(self, building) :
        
        if isinstance(building, bldg.SpawnPoint) :
            if building == self.active_spawn_point :
                return Fore.BLUE
            
            return Fore.MAGENTA
        
        if not (isinstance(building, troops.Troops) or isinstance(building, bldg.Building)) :
            return ''
        
        
        hp_frac = building.hp / building.max_hp
        
        if (hp_frac > 0.5) :
            return Fore.GREEN
        
        if (hp_frac > 0.2) :
            return Fore.YELLOW
        
        if (hp_frac > 0) :
            return Fore.RED
        
        if (hp_frac <= 0) :
            return Fore.BLACK
    
        return ''
                
    
    
    def hp_bar(self) :
        if self.king is None :
            return ''
        
        bar = []
        health_frac = (float(self.king.hp) / troops.King.max_hp) * 20
        for i in range(20) :
            if i < health_frac :      
                bar.append(Back.GREEN + Style.DIM + Fore.BLACK + "░░" + Back.RESET + Fore.RESET + Style.RESET_ALL)
                
            else :
                bar.append(Fore.BLACK + "░░" + Back.RESET + Fore.RESET)
                
        return (''.join(bar))      
        
    
    
    def render(self, input) :
        if (self.deployed == 1) and (self.live_troops == set()) :
            return -1
        
        if (self.live_builds == set()) :
            return 1
            
        print(Style.BRIGHT)
        self.update(input)
        
        os.system('clear')
        
        terminal_sz = os.get_terminal_size()
        print(' ' * (44 + (terminal_sz.columns - 100) // 2 - 1), 'Terminal CoC', ' ' * 44)
        for i in self.map :
            row = []
            for j in i :
                if(len(j) != 2) :
                    print(j, ":  ", len(j))
                    print(row)
                row.append(Back.BLACK + self.set_color(j[0]) + j[1] + Back.RESET + Fore.RESET)
            
            print(' ' * ((terminal_sz.columns - 100) // 2 - 1), ''.join(row))
        
        
        
        if not (self.king is None) :  
            print('\n', ' ' * ((terminal_sz.columns - 100) // 2 - 1) + "  King Health :  " + self.hp_bar())
            
        print('\n' + ' ' * ((terminal_sz.columns - 100) // 2) + "Toggle SpawnPoints: j, k, l")
        print(' ' * ((terminal_sz.columns - 100) // 2) + "Spawn King: v \t\t Spawn Barbarian: b")
        print(' ' * ((terminal_sz.columns - 100) // 2) + "Move King: w, a, s, d")
        print(' ' * ((terminal_sz.columns - 100) // 2) + "King Normal Attack: <space> \t\t Leviathan Attack: x")
        print(' ' * ((terminal_sz.columns - 100) // 2) + "Healing Spell: h")
        # print(self.buildings)
        return 2

    
    
    def place(self, building, position) :
        if (isinstance(building, bldg.Building)) :
            self.buildings[building] = position
            if not (isinstance(building, bldg.Wall) or isinstance(building, bldg.SpawnPoint)) :
                self.live_builds.add(building)
            
        
        if isinstance(building, troops.Troops) :
            self.troops[building] = position
            self.live_troops.add(building)
            self.deployed = 1
            
        
        for i in range(building.dim[0]) :
            for j in range(building.dim[1]) :
                self.map[position[0]+i][position[1]+j] = building.art[i][j]
     
     
                
    
    def heal(self) :
        for troop, pos in self.troops.items() :
            troop.hp = min(troop.hp * 1.5, troop.max_hp)   
            
            
    def rage(self)   :
        pass
                
    
    def update(self, input) :
        
        # if not self.troops : return -1
        
        # if not self.buildings : return 1
        
        if input == 'j' :
            self.active_spawn_point = self.spawn_pts['J']
        
        
        if input == 'k' :
            self.active_spawn_point = self.spawn_pts['K']
        
        
        if input == 'l' :
            self.active_spawn_point = self.spawn_pts['L']
        
        
        if input == 'b' :
            if (self.barb_count < self.max_barb_count) :
                                
                self.place(troops.Barbarian(self.active_spawn_point.art), self.buildings[self.active_spawn_point])
                self.barb_count += 1
        
        
        if input == 'v' :
            if (self.king_count < 1) :
                                
                self.king = troops.King(self.active_spawn_point.art)
                self.place(self.king, self.buildings[self.active_spawn_point])
                self.king_count += 1
        
        if input == 'h' :
            self.heal()
            
            
        if input == 'r' :
            self.rage()
        
        for troop, position in self.troops.items() :
            # if(troop.hp <= 0) :
            #     del self.troops[troop]
                
            troop.move(position, self, input)
            
        for building, position in self.buildings.items() :
            
            if (isinstance(building, bldg.SpawnPoint)) : continue
            
            # if building.hp <= 0 : 
            #     del self.buildings[building]
            
            if isinstance(building, bldg.Cannon) :
                building.attack(self.buildings[building], self)
                
        return 0