# import numpy
# import colorama
import sys

sys.path.append('./src/')
import village 
import gameplay



def main() :
    my_village = village.Village()
    my_village.render()
    # game = gameplay.Gameplay()
    # game.start_game()

if __name__ == '__main__' :
    main()
    