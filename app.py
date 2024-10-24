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


while True:
    
    userGivenSsn =  input("Syötä asiakkaan henkilötunnus: ")
    userGivenSsn = userGivenSsn.upper() # Varmistetaan, että tarkiste on
    
    # TODO: Tee tarkistus siitä, että nim ei voi olla tyhjä

    # TODO: Rakenna funktio, joilla kysytään nimet ja yhdysnimet isoille alkukirjaimille -> reg exp



    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth()
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastname = input("Syötä asiakkan sukunimi ")
            userGivenLastname = userGivenLastname.capitalize()
            userGivenFirstname = input("Syötä asikkan etunimi ")
            userGivenFirstname = userGivenFirstname.capitalize()
            print("Syntymäaika:", ssnToCheck.dateOfBirth)
            print("Ikä:", age)
            print("Sukupuoli:", ssnToCheck.gender)
        except Exception as e:
            print("Syöttämässäsi sosissliturvatunnuksessa oli virhe", e)
        

        # Kysytään halutaanko poistan ohjelmasta
    wantAbort = input("Haluatko päättää ohjelman k/E: ")
    # Mutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko vastaus K
    if wantAbort.upper == "K":
        break # Poistetaan ikuiswsta silmukasta

