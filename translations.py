import json

global transl
with open('translations.json') as json_file:
	transl = json.load(json_file)

def cTranslate (toTranslate,toLanguage):
	language = internalDetection(toTranslate)
	if language != False:
		index = language[1]
		return translate(index,toLanguage)
	else:
		return False

def internalDetection(toDetect):
	i = 0
	for (key, value) in transl:
		language = transl[i]['lang']
		contents = list(transl[i]['contents'])
		j = 0
		for item in contents:
			if (contents[j] == toDetect):
				return [language,j]
			j=j+1
		i=i+1;
	return False


def languageDetect(toDetect):
	i = 0
	for (key, value) in transl:
		language = transl[i]['lang']
		contents = list(transl[i]['contents'])
		j = 0
		# Looping trough each word
		for item in contents:
			if (contents[j] == toDetect):
				return language
			j=j+1
		i=i+1;
	return False


def translate(translationIndex,toLanguage):
	i = 0
	for (key, value) in transl:
		if transl[i]['lang'] == toLanguage:
			return transl[i]['contents'][translationIndex]
		i=i+1
	return False