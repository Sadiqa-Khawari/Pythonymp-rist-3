# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# ================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
 # --------------------------------


import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

# LUOKKAMÄÄRITYKSET
# -----------------

# Luodaan käyttöliittymätiedoston lataajaobjekti QUiLoader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perustella, pääikkunalla ei ole isäntäobjekti
window = loader.load("mainWindow.ui", None)

# Asetstaan pääikkunan nimi
window.setWindowTitle("TÄMÄ ON PÄÄIKKUNA")
label = window.findChild(QtWidgets.QLabel, "label")

statusBar = window.findChild(QtWidgets.QStatusBar, "statusbar")
if statusBar != None:
    statusBar.showMessage("Kaikki hyvin", -1)

if label != None:
    label.setText("Muutettu teksiä")

else:
    if statusBar != None:
        statusBar.showMessage("Pieleen meni!", 5000)

# Määritellään ikkuna näyväksi
window.show()


app.exec()