from flask_restful import Resource, reqparse, inputs
import werkzeug


faceDetectionParser = reqparse.RequestParser()
faceDetectionParser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
