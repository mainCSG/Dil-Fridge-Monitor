from mss import mss
from datetime import datetime
import time
import cv2

###TODO Change to dropbox folder on local computer
path_to_dropbox_folder = "subfolder"

# Initial wait to give time to open camera
time.sleep(10)

with mss() as sct:
    while True:

        #defines filename
        filename = path_to_dropbox_folder + "\\" + str(datetime.now()).replace(':',"_") + ".png"

        # Takes screenshot
        sct.shot(output=filename)

        # Reads image, inverts it and then overwrites the file
        img = cv2.imread(filename)
        flipped_img = cv2.flip(img, 1)
        cv2.imwrite(filename, flipped_img)

        #Waits for 10 minutes between screenshots
        time.sleep(600)