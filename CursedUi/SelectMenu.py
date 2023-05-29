import curses

class SelectMenu () : 
    def __init__(self,containerScr,item_selectors,selected = ">", deselected = "-",active_attr = curses.A_BOLD,activate=True,
        hint = "Menu: Q=Quit, UP/DOWN=navigate, LEFT/RIGHT=select/deselect", hint_box = None,id = ""):
        self.item_selectors = item_selectors
        self.id = id
        self.active_selector = False 
        self.selection = 0 
        self.selected = selected
        self.deselected = deselected 
        self.containerScr = containerScr
        self.attr = active_attr if activate else curses.A_NORMAL
        self.active = activate 
        self.active_attr = active_attr
        self.hint = hint 
        self.hint_box = hint_box
        self.display()
        if activate: self.activate()
    def get_choice (self,key):
        if self.active_selector:
            if key == curses.KEY_LEFT:
                self.deactivate() 
                self.active_selector = False 
                self.item_selectors[self.selection].deactivate()
                self.display()
                self.refreshAll()
            else: 
                self.item_selectors[self.selection].get_choice(key)
                self.refreshAll()
        else:
            if key == curses.KEY_DOWN:
                self.selection = (self.selection + 1) % len(self.item_selectors)
            if key == curses.KEY_UP:
                self.selection -= 1
                if self.selection < 0: self.selection = len(self.item_selectors) - 1
            if key == curses.KEY_RIGHT:
                self.activate() 
                self.active_selector = True 
                self.item_selectors[self.selection].activate()
                self.refreshAll()
            self.display() 
    def display(self):
        for i in range(len(self.item_selectors)):
            if i == self.selection: 
                self.containerScr.addstr(self.item_selectors[i].y,self.item_selectors[i].x,self.selected,self.attr)
                self.containerScr.refresh()
            else: 
                self.containerScr.addstr(self.item_selectors[i].y,self.item_selectors[i].x,self.deselected,self.attr)
                self.containerScr.refresh()
        self.refreshAll()
    def refreshAll(self):
        for selector in self.item_selectors:
            selector.build()
    def returnChoicesObject (self):
        choices = {}
        for i in range(len(self.item_selectors)):
            choices[self.item_selectors[i].id] = self.item_selectors[i].returnChoice()
        return choices
    def add_items (self,items):
        for item in items:
            self.item_selectors.append(item)
        self.refreshAll()
        self.display()
    def remove_items(self,item_ids):
        self.display_blank()
        new_item_list = []
        for i in range(len(self.item_selectors)):
            if self.item_selectors[i].id in item_ids:
                self.item_selectors[i].window.clear()
                self.item_selectors[i].window.refresh()
            else: 
                new_item_list.append(self.item_selectors[i])
        self.item_selectors = new_item_list
        self.selection = 0
        self.activate()
        self.active_selector = False
        self.display()
    def display_blank(self):
        for i in range(len(self.item_selectors)):
                self.containerScr.addstr(self.item_selectors[i].y,self.item_selectors[i].x," ",self.attr)
                self.containerScr.refresh()
        self.refreshAll()
    def activate(self): 
        self.active = True 
        self.attr = self.active_selector
        if self.hint_box != None: 
            self.hint_box.clear()
            self.hint_box.addstr(0,1,self.hint)
            self.hint_box.refresh()
        self.display()
    def deactivate(self):
        self.active = False 
        self.attr = curses.A_NORMAL
        self.display() 
    def getItemById(self,id): 
        for i in range(len(self.item_selectors)):
            if id == self.item_selectors[i].id:
                return self.item_selectors[i]
    