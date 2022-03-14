import sys,tty,termios
import time
import gameplay

class _Getch:       
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get(inkey):
    
    while(1):
            k=inkey()
            if k!='': break
    print (time.time(), ': ', ord(k), ': ', k)

def main():
    inkey = _Getch()
    for i in range(0,25):
        get(inkey)

if __name__=='__main__':
    main()