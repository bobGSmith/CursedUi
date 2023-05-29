# Curses UI 

This package contains functions and classes that help one to build a commandline user interface using curses. This includes menus, textboxes, input boxes etc..

## Install 
To install the package, navigate to the main directory containing the setup.py file and run: 

```
pip install . 
```

## Contents 
The package comes with a set of importable objects: 
* Button - A "clickable" button that executes arbitrary onClick logic 
* InputText - A text input field where the user can type or paste, for password inputs you can mask the input with "*" or other symbol.
* SelectItem - Similar to a drop down menu, user can select from list of options using up and down arrow. 
* SelectMenu - This takes an array of the objects described, displays them, and allows the user to scroll through, activate, and deactivate them. 

## Scrips
* example.py - a demo of a app created with CursedUi
* getKey.py - a tool for checking the number assocated with each key 

## Example 
For example code see `example.py`

### Example screenshot 

```
 ┌────────────────────────────────────────────────────────────┐  
 │ Favourite Things                                           │  
 │ >Pet      : dog                                            │  
 │ -Pet Name : type here                                      │  
 │ -Food     : pizza                                          │  
 │ -Holiday  : spain                                          │  
 │ -[ SUBMIT ]                                                │  
 │                                                            │  
 └────────────────────────────────────────────────────────────┘  
 Display                                                         
 ~ Welcome to CursedUi builder demo!                             
 ~ Use arrow keys to navigate the input menu. Right arrow        
 ~ activates item, Left deactivates. Up Down scrolls through     
 ~ items and selected item options, hit return to 'click'        
 ~ buttons. For text input fields you can type or paste.         
                                                                 
 | Hit Q to quit | Use arrow keys |                              
```

## Dev to do
### Setup App 
Possobly turn the main function in the `example.py` script into an App object where you can build the app by adding input fields and display fields etc. Probs not worth it. Alternatively create a setup_terminal function to put in your main file with all the options (display areas, minimum height/width etc)

### Mouse click 
Possibly enable mouse clickc to activate input fields trigger onClick events for `Buttons`. 

### Allow multiple SelectMenu 
Either make select menu that can take an array of select Menus (which would allow arbitrary depth of nesting) or possibly just make it possible to add more than one SelectMenu to the Main / App area and have a way of selecting from that (probably a less good solution).

### Add Utils 
Make a utils module with all the helper functions like add_newlines etc. 

### Display Text Box 
Make a window object for displaying text where when it overflows it truncates the displayed text to fit and allows scrolling up and down to display the rest. 

pos make create_window into a class Window

### Remove items 
add a remove items from menu option that refreshes the display and removes based on id. useful for conditionally rendering items 

### Select item scrolling text 
if item text does not fit in item display box. allow user to scroll through the text with right arrow 

 

