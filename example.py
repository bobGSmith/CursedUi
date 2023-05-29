import curses
from CursedUi import *


# Custom onClick function for submit button
def submit_onClick (scr,parent_menu):
    def submit ():
        choices = parent_menu.returnChoicesObject() 
        width = get_lines_or_cols(scr,"col")
        string = f'Why not take a trip to {choices["holiday_choice"]} with your {choices["pet_choice"]} {choices["pet_name"]} and have a {choices["food_choice"]}!'
        string = add_newlines(string,width - 2, indent = "  ~ ", startIndent = True)
        scr.clear()
        scr.addstr(2,0,string)
        scr.box()
        scr.addstr(0,2,"Display Area")
        scr.refresh() 
    return submit           


def main (stdscr): 

    scr = setup_terminal (19,70)

    # Create menu area and display area
    #menu_area = create_window(scr,9,get_lines_or_cols(scr,"col")-1,0,1,title="Favourite things",display_default=False,box=True)
    menu_area = CursedWindow(scr,9,get_lines_or_cols(scr,"col")-1,0,1,title="Favourite things",display_default=False,box=True,id="menu_area")
    disp_area = CursedWindow(scr,8,get_lines_or_cols(scr,"col")-1,9,1,"Display Area",True,True,id ="disp_area")
    hint_box = CursedWindow(scr,1,get_lines_or_cols(scr,"col")-1,17,1,"",False,False,id="hint_box")

    mainMenu = SelectMenu(menu_area,[],hint_box = hint_box,id="main_menu")
    menu_area.add_element(mainMenu)
    
    mainMenu.add_items([
        SelectItem(menu_area,"Pet",["dog", "cat" ,"fish"],2,2,"pet_choice",hint_box = hint_box,parent_menu=mainMenu),
        InputText(menu_area,"Pet Name",3,2,40,"pet_name",hint_box = hint_box, parent_menu = mainMenu),
        SelectItem(menu_area,"Food",["pizza","burger","pasta"],4,2,"food_choice",hint_box = hint_box,parent_menu=mainMenu),
        SelectItem(menu_area,"Holiday",["spain","italy","france"],5,2,"holiday_choice",hint_box = hint_box,parent_menu=mainMenu),
        Button(menu_area,"SUBMIT","HIT IT!","DONE",6,2,"submit_button",submit_onClick(disp_area,mainMenu),hint_box=hint_box,parent_menu=mainMenu)
    ])
    


   # hint_box.addstr(0,1," Q=Quit, UP/DOWN=navigate, LEFT/RIGHT=select/deselect") 
    
    done = False 
    while not done: 
        key = scr.getch()
        
        if key != curses.ERR :
            if chr(key) in ["q","Q"] and not mainMenu.active_selector:
                done = True
            mainMenu.get_choice(key)
        #scr.addstr(10,10,str(key))
        
if __name__ == "__main__":
    curses.wrapper(main)   