import curses

class Button () : 
    def __init__(
        self,containerScr,inactive_label,active_label,clicked_label,
        y,x,id,onClick=None,shift = 2,reset_click_on_deactivate = True,
        selected_attr = curses.A_STANDOUT,parent_menu = None,
        onclick_finished_label = "done",hint_box = None,
        hint="Button: Hit Enter to click, left arrow to deselect"):
        self.containerScr = containerScr 
        self.inactive_label = inactive_label
        self.active_label = active_label 
        self.clicked_label = clicked_label 
        self.parent_menu = parent_menu
        self.reset_click_on_deactivate = reset_click_on_deactivate
        self.x = x
        self.y = y
        self.id = id
        self.shift = shift
        self.onClick = onClick
        self.width = max(len(self.inactive_label),len(self.active_label),len(self.clicked_label),len(onclick_finished_label)) + 4
        self.active = False 
        self.clicked = False
        self.attr = curses.A_NORMAL
        self.selected_attr = selected_attr
        self.window = containerScr.subwin(0,self.width, self.y, self.x + shift)
        self.hint = hint 
        self.hint_box = hint_box 
        self.onclick_finished_label = onclick_finished_label
        self.onclick_finished = False
        self.build()
        self.window.box()
    def build (self):
        self.window.clear()
        if self.onclick_finished: 
            self.window.addstr(0,0,f"[ {self.onclick_finished_label:{self.width - 4}} ]",self.attr)
        elif self.clicked: 
            self.window.addstr(0,0,f"[ {self.clicked_label:{self.width - 4}} ]",self.attr)
        else: 
            self.window.addstr(0,0,f"[ {self.active_label if self.active else self.inactive_label:{self.width - 4}} ]",self.attr)
        self.window.refresh()
    def activate(self):
        self.active = True 
        self.attr = self.selected_attr
        self.build()
        if self.hint_box != None:
            self.hint_box.clear()
            self.hint_box.addstr(0,1,self.hint)
            self.hint_box.refresh()
    def deactivate(self):
        self.active = False 
        self.onclick_finished = False
        if self.reset_click_on_deactivate:
            self.clicked = False 
        self.attr = curses.A_NORMAL
        self.build()
        if self.parent_menu != None: 
            self.parent_menu.activate() 
    def get_choice(self, key):
        if self.active and not self.clicked:
            if key == 10:
                self.clicked = True
                self.build()
                self.onClick()
    def returnChoice(self):
        return self.clicked
