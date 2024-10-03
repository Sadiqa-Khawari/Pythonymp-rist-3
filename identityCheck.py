


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

    # Vuosisatakoodien sanakirja
    centuryCodes = {
         "+": 1800,
         "-": 1900,
         "A": 2000,
    }

    validCenturyCodes = centuryCodes.keys()

    

    # Sanakirja, jossa on jakojäännösten kirjaintunnuksen
    modulusSymbol = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "H",
        17: "J",
        18: "K",
        19: "L",
        20: "M",
        21: "N",
        22: "p",
        23: "R",
        24: "S",
        25: "T",
        26: "U",
        27: "V",
        28: "W",
        29: "X",
        30: "Y"

    }
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

    # Jos muuta kuin pelkkiä numeroita
    else:
        
            result = (3, "Päivä virheellinen")

    # Trkistatetan kuukausiosan oikeellisuus, pitä olla pelkkiä numeroita
    if monthPart.isdigit():
         month = int(monthPart)

        # Kuukausi pitää olla väliltä 1 -12
         if month < 1:
            result = (4, "Kuukausi virheellinen")
         if month > 12:
            result = (4, "Kuukausi virheellinen")
    # Jos muuta kuin pelkkkiä numeroita
    else:
         result = (4, "kuukausi virheellinen")

        # Trkistatetan kuukausiosan oikeellisuus, pitä olla pelkkiä numeroita
    if yearPart.isdigit():
         year = int(yearPart)
    else:
         result = (5, "Vuosi virheellinen")

         #TODO: Tähän Try-Except, jolla trakistetaan vuosisatakoodi

         # TODO: Tähän moduli 31 tarkisteen 

       
    if length < 11:
        result = ( 1, "Henkilötunnus liian lyhyt")
    
    if length > 11:
        result = ( 2, "Henkilötunnus liian pitkä")

   
    return result

if __name__ == "__main__":
     hetu = "130728-478N"
     paivat = hetu[0:2]
     kuukaudet = hetu[2:4]
    # print(paivat)
    # print(kuukaudet)

    # Vuosisatakoodien sanakirja
    centuryCodes = {
         "+": 1800,
         "-": 1900,
         "A": 2000
    }

    validCenturyCodes = list(centuryCodes.keys())
    validCC = [*centuryCodes.keys()]
    print("Hassu tapa", validCC)
    print("Listafuntkiolla", validCenturyCodes)

    # Haetaan vuosisata avaimen perusteella
    print("Vuosisatakoodi - on " , centuryCodes["-"])

    # Vuosisatakoodien avaimet listana
    print("Sallitut vuosisatakoodit ovat", validCenturyCodes)

    # Haetaan olemattalla avalla
   # print("Vuosisatakoodi * on", centuryCodes["*"])

    # Haetaanindeksinumero listan jäsenelle
    try:
        position = validCenturyCodes.index("*") 
        print(position)
    except:
        print("Ei löytynyt")