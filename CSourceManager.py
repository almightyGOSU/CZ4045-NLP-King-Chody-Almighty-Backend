import CDALSource
import CFileManager
from CCorpusManager import CCorpusManager
from CSource import CSource
from flask import url_for
import CDALType

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
	lstTokens = CDALSource.getTypes()     
   
   ## text = Text(lstTokens)
   ## c = ConcordanceIndex(text.tokens, key = lambda s: s.lower())
 
   ## concordance_txt = ([text.tokens[map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset])[0]:offset+right_margin]
   ###                     for offset in c.offsets(pStrWord)])
                         
    return lstTokens

def getSourceSimilarity(pStrWord):

	#idx = ContextIndex([word.lower( ) for word in CDALSource.getTypes()])
	#save = []

    ##save.append(idx.similar_words(pStrWord))

	return CDALSource.getTypes()