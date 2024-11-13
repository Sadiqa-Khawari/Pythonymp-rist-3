# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTA (MainWindow.py)
# ==================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow

# Määritellän luokka joka perii QMainWindow- jaUi_
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application."""
    def __init__(self, arg):
        super().__init__()
    

    