# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

userGivenSsn =  input("Syötä asiakkaan henkilötunnus: ")
ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
ssnToCheck.isValidSsn()

# Käynnistetään videokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
sound.parametricBeep(400,330)
sound.playWav('Alkaa.WAV')

# TESTIT KOODAUKSEN AIKANA
# ========================

if __name__ == "__main__":
    pass