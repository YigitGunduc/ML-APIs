import os
import utils
import werkzeug
import numpy as np
from PIL import Image
from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse, inputs

# face detection module
from ai.vision.QRCodeDetectionLib import QRCodeDetection

# face detection schema
from schemas.QRCodeDetectionSchema import QRCodeDetectionParser


class QRCodeDetectionResource(Resource):

    def get(self):
        
        args = QRCodeDetectionParser.parse_args()

        image_file = args['image']

        file_name = np.random.randint(1,10000000)  # picking a random number for image
        image_file.save(f"{file_name}.jpg")  # saving the image
        data = QRCodeDetection(str(file_name) + '.jpg')  # detecting the objects in the image
        os.remove(f"{file_name}.jpg")  # removing to original image
        return data # {'status' : 'success'}, 201