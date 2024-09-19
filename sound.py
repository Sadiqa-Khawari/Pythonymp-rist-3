# MODUULI ÄÄNIMERJJIEN ANTAMISEEN
# ===============================

# KIRJASTOT JA MODUULIT
# ---------------------

# Wndows-äänet
import winsound

# Ajankäsittely
import time

#  ÄÄNIFUNKITOT
# -------------

def shortBeep():
    """Creates a 1 KHz sound for 1/4 second
    """
    winsound.Beep(1000, 250)

def longBeep():
    """Creates a 1 KHz sound for 2 second
    """
    winsound.Beep(1000,2000)

def waitMs(ms):
    """Waits for timeperiod
    
    Args:
         ms (int): time in milliseconds
         """
    seconds = ms / 1000
    time.sleep(seconds)

# Säädettävät äänet 1. korkeus ja kesto parametreina 
def parametricBeep(frequency, duration):
    """Produces a suond at given frequency and duration
        
    Args:
        frequency (int): Frequency of the tone in Hz
        duration (int): Durantion in milliseconds
    """
    winsound.Beep(frequency, duration)

# Säädettävät äänet 2. toistuva äänimerkki korkeus, kesto ja määrä

# Ääni tulee halutusta tiedostosta, parametrina äänet nimi 

if __name__ == "__main__":
    #shortBeep()
    # waitMs(500)
    # longBeep()
    waitMs(500)
    parametricBeep(360)