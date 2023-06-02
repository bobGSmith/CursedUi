import curses 

class SelectItem () :
    def __init__ (self,containerScr,label,items,y,x,id,label_width=8,item_width=8,shift=2,selected_attr = curses.A_BOLD,
                  hint = "Select: use UP/DOWN to scroll items, hit LEFT when done",
                  hint_box = None, parent_menu = None):
        self.label = label
        self.items = items 
        self.y = y 
        self.x = x
        self.id = id
        self.hint = hint 
        self.hint_box = hint_box
        self.parent_menu = parent_menu
        self.width = label_width + item_width + 2
        self.label_width = label_width 
        self.item_width = item_width
        self.index = 0
        self.window = containerScr.subwin(0, self.width, self.y, self.x + shift)
        self.selection = 0
        self.active = False
        self.attr = curses.A_NORMAL
        self.selected_attr = selected_attr
        self.build()
    def build (self):  
        self.window.clear() 
        self.window.addstr(0,0,f"{self.label:<{self.label_width}} : {self.getTruncatedValue(self.items[self.selection],self.index):<{self.item_width}}",self.attr)
        self.window.refresh()
    def get_choice(self, key):
        if self.active: 
            if key == curses.KEY_UP:
                self._next()
            if key == curses.KEY_DOWN:
                self._previous()
            if key == curses.KEY_RIGHT:
                self.index += 1 
                self.build()
    def _next (self): 
        self.selection = (self.selection + 1) % len(self.items) 
        self.index = 0
        self.build()
    def _previous (self): 
        self.selection -= 1
        if self.selection < 0: self.selection = len(self.items) - 1
        self.index = 0
        self.build()
    def activate (self):
        self.active = True
        self.attr = self.selected_attr
        self.index = 0
        self.build()
        if self.hint_box != None: 
            self.hint_box.clear() 
            self.hint_box.addstr(0,1,self.hint)
            self.hint_box.refresh() 
    def deactivate(self):
        self.active = False 
        self.attr = curses.A_NORMAL
        if self.parent_menu != None: 
            self.parent_menu.activate() 
        self.build()
    def returnChoice(self):
        return self.items[self.selection]
    def getTruncatedValue (self,index=0,trailing_start="",trailing_end = ".."):
        value = self.items[self.selection]
        i = index % len(value)
        if len(value) < self.item_width: 
            return value 
        else: 
            truncated = f"{value[i:(i+(self.item_width) if len(value) - i > self.item_width else None)]}"
            if len(truncated) < self.item_width:
                return getTruncatedValue(f"{truncated} {value}",self.item_width)
            else:
                return f"{trailing_start}{truncated[len(trailing_start):-len(trailing_end)]}{trailing_end}"