
class LandmarkDetection(Resource):

   def post(self):
        
        parse = reqparse.RequestParser()
        parse.add_argument('key', type=str, required=True, help='Your API key')
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='file that you want to send to the API')
        args = parse.parse_args()

        key= args['key']
        
        if key == 'YourApiKey':
            image_file = args['image']

            if utils.is_filename_safe(image_file):
                
                file_name = np.random.randint(1,10000000) # picking a random number for image
                image_file.save(f"{file_name}.jpg") # saving the image

                data = vision.landmarkDetection(str(file_name) + '.jpg') # detecting the objects in the image
                os.remove(f"{file_name}.jpg") #removing to original image
                img = Image.fromarray(data, 'RGB')
                img.save('img.jpg')
                return send_file('img.jpg') # {'status' : 'success'}, 201

            else:
                return {'status' : 'Unsupported Media type'}, 415  
        
        else:
            return {'status' : 'Unauthorized'}, 401    


