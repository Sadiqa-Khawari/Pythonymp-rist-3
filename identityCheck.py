


""" Moudule makes sanity check for RAseko student id and the Finish Social Secority
"""

# KIRJASTOT JA MOUDUULIT
# ----------------------

# FUNKTIOT
# --------

# Opiskelijatunnuksen oikea muoto
def opeskelijanumeroOk(opeskelijanumero: str) -> bool:
    """Check if student number is 5 or 6 digitus and does not contain any
    characters other than numbers

    Args:
        opeskelijanumero (str): Raseko`s student id
    returns:
        bool: True if correct otherwise False
    """
    result: bool = False
    pituus = len(opeskelijanumero)
    if pituus == 5 or pituus == 6:
            result = True
    return result

# Henkilotunnus esimerkki 130787-676 testataan
# 1. Pituus 
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - ja A
# 4. Moduli 31 tarkistus

# Loullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja 

def checkHeTu(hetu):
  
    # Oletustulos 0 ok jos kaikki on kunnossa
    result = (0, "ok")

    # Lasketaan HeTu-parametrin pitus
    length = len(hetu)

    # Jos pitus oikea tehdään eri osat
    if length == 11:
        dayPart = hetu[0:2]
        monthPart = hetu[2:4]
        yearPart = hetu[4:6]
        centuryPart = hetu[6:7]
        numberPart = hetu[7:10]
        checkSum = hetu[10]

        #  Tarkistwtaan päiväosan oikeellisuus pitää olla pelkkiä numeroita
    if dayPart.isdigit():
        day = int(dayPart)

        # Päivän pitää olla väliltä 1 -31
        if day < 1:
            result = (3, "Päivä virheellinen")
        if day > 31:
            result = (3, "Päivä virheellinen")
    else:
            # Jos muuta kuin pelkkiä numeroita
            result = (3, "Päivä virheellinen")
       
    if length < 11:
        result = ( 1, "Henkilötunnus liian lyhyt")
    
    if length > 11:
        result = ( 2, "Henkilötunnus liian pitkä")

   
    return result

if __name__ == "__main__":
     hetu = "130728-478N"
     paivat = hetu[0:2]
     kuukaudet = hetu[2:4]
     print(paivat)
     print(kuukaudet)