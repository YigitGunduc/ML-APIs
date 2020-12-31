from flask_restful import Resource, reqparse, inputs
import werkzeug

objectDetectionParser = reqparse.RequestParser()
objectDetectionParser.add_argument('key', type=str, required=True, help='Your API key')
objectDetectionParser.add_argument('mode', type=str, required=False, help='mode(label/return-classes) label : labels and return a new image, return-classes : return found classes in the image in a json format')
objectDetectionParser.add_argument('put-text', type=inputs.boolean, required=False)
objectDetectionParser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
