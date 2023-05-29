from .add_newlines import add_newlines
from .get_lines_or_cols import get_lines_or_cols
from .help_string import help_string
from .CursedWindow import CursedWindow


def create_window (containerScr,h,w,y,x,title="Display",display_default = False, box = True, default_string = help_string):
    '''deprecated: better to just use Window object directly'''
    new_win = CursedWindow(containerScr,h,w,y,x,title,display_default=display_default,box=box,default_string=default_string)
    return new_win

