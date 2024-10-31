# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKTIOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (str): a single character to convert

    Returns:
        int: Code128B value for calcultaing the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculateCode128BCheksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: Modulo 103 checksum of weighted values
    """
    text = text.strip() # Poistetaan ylimääräiset tyhjät alusta ja lopusta
    numberOfLetters = len(text)
    weightedSum = 0 # Alustetaan summa tyhjäksi

    # Käydään teksti kirjaimittain läpi
    for number in range(numberOfLetters):
        letter = text[number]

        # Kutsutaan funktiota, joka palauttaa 128-koodin
        code128BValue = barCodeValue(letter)

        # Lasketaan sijainnilla painotettu arvo
        weightedValue = code128BValue * (number + 1)

        # Lisätetään se summaan
        weightedSum = weightedSum + weightedValue

        # Lisätään alkumerkin arvo
    weightedSum = weightedSum + 104 
    code128BChecksum = weightedSum % 103 # Lasketaan jakojäänns mod 
    return code128BChecksum

# TODO: Tee tämä funktio loppuun ja testaa sitä Notepadissa
def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code 128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BarcodeString = ''
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculateCode128BCheksum(text)
    checkSumSymbol = chr(checkSum + 32)
    code128BarcodeString = startChar + text + checkSumSymbol + stopChar
    return code128BarcodeString

if __name__ == "__main__":
    testString = '128B'
    print('painotetut arvot yhteensä:',calculateCode128BCheksum(testString))
    print("Koko viivakoodi on", createCode128B("128B"))