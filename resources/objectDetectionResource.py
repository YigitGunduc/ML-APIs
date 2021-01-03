import os
import utils
import werkzeug
import numpy as np
from PIL import Image
from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse, inputs

# object detection module
from ai.vision.objectDetectionLib import objectDetection

# object detection schema
from schemas.objectDetectionSchema import objectDetectionParser


class OjectDetectionResource(Resource):


    def get(self):

        args = objectDetectionParser.parse_args()
        
        image_file = args['image']

        if utils.is_filename_safe(image_file):
            file_name = np.random.randint(1, 10000000)  # picking a random number for image
            image_file.save(f"{file_name}.jpg")  # saving the image

        
            data = objectDetection(str(file_name) + '.jpg')  # detecting the objects in the image
            os.remove(f"{file_name}.jpg")  # removing to original image
            return data

        else:
            return {'status': 'Unsupported Media type'}, 415


