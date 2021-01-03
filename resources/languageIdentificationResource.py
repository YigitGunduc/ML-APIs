import os
import utils
import werkzeug
import numpy as np
from PIL import Image
from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse, inputs

from ai.nlp.languageIdentificationLib import languageIdentification

from schemas.languageIdentificationSchema import languageIdentificationParser

class LanguageIdentificationResource(Resource):

    def get(self):
        
        args = languageIdentificationParser.parse_args()

        text = args['text']

        langs = languageIdentification(text)  #

        return langs