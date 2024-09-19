# MODUULI VIDEOKUVAN KÄSITTELYYN
# ==============================

# KIRJASTOT JA MODUULIT
# ---------------------

# Ulkoinen kirjasto opencv-python ladataan nimellä CV2
import cv2

# FUNKITO, JOKA KÄYNNISTÄÄ WEB- KAMERA JA NÄYTTÄÄ KUVAA IKKUNASSA
# ---------------------------------------------------------------

def webstream(camIx):
    """ Opens a video stream and show frames in windew

    Args:
         camIx (int): Index of the camera srarting from 0
    """

   # Define the name of Video Window
    windowName = "Kamera " + str(camIx)


   # Create a capture object for the video stream
    capture = cv2.VideoCapture(camIx)
 
   # MAIN LOOP FOR THE APP TO RUN
   # ============================

   # While getting the stream show video on a window 
    while capture.isOpened():
        ret, frame = capture.read()
    
         # kun striimi lopuu, 
        if not ret:
           print("Can't receive frames. Exiting ...")
           break
 
        # Define a key press (q) to interrupt/quit the program 
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == ord('q'):
           break
 
    # Finally release capture object and close the window
    capture.release()
    cv2.destroyAllWindows()

    # TESTIT
    # ======
    if __name__ == "__main__":
     
      webstream(1)

