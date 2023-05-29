import curses 
from .help_string import help_string
from .add_newlines import add_newlines
from .get_lines_or_cols import get_lines_or_cols

class CursedWindow () : 
    def __init__ (
        self, containerScr,
        h, w, y, x, title="",
        display_default=False,
        box = True,
        default_string = help_string,
        active_title = curses.A_REVERSE,
        active_at_start = True,
        onbuild = None,
        id = ""
    ):
        self.containerScr = containerScr
        self.h = h 
        self.w = w
        self.y = y
        self.x = x 
        self.title = title
        self.has_box = box 
        self.elements = []
        self.active = active_at_start
        self.active_title = curses.A_BOLD
        self.default_string = default_string
        self.window = self.containerScr.subwin(self.h,self.w,self.y,self.x)
        self.elements_dict = {} 
        self.onbuild = onbuild
        self.display_default = display_default
        self.id = id
        if self.display_default:
            self.window.addstr(2,0,add_newlines(
                default_string,
                get_lines_or_cols(self.window,"col")-3,
                indent="  ~ ",
                startIndent = True))
        self.build()
    def refresh(self): 
        self.window.refresh() 
    def clear(self):
        self.window.clear() 
    def addstr(self,y,x,string,attr=curses.A_NORMAL):
        self.window.addstr(y,x,string,attr)
    def subwin(self,h,w,y,x):
        new_window = self.window.subwin(h,w,y,x)
        return new_window
    def getmaxyx (self): 
        return self.window.getmaxyx() 
    def box (self): 
        self.window.box()
    def activate(self): 
        self.active = True 
        self.build() 
    def deactivate(self):
        self.active = False 
        self.build() 
    def build (self) :
        if self.has_box: self.box()
        if self.title != "": self.window.addstr(
            0,2,self.title,
            self.active_title if self.active else curses.A_NORMAL
        )
        if self.onbuild != None: self.onbuild() 
        self.window.refresh() 
    def buildAllElements (self) :
        for el in self.elements:
            el.build()  
    def add_element(self,element):
        self.elements.append(element)
        self.elements_dict[element.id] = element
    def getElementById (self,id):
        return self.elements_dict[id]
        
    
    
        
            
        