from flask_restful import Resource, reqparse, inputs
import werkzeug

objectDetectionParser = reqparse.RequestParser()
objectDetectionParser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
