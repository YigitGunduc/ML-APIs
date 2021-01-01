from langdetect import detect, detect_langs

def languageIdentification(text):
	lang = detect(text)
	confidenceDistribution = detect_langs(text)
	return {'Identified-Language':lang,'Confidence-Distribution': str(confidenceDistribution) }
