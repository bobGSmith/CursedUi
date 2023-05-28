import curses
class InputText () : 
    def __init__ (self,containerScr, label,y,x,width,id,shift = 2,selected_attr=curses.A_BOLD ,default_value = "type here",hide_input = False,mask = "*") : 
        self.containerScr = containerScr
        self.label = label
        self.id = id 
        self.x = x 
        self.y = y
        self.width = width 
        self.shift = shift 
        self.selected_attr = selected_attr 
        self.attr = curses.A_NORMAL
        self.default_value = default_value
        self.window = containerScr.subwin(0,width,self.y,self.x+shift)
        self.value = self.default_value
        self.hide_input = hide_input 
        self.mask = mask
        self.active = False 
        self.build()
    def build(self): 
        self.window.clear()
        if self.value == self.default_value: 
            self.window.addstr(0,0,f"{self.label:8} : {self.value:30}",self.attr)
        else: 
            self.window.addstr(0,0,f"{self.label:8} : {self.mask * len(self.value) if self.hide_input else self.value:30}",self.attr)
        self.window.refresh() 
    def get_choice(self, key):
        if self.active:
            if key == 8:
                if len(self.value) > 0: 
                    self.value = self.value[0:len(self.value)-1]
                    self.build()
            else: 
                self.value += chr(key)
            self.build()
    def activate (self):
        self.active = True 
        self.attr = self.selected_attr
        if self.value == self.default_value:
            self.value = ""
        self.build() 
    def deactivate (self):
        self.active = False 
        self.attr = curses.A_NORMAL
        self.build()
    def returnChoice (self):
        return self.value