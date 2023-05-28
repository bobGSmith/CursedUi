from .utils import help_string, add_newlines, get_lines_or_cols
import curses
def create_window (containerScr,h,w,y,x,title="Display",display_default = False, box = True, default_string = help_string):
    new_win = containerScr.subwin(h,w,y,x)

    if display_default:
        new_win.addstr(2,0,add_newlines(
            default_string,
            get_lines_or_cols(new_win,"col")-3,
            indent="  ~ ",
            startIndent = True))
    if box: new_win.box()
    new_win.addstr(0,2,title,curses.A_BOLD)
    new_win.refresh() 
    return new_win