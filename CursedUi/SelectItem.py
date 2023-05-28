import curses 

class SelectItem () :
    def __init__ (self,containerScr,label,items,y,x,id,label_width=8,item_width=8,shift=2,selected_attr = curses.A_BOLD):
        self.label = label
        self.items = items 
        self.y = y 
        self.x = x
        self.id = id
        self.width = label_width + item_width + 2
        self.label_width = label_width 
        self.item_width = item_width
        self.window = containerScr.subwin(0, self.width, self.y, self.x + shift)
        self.selection = 0
        self.active = False
        self.attr = curses.A_NORMAL
        self.selected_attr = selected_attr
        self.build()
    def build (self):  
        self.window.clear() 
        self.window.addstr(0,0,f"{self.label:<{self.label_width}} : {self.items[self.selection]:<{self.item_width}}",self.attr)
        self.window.refresh()
    def get_choice(self, key):
        if self.active: 
            if key == curses.KEY_UP:
                self._next()
            if key == curses.KEY_DOWN:
                self._previous()
    def _next (self): 
        self.selection = (self.selection + 1) % len(self.items) 
        self.build()
    def _previous (self): 
        self.selection -= 1
        if self.selection < 0: self.selection = len(self.items) - 1
        self.build()
    def activate (self):
        self.active = True
        self.attr = self.selected_attr
        self.build()
    def deactivate(self):
        self.active = False 
        self.attr = curses.A_NORMAL
        self.build()
    def returnChoice(self):
        return self.items[self.selection]