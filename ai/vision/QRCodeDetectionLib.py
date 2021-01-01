import cv2
import numpy as np
from pyzbar.pyzbar import decode
import numba

@numba.jit
def QRCodeDetection(imFile):
	"""
	finds positions and value of a QRcode
 	@param imFile (str) : file name of the image
    @return : result (dict) : containing Cordinates of the QRcode and its value
	"""
	result = dict()

	img = cv2.imread(imFile)

	for QRcode in decode(img):
		QRcodeValue = QRcode.data.decode('utf-8')
		corners = np.array(QRcode.polygon, dtype=np.int32)

		corners = tuple(map(tuple, corners))
		result['corners'] = str(corners)[1:-1]
		result['value'] = QRcodeValue

		return result
