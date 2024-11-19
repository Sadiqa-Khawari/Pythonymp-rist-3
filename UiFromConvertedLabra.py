# LABRATORIOETIKETTISOVELLUKSEN PÄÄIKKUNAN
# LUOMINEN Labra_ui.py TIEDOSTAN PERUSTELLA
# =========================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet
from Labra_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

import identityCheck2 # Henkilötunnuksen tarkistukseen liityvät luokka
import barcode  # Viivakoodin muodostukseen tarvittavat rutiinit
from avtools import sound # Äänitoiminnot

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

         # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        #  Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDOUT SIGNAALIT
        # ----------------------

        # Kun poistutaan ssnLine Edit-elementistä suoritetaan barcodeLable-eleminted
        self.ui.ssnLineEdit.textEdited.connect(self.updateBarcodeLabel)

      
    # OHJELMOIDUT SLOTIT   
    # ------------------

    # Vivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        # Jos se on oikein, luodaan viivakoodi
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistussumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän  

        
        # jos se muostettu väärin näytetaan virheilmotus MessageBox-ikkunassa

        self.errorTitle = "Henkilötunnus virheellinen"
        self.errorText = "Syöttämässäsi henkilötunnuksessa on virhe"
        self.openErrorMsgBox(self.errorTitle, self.errorText)
        
    # Virheilmoitusikkuna
    def openErrorMsgBox(self, errorTitle, errorText):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec() 


    
if __name__ == "__main__":

    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()


    