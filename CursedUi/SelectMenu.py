import curses

class SelectMenu () : 
    def __init__(self,containerScr,item_selectors,selected = ">", deselected = "-"):
        self.item_selectors = item_selectors
        self.active_selector = False 
        self.selection = 0 
        self.selected = selected
        self.deselected = deselected 
        self.containerScr = containerScr
        self.display()
    def get_choice (self,key):
        if self.active_selector:
            if key == curses.KEY_LEFT:
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
                self.active_selector = True 
                self.item_selectors[self.selection].activate()
                self.refreshAll()
            self.display() 
    def display(self):
        for i in range(len(self.item_selectors)):
            if i == self.selection: 
                self.containerScr.addstr(self.item_selectors[i].y,self.item_selectors[i].x,self.selected)
                self.containerScr.refresh()
            else: 
                self.containerScr.addstr(self.item_selectors[i].y,self.item_selectors[i].x,self.deselected)
                self.containerScr.refresh()
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
     