import village
import troops
import gvars
import get
import buildings
import sys,tty,termios
import time
import pickle

class Gameplay :
    
    def __init__(self) :
        self.start_time = 0
        self.last_refresh_time = 0
        self.frame_count = 0
        self.events = {}
        self.village = village.Village()
        self.getch = get.Get()
        self.last_input = ''
    
        
    def __call__(self) :
        self.start_time = time.time()
        self.last_refresh_time = self.start_time
        res = -2
        
        while(True) :
            # print(time.time() - self.last_refresh_time)
            
            k = get.input_to(self.getch, timeout=0.2)
            
         
            
            if k == 'q' :
                res = 0
                break
            # while(time.time() - self.last_refresh_time < 0.33) :
            #     print(time.time() - self.last_refresh_time)
            #     k = get.input_to(self.getch)
            #     self.last_input = k 
                # if ord(k) == 3 :
                #     return
        
    
            self.frame_count += 1
            # self.last_refresh_time = time.time()
            
            
            # print(self.frame_count, ': ', k)
            if k is not None :
                self.events[self.frame_count] = k
            
            res = self.village.render(k)
            
            if (res in [0, -1, 1]) :
                break
        
        
        return [res, self.events]
            
        
        
        



def main() :
    # my_village = village.Village()
    # my_village.render()
    game = Gameplay()
    game_log = game()
    print(game_log)

if __name__ == '__main__' :
    main()
    