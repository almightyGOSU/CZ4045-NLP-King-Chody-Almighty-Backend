import CDALSource
import CFileManager
from CCorpusManager import CCorpusManager
from CSource import CSource
from flask import url_for
import CDALType
import nltk
import nltk.text

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
	ContextIndex([word.lower() for word in CDALSource.getTypes()])
	return CDALSource.getTypes()