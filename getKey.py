import curses 

class CharDisplay () : 
    def __init__(self,containerScr,y,x,height,width):
        self.containerScr = containerScr
        self.x=x
        self.y=y
        self.height=height
        self.width = width
        self.window = containerScr.subwin(y+height,x+width,y,x)
        self.window.box()
        self.cur_key = None 
    def displayChar (self,key):
        self.window.clear()
        self.window.addstr(2,2,f"{chr(key)} = {str(key)}")
        self.cur_key = key
        self.window.box()
        self.window.refresh() 


def main (stdscr) : 
    #curses.cbreak() 
    curses.curs_set(False)
    curses.noecho()
    scr = curses.newwin(curses.LINES-1,curses.COLS-1,0,0) 
    scr.keypad(True)
    chrBox = CharDisplay(scr,2,2,3,12) 
    scr.addstr(1,2,"Press any key to see its number code:")
    scr.addstr(7,2,"Hit Esc twice to quit")
    done = False 
    while not done:
        key = scr.getch()
        if chrBox.cur_key == 27 and key == 27: 
            done = True 
            break
        else:            
            chrBox.displayChar(key)

if __name__ == "__main__":
    curses.wrapper(main)