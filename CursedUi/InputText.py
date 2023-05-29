import curses
import string

class InputText () : 
    def __init__ (self,containerScr, label,y,x,width,id,shift = 2,selected_attr=curses.A_BOLD ,default_value = "type here",hide_input = False,mask = "*",
            hint = "Text: type or paste input, hit LEFT when done!",
            hint_box = None, parent_menu = None,label_width = 8,
            basic_text_only = True
        ) : 
        self.containerScr = containerScr
        self.label = label
        self.id = id 
        self.x = x 
        self.y = y
        self.width = width 
        self.label_width = label_width
        self.input_width = self.width - (len(label)+3)
        self.shift = shift 
        self.selected_attr = selected_attr 
        self.attr = curses.A_NORMAL
        self.default_value = default_value
        self.window = containerScr.subwin(0,width,self.y,self.x+shift)
        self.value = self.default_value
        self.truncated_value = self.getTruncatedValue()
        self.hide_input = hide_input 
        self.mask = mask
        self.hint = hint 
        self.hint_box = hint_box 
        self.parent_menu = parent_menu
        self.active = False 
        self.basic_text_only = basic_text_only
        self.build()
    def build(self): 
        self.window.clear()
        if self.value == self.default_value: 
            self.window.addstr(0,0,f"{self.label:{self.label_width}} : {self.getTruncatedValue():{self.input_width}}",self.attr)
        else: 
            self.window.addstr(0,0,f"{self.label:{self.label_width}} : {self.mask * len(self.getTruncatedValue()) if self.hide_input else self.getTruncatedValue():{self.input_width}}",self.attr)
        self.window.refresh() 
    def get_choice(self, key):
        if self.active:
            if key == 8:
                if len(self.value) > 0: 
                    self.value = self.value[0:len(self.value)-1]
                    self.build()
            else: 
                if self.basic_text_only:
                    if chr(key) in string.printable:
                        self.value += chr(key)
                else: self.value += chr(key)
            self.build()
    def activate (self):
        self.active = True 
        self.attr = self.selected_attr
        if self.value == self.default_value:
            self.value = ""
        self.build() 
        if self.hint_box != None: 
            self.hint_box.clear() 
            self.hint_box.addstr(0,1,self.hint)
            self.hint_box.refresh()
    def deactivate (self):
        self.active = False 
        self.attr = curses.A_NORMAL
        self.build()
        if self.parent_menu != None: 
            self.parent_menu.activate() 
    def returnChoice (self):
        return self.value
    def getTruncatedValue(self): 
        
        if len(self.value) < self.input_width:
            return self.value
        else:
            return f"..{self.value[(len(self.value)-self.input_width) +2:]}" 