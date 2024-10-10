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
    def checkength(self) -> bool:
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
        else:
            return True

    # Pilkotaan henkilötunnus osiin
    def splitSsn(self, arg):
        pass

    # Muutetaan syntymäaikaosa ja vuosisata päivämääräksi
    def getDateOfBirth(self, arg):
        pass

    # Lasketaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass

    # Selvitetään varmistussumman avulla onko HETu syötetty oikein
    def isValidSsn(self, arg):
        pass
