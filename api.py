import os
import werkzeug
import numpy as np
from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse, inputs
from PIL import Image
import utils
import vision

app = Flask(__name__)
api = Api(app)


class OjectDetection(Resource):

    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('key', type=str, required=True, help='Your API key')
        parse.add_argument('mode', type=str, required=False, help='mode(label/return-classes) label : labels and return a new image, return-classes : return found classes in the image in a json format')
        parse.add_argument('put-text', type=inputs.boolean, required=False)
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
        args = parse.parse_args()

        apiKey = args['key']
        mode = args['mode']
        putText = args['put-text']

        if apiKey == 'YourApiKey':
            image_file = args['image']

            if utils.is_filename_safe(image_file):
                file_name = np.random.randint(1, 10000000)  # picking a random number for image
                image_file.save(f"{file_name}.jpg")  # saving the image

                if mode == 'label':
                    data = vision.objectDetection(str(file_name) + '.jpg', mode=mode, putText=putText)  # detecting the objects in the image
                    os.remove(f"{file_name}.jpg")  # removing to original image
                    img = Image.fromarray(data, 'RGB')
                    img.save('img.jpg')
                    return send_file('img.jpg')

                if mode == 'return-classes':
                    data = vision.objectDetection(str(file_name) + '.jpg', mode=mode)  # detecting the objects in the image
                    os.remove(f"{file_name}.jpg")  # removing to original image
                    return {'objects': data}

            else:
                return {'status': 'Unsupported Media type'}, 415

        else:
            return {'status': 'Unauthorized'}, 401    


class LandmarkDetection(Resource):

    def post(self):
        
        parse = reqparse.RequestParser()
        parse.add_argument('apiKey', type=str, required=True, help='Your API key')
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
        args = parse.parse_args()

        apiKey= args['apiKey']

        if apiKey == 'YourApiKey':
            image_file = args['image']

            if utils.is_filename_safe(image_file):

                file_name = np.random.randint(1,10000000)  # picking a random number for image
                image_file.save(f"{file_name}.jpg")  # saving the image

                data = vision.landmarkDetection(str(file_name) + '.jpg')  # detecting the objects in the image
                os.remove(f"{file_name}.jpg")  # removing to original image
                img = Image.fromarray(data, 'RGB')
                img.save('img.jpg')
                return send_file('img.jpg')  # {'status' : 'success'}, 201

            else:
                return {'status': 'Unsupported Media type'}, 415

        else:
            return {'status': 'Unauthorized'}, 401


api.add_resource(OjectDetection, "/api/v1/vision/object-detection")
api.add_resource(LandmarkDetection, "/api/v1/vision/landmarks-detection")

if __name__ == "__main__":
    app.run(debug=True)
