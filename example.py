import curses
from CursedUi import *

def get_lines_or_cols (scr,line_or_col = "line"):
    lines, cols = scr.getmaxyx() 
    if line_or_col == "line":
        return lines 
    if line_or_col == "col":
        return cols

def add_newlines (string, nth = 10, indent = " ", startIndent=False ):
    new_str = newstr = indent if startIndent else ""
    prev_len = 0
    for i, w in enumerate(string.split(" ")): 
        cur_len = len(w) + 1
        if prev_len + cur_len > nth - len(indent) - 4: 
            new_str += f"\n{indent}{w}"
            prev_len = 0
        else: 
            prev_len += cur_len
            new_str += w if len(new_str) == 0 or new_str == indent else f" {w}"
            if "\n" in w:
                prev_len = len(w.split("\n"))[-1]
    return new_str

def add_newlines (string, nth = 10, indent = " ", startIndent=False,newline="\n"):
    new_str = newstr = indent if startIndent else ""
    prev_len = 0
    for i, w in enumerate(string.split(" ")): 
        cur_len = len(w) + 1
        if prev_len + cur_len > nth - len(indent) - 4: 
            new_str += f"\n{indent}"
            prev_len = 0
        if "\n" in w:
            prev_len = len(w.split("\n")[-1])
            new_str += f" {w.split(newline)[0]}"
            new_str += f"\n{indent}"
            new_str += w.split("\n")[-1]
        else: 
            new_str += w if prev_len == 0  else f" {w}"
            prev_len += cur_len

    return new_str

def submit_onClick (scr,parent_menu):
    def submit ():
        choices = parent_menu.returnChoicesObject() 
        width = get_lines_or_cols(scr,"col")
        string = f'Why not take a trip to {choices["holiday_choice"]} with your {choices["pet_choice"]} {choices["pet_name"]} and have a {choices["food_choice"]}!'
        string = add_newlines(string,width - 2, indent = "~ ", startIndent = True)
        scr.clear()
        scr.addstr(1,0,string)
        scr.refresh() 
    return submit           

def main (stdscr): 
    curses.curs_set(False)
    curses.cbreak()
    curses.noecho()

    W = 60 if curses.COLS < 60 else curses.COLS
    H  = 22 if curses.LINES < 22 else curses.LINES
    curses.resize_term(H,W)

    scr = curses.newwin(curses.LINES-1,curses.COLS-1,0,0)
    scr.keypad(True)

    menu_area = scr.subwin(9,curses.COLS-2,0,1)
    menu_area.box()
    menu_area.addstr(1,2,"Favourite Things")
    disp_area = scr.subwin(10,curses.COLS-2,9,1)
    disp_area.addstr(0,1,"Display",curses.A_UNDERLINE)
    disp_area.addstr(2,0,add_newlines("Welcome to CursedUi builder demo! \nUse arrow keys to navigate the input menu. Right arrow activates item, Left deactivates. Up Down scrolls through items and selected item options, hit return to 'click' buttons. For text input fields you can type or paste.",get_lines_or_cols(scr,"col")-2,indent="~ ",startIndent = True))
    mainMenu = SelectMenu(
        menu_area,
        []
    )
    mainMenu.add_items([
        SelectItem(menu_area,"Pet",["dog", "cat" ,"fish"],2,2,"pet_choice"),
        InputText(menu_area,"Pet Name",3,2,40,"pet_name"),
        SelectItem(menu_area,"Food",["pizza","burger","pasta"],4,2,"food_choice"),
        SelectItem(menu_area,"Holiday",["spain","italy","france"],5,2,"holiday_choice"),
        Button(menu_area,"SUBMIT","RETURN","DONE",6,2,"submit_button",submit_onClick(disp_area,mainMenu))
    ])
    stdscr.addstr(curses.LINES-1,0,"| Hit Q to quit | Use arrow keys |") 
    stdscr.refresh()
    done = False 
    while not done: 
        key = scr.getch()
        
        if key != curses.ERR:
            if chr(key) in ["q","Q"]:
                done = True
            mainMenu.get_choice(key)
        #scr.addstr(10,10,str(key))
        
if __name__ == "__main__":
    curses.wrapper(main)   