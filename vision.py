import numpy as np
import dlib
import cv2

# Load Yolo
net = cv2.dnn.readNet("thirdparty/yolo/yolov3.weights", "thirdparty/yolo/yolov3.cfg")
classes = []
with open("thirdparty/yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading landmarks detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("thirdparty/shape_predictor_68_face_landmarks.dat")


# Loading image
def objectDetection(imFile,mode = 'return-classes',putText = True):
	img = cv2.imread(imFile)
	height, width, channels = img.shape
	# Detecting objects
	blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
	net.setInput(blob)
	outs = net.forward(output_layers)

	# Showing informations on the screen
	class_ids = []
	confidences = []
	boxes = []
	for out in outs:
	    for detection in out:
	        scores = detection[5:]
	        class_id = np.argmax(scores)
	        confidence = scores[class_id]
	        if confidence > 0.5:
	            # Object detected
	            center_x = int(detection[0] * width)
	            center_y = int(detection[1] * height)
	            w = int(detection[2] * width)
	            h = int(detection[3] * height)
	            # Rectangle coordinates
	            x = int(center_x - w / 2)
	            y = int(center_y - h / 2)
	            boxes.append([x, y, w, h])
	            confidences.append(float(confidence))
	            class_ids.append(class_id)

	indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
	
	if mode == 'label':
	
		font = cv2.FONT_HERSHEY_PLAIN
		for i in range(len(boxes)):
			if i in indexes:
				x, y, w, h = boxes[i]
				label = str(classes[class_ids[i]])
				color = colors[i]
				cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
				if putText == True:
					cv2.putText(img, label, (x, y + 30), font, 2, color, 2)
	
		return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	if mode == 'return-classes' :
		dct = dict()
		for i in range(len(boxes)):
		    if i in indexes:
		    	label = str(classes[class_ids[i]])
		    	dct[label] = confidences[i]
		    	
		return dct



def landmarkDetection(imFile):
	frame = cv2.imread(imFile)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = detector(gray)
	for face in faces:
		x1 = face.left()
		y1 = face.top()
		x2 = face.right()
		y2 = face.bottom()
		#cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

		landmarks = predictor(gray, face)

		for n in range(0, 68):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			cv2.circle(frame, (x, y), 2, (50, 255, 20), -1)

	return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
