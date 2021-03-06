import CDALSource
import CFileManager
from CCorpusManager import CCorpusManager
from CSource import CSource
from flask import url_for
import CDALType
from nltk.tokenize import word_tokenize

def addNewSource(pJsonSource):

	objSource = CSource(pJsonSource["URL"], 
				pJsonSource["Content"],
				pJsonSource["Source"])

	intId = CDALSource.insertNewSource(
				objSource
			);

	if intId < 0:
		return None

##	CCorpusManager.addTokens(objSource.getTypes());
	CDALType.insertNewTypes(objSource.getTypes())

	return url_for('getSource', source_id=intId, _external=True)

def getSource(pIntId):
	objRow = CDALSource.getSource(pIntId)

	objRow[0] = CFileManager.readFromFile(str(objRow[0]))

	return objRow

def getCorpusSummary():
	return CDALSource.getCorpusSummary()

def getFullSource():

	for intCount in range(1, CCorpusManager.getDocumentsCount() + 1):
		yield "</br>" + CFileManager.readFromFile(str(intCount))

def getSourceTokens(pIntId):
	strText = CFileManager.readFromFile(str(pIntId))

	objSource = CSource("A", strText, "A")

	return objSource.getToken()

def getSourcePOS(pIntId):
	strText = CFileManager.readFromFile(str(pIntId))

	objSource = CSource("A", strText, "A")

	return objSource.getPOSTags()

def getSourceConcordance(pStrWord):
	return CDALSource.getTypes()

def getSourceSimilarity(pStrWord):

	strText = ""
	lstTokens = []

	for intCount in range(1, CCorpusManager.getDocumentsCount() + 1):
		lstTokens += word_tokenize(CFileManager.readFromFile(str(intCount)))

	return lstTokens

	#objCI = nltk.text.ContextIndex([word.lower() for word in lstTokens])
	#objCI = nltk.text.ContextIndex(['tasty','fluffy','yummy','','','','',''])
	#return objCI.similar_words(pStrWord)