import cv2
import numpy as np
from pyzbar.pyzbar import decode


def QRCodeDetection(imFile):
	img = cv2.imread(imFile)

	for barcode in decode(img):
		myData = barcode.data.decode('utf-8')
		return(myData)
