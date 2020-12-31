# imports
from flask import Flask
from flask_restful import Api

# Resources
from resources.faceDetectionResource import FaceDetectionResource
from resources.objectDetectionResource import OjectDetectionResource
from resources.QRCodeDetectionResource import QRCodeDetectionResource
app = Flask(__name__)
api = Api(app)

api.add_resource(QRCodeDetectionResource, '/vision/qrcode-detection')
api.add_resource(OjectDetectionResource, "/vision/object-detection")
api.add_resource(FaceDetectionResource, "/vision/face-detection")

if __name__ == "__main__":
    app.run(debug=True)
