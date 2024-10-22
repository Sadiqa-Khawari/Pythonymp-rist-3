# LUOKKA HENKIÖTUNNUSTEN KÄSITTELYYN
# ==================================

# KIRJASTOT JA MOODUULIT
# ----------------------

# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    """Varios methods to access and validate Finish Security Number propersties
    """
    def __init__(self, ssn) -> None:
        """Generates a Finish SSN object

        Args:
            ssn (str): 11 character SSN to process
        """
        self.ssn = ssn

        #   Laskemallä selvävät ominaisuudet
        self.deteOfBirth = " "
        self.number = 0
        self.gender = " "
        self.chechSum = " "

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
                    "month" : monthPart,
                    "years" : yearPart,
                    "century" : centuryPart,
                    "number" : birthNumberPart,
                    "checksum" : checksumPart
                    }
        else:
            # TODO : Mieti, pitäisikö synnyttää vihretilanne raisella
            return {"status" : "error"}
    # Muutetaan syntymäaikaosa ja vuosisata päivämääräksi
    def getDateOfBirth(self, arg):
        pass

    # Lasketaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass

    # Selvitetään varmistussumman avulla onko HETu syötetty oikein
    def isValidSsn(self, arg):
        pass

# MAIN KOKEILUJA VARTEN (POISTA KUN EI ENÄÄ TARVITAN)
# ===================================================

if __name__ == "__main__":
    hetu1 = NationalSSN("130728-478N")
    print("Oikein muodostettu: ", hetu1.checkSsnLengthOk())
    print("HeTun osat ovat: ", hetu1.splitSsn())