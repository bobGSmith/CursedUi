"""CursedUi

A python library for developing command line interfaces using curses. 
It includes various input objects (text input, select from list, button, menu etc...).
"""

from .SelectMenu import SelectMenu 
from .Button import Button 
from .InputText import InputText
from .SelectItem import SelectItem
from .create_window import create_window
from .utils import *



__version__ = "1.0.0"
__author__ = 'Bob G Smith'