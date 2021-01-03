import os
import utils
import werkzeug
import numpy as np
from PIL import Image
from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse, inputs

# face detection module
from ai.vision.faceDetectionLib import faceDetection

# face detection schema
from schemas.faceDetectionSchema import faceDetectionParser


class FaceDetectionResource(Resource):

    def get(self):
        
        args = faceDetectionParser.parse_args()

        image_file = args['image']

        file_name = np.random.randint(1,10000000)  # picking a random number for image
        image_file.save(f"{file_name}.jpg")  # saving the image

        data = faceDetection(str(file_name) + '.jpg')  # detecting the objects in the image
        os.remove(f"{file_name}.jpg")  # removing to original image
        img = Image.fromarray(data, 'RGB')
        img.save('img.jpg')
        return send_file('img.jpg')  # {'status' : 'success'}, 201