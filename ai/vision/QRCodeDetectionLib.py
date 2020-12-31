import cv2
import numpy as np
from pyzbar.pyzbar import decode


def QRCodeDetection(imFile):
			
	result = dict() 

	img = cv2.imread(imFile)

	for barcode in decode(img):
		data = barcode.data.decode('utf-8')
		points = np.array(barcode.polygon,dtype=np.int32)
		
		corners = tuple(map(tuple, points))
		result['Corners'] = str(corners)[1:-1]
		result['Value'] = data
		
		return result
