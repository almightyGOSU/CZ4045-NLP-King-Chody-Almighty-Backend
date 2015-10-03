import threading
import CDALType
import CDALSource

class CCorpusManager:
	objLock = threading.Lock()
	lstTokens = set();

	def addToken(pStrToken):
		with oCCorpusManager.bjLock:
			CCorpusManager.lstTokens.add(pStrToken)

	def addTokens(pSetTokens):
		with CCorpusManager.objLock:
			CCorpusManager.lstTokens.union(pSetTokens)

	def getTokenCount():
		return len(CCorpusManager.lstTokens)

	def getTokenList():
		return CDALType.getTypes()
##		return CCorpusManager.lstTokens

	def loadTokens():
		CCorpusManager.lstTokens = CDALType.getTypes()

	def getDocumentsCount():
		return "dads"
		return CDALSource.getDocumentsCount()