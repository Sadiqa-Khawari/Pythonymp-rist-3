# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

#from avtools import sound # Äänimerkit ja äänitiedostot
#from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# TODO: Pääohjelma ikuinen silmukka, josta poistutaan tarvittaessa (kaksi mekanismi itse)
# TODO: Paranna pääohjelmaa siten, että se ei kaadu, kun käytää virheelisen henkilötunnuksen
userGivenSsn =  input("Syötä asiakkaan henkilötunnus: ")
userGivenLastname = input("Syötä asiakkan sukunimi")
# TODO: Tee tarkistus siitä, että nim ei voi olla tyhjä
userGivenFirstname = input("Syötä asikkan etunimi")
# TODO: Tee tarkistus siitä, että nim ei voi olla tyhjä
# TODO: Varautu tilanteeseen, jossa hetu:n tarkista on annettu pienillä kirjaimilla
# TODO: Muuta syötettyjen nimien alkukirjan

ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
if ssnToCheck.isValidSsn() == True:
    ssnToCheck.getDateOfBirth()
    ssnToCheck.getGender()
    age = ssnToCheck.calculateAge()
    print("Syntymäaika:", ssnToCheck.dateOfBirth)
    print("Ikä:", age)
    print("Sukupuoli:", ssnToCheck.gender)

