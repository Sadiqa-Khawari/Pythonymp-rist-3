# LUOKKA HENKIÖTUNNUSTEN KÄSITTELYYN
# ==================================

# KIRJASTOT JA MOODUULIT
# ----------------------

# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    def __init__(self, ssn) -> None:
        self.ssn = ssn

        #   Laskemallä selvävät ominaisuudet
        self.deteOfBirth = " "
        self.number = 0
        self.gender = " "
        self.chechSum = " "

    # Luokan metodi osien laskentaan ja järkevyystar