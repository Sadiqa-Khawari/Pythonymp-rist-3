# MODUFLI vvVACOODIEN TUOTTAMISEEN 
# ================================

# kIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKITOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (str): a single chracter to convert

    Returns:
        int: Code128B value for calcultaing the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue -32
    return code128BValue

def calculateCode128BCheksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): texr string to use in a barcode

    Returns:
        int: Modulo 103 checksum of weighd values
    """
    text = text.strip()
    numberOfLetters = len(text)
    code128BChecksum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum = weightedSum + weightedValue
    weightedSum = weightedSum + 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum

#TODO :Tee tämä funktio loppuun ja te
def createCode128B(text: str) -> str:
    """Creates a complete code 128B to be printed using libre code 128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """

    code128BarcodeString = ""
    return code128BarcodeString

if __name__ == "__main__":
    testString = "128B"
    print("painotetut arvot yhteensa:", calculateCode128BCheksum(testString))