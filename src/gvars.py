import sys,tty,termios


spawn_point_art = {'J': '🅙 ',
                    'K': '🅚 ',
                    'L': '🅛 '}

spawn_point_loc = {'J': (40, 40),
                    'K': (5, 36),
                    'L': (45, 6)}


class Getch:       
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch