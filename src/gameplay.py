import village
import troops
import gvars
import get
import buildings
import sys,tty,termios
import time

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
        while(True) :
            # print(time.time() - self.last_refresh_time)
            k = get.input_to(self.getch, timeout=0.5)
            
            if k == 'q' :
                return self.events
            # while(time.time() - self.last_refresh_time < 0.33) :
            #     print(time.time() - self.last_refresh_time)
            #     k = get.input_to(self.getch)
            #     self.last_input = k 
                # if ord(k) == 3 :
                #     return
        
    
            self.frame_count += 1
            # self.last_refresh_time = time.time()
            
            
            # print(self.frame_count, ': ', k)
            self.village.render()
        
    
class Event :
    pass


def main() :
    # my_village = village.Village()
    # my_village.render()
    game = Gameplay()
    game_log = game()

if __name__ == '__main__' :
    main()
    