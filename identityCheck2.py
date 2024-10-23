# LUOKKA HENKIÖTUNNUSTEN KÄSITTELYYN
# ==================================

# KIRJASTOT JA MOODUULIT
# ----------------------

# kirjosto päivämäärälaskenta varten
import datetime

# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    """Varios methods to access and validate Finish Security Number propersties
    """
    def __init__(self, ssn: str) -> None:
        """Generates a Finish SSN object

        Args:
            ssn (str): 11 character SSN to process
        """
        self.ssn = ssn

        # Laskemallä selvävät ominaisuudet
        self.deteOfBirth = " "
        self.number = 0
        self.gender = " "
        self.chechSum = " "

        # Sanakirjat vuosisatakoodeille ja varmisteille
        self.centuryCodes = {
        '+': "1800",
        '-': "1900",
        'A': "2000"
        }

        self.moduloSymbols = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'H',
        17: 'J',
        18: 'K',
        19: 'L',
        20: 'M',
        21: 'N',
        22: 'P',
        23: 'R',
        24: 'S',
        25: 'T',
        26: 'U',
        27: 'V',
        28: 'W',
        29: 'X',
        30: 'Y'
        }
    # Luokan metodi osien laskentaan ja järkevyystarkistuksiin

    # Tarkistaan, että HeTu:n pitus on 11 merkkiä
    def checkSsnLengthOk(self) -> bool:
        """Checks correct length of the SSN

        Returns:
            bool: 
        """
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
            # TODO: Mieti pittäisikö tässä generoida virheilmoitus (raise)
        else:
            return True

    # Pilkotaan henkilötunnus osiin
    def splitSsn(self) -> dict:
        """Splits the SSN to functional parts ie. birthdate, century, number and the checksum

        Returns:
            dict: parts as strings
        """
        # Tehdään pikkominen vain jos pitus on oikein
        if self.checkSsnLengthOk(): # Jos Ture pikotaan, huom. self.metodinNimi
            dayPart = self.ssn[0:2]
            monthPart = self.ssn[2:4]
            yearPart = self.ssn[4:6]
            centuryPart = self.ssn[6]
            birthNumberPart = self.ssn[7:10]
            checksumPart = self.ssn[10]
            return {"days" : dayPart,
                    "months" : monthPart,
                    "years" : yearPart,
                    "century" : centuryPart,
                    "number" : birthNumberPart,
                    "checksum" : checksumPart
                    }
        else:
            # TODO : Mieti, pitäisikö synnyttää vihretilanne raisella
            return {"status" : "error"}
        
    # Muutetaan syntymäaikaosa ja vuosisata päivämääräksi
    def getDateOfBirth(self) -> None:
        """Sets the value of dateOfBirths property for object
        """
        # TODO: Onko järkeä hakea syntymäaikaa, jos hetu muuten virheellinen?
        if self.checkSsnLengthOk():
            isoDate = "1799-12-31"
            parts = self.splitSsn()
            centurySymbol = parts["century"]

            # TODO: Mitä jos symboli on väärä, sitähän ei huomioida järkevyystarkistuksessa -> kaatuu

            century = self.centuryCodes[centurySymbol]
            isoDate = century[0:2] + parts["years"] + "-" + parts["months"] + "-" + parts["days"]
            self.dateOfBirth = isoDate

    
    # Selvitetään varmistussumman avulla onko HETu syötetty oikein
    def isValidSsn(self) -> bool:
        """Recalculate the checksum of the SSN and verifies it is the same in the given SSN 

        Returns:
            bool: Ture if SSN valid, False otherwise
        """
        if self.checkSsnLengthOk:
            parts = self.splitSsn()
            moduloString = parts["days"] + parts["months"] + parts["years"] + parts["number"]
            moduloNumeric = int(moduloString)
            checkSumCalculated = moduloNumeric % 31
            checkSumCalculatedSymbol = self.moduloSymbols[checkSumCalculated]
            if checkSumCalculatedSymbol == parts["checksum"]:
                return True
            else:
                return False
        else:
            return False
        
    # Lasketaan ikä nyt täysinä vuosina
    def calculateAge(self):
        pass
        # Tarkistetaan ennen laskentaa, että henkilötunus on oikein syötetty

            #Muutetaan olin syntymääaikaominaisuuteen talennrttu ISO-päivämäärä python-päivämäräksi

            #Haetaan nykyinen päivämäärä

            #Lasketaan päivämäärien ero täysinä vuosina

            # Palautetaan ikä vuosina
            
# MAIN KOKEILUJA VARTEN (POISTA KUN EI ENÄÄ TARVITAN)
# ===================================================

if __name__ == "__main__":
    hetu1 = NationalSSN("130728-478N")
    hetu1.getDateOfBirth()
    ika = hetu1.calculateAge()
    print("Oikein muodostettu: ", hetu1.checkSsnLengthOk())
    print("HeTun osat ovat: ", hetu1.splitSsn())
    print("Syntymäaikaosa ISO-muodossa on ", hetu1.dateOfBirth)
    print("Henkilötunnus on oikein muodostettu", hetu1.isValidSsn())
    print("Henkilön ikä on", ika)
