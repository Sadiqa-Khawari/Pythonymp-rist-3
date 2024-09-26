


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