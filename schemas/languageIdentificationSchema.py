from flask_restful import Resource, reqparse, inputs

languageIdentificationParser = reqparse.RequestParser()
languageIdentificationParser.add_argument('text', type=str, required=True)
