from nltk.tokenize import sent_tokenize, word_tokenize

class CSource:

	def __init__(self, pStrUrl, pStrContents, pStrSource):
		self._strURL = pStrUrl
		self._strContents = pStrContents
		self._lstSentence = sent_tokenize(pStrContents)
		self._lstToken = word_tokenize(pStrContents)
		##self._lstType = set(token.lower() for token in self._lstToken)

		lstLower = [token.lower() for token in self._lstToken]

		self._lstType = [(token,lstLower.count(token)) for token in set(lstLower)]

		self._strSource = pStrSource;

	def getURL(self):
		return self._strURL

	def getTokenCount(self):
		return len(self._lstToken)

	def getSentenceCount(self):
		return len(self._lstSentence)

	def getTypeCount(self):
		return len(self._lstType)

	def getTypes(self):
		return self._lstType

	def getSource(self):
		return self._strSource

	def getContents(self):
		return self._strContents
