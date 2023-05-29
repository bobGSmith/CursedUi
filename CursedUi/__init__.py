"""CursedUi

A python library for developing command line interfaces using curses. 
It includes various input objects (text input, select from list, button, menu etc...).
"""

from .SelectMenu import SelectMenu 
from .Button import Button 
from .InputText import InputText
from .SelectItem import SelectItem
from .create_window import create_window
from .add_newlines import add_newlines
from .get_lines_or_cols import get_lines_or_cols
from .help_string import help_string
from .setup_terminal import setup_terminal
from .CursedWindow import CursedWindow


__version__ = "1.0.0"
__author__ = 'Bob G Smith'