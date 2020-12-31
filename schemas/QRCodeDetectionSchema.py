from flask_restful import Resource, reqparse, inputs
import werkzeug


QRCodeDetectionParser = reqparse.RequestParser()
QRCodeDetectionParser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
