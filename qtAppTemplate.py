# MALLIPOHJA QT-SOVELLUSTEN RAKENTAMISEEN PySide6-KIRJASTON AVALLA
# ================================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Järjestelmäkomentojen kirjasto
import sys

# Pyside-kirjastot
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication # Käyttöliittymän elementit (kaikki), korvaa listalla
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# LUOKKAMÄÄRITYKSET
# -----------------

# Pääikkunan luokka, joka perii QMainWindow-luokan
class MainWindow(QMainWindow):

    # Konstruktori
    def __init__(self):
        super().__init__(self)

        # Louodaan käyttöliittymän lataaja
        windowLoader = QUiLoader()

        # Annetaan sille käyttöliittymätiedosto 
        
        window = windowLoader.load("mainWindow.ui", None)
        window.show()
        self.setWindowTitle("Hippoptamus")
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    
    sys.exit(application.exec())