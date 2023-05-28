import curses 

def setup_terminal (min_h = 22, min_w = 60, fixed_size = False):
    curses.curs_set(False)
    curses.cbreak()
    curses.noecho()
    if fixed_size: 
        H,W = min_h,min_w
    else: 
        W = min_w if curses.COLS < min_w else curses.COLS
        H  = min_h if curses.LINES < min_h else curses.LINES
    curses.resize_term(H,W)
    scr = curses.newwin(curses.LINES-1,curses.COLS-1,0,0)
    scr.keypad(True)
    return scr 