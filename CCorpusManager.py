lstTokens = {};

def addToken(pStrToken):
	with self.lock:
		lstTokens.add(pStrToken)

def addTokens(pSetTokens):
	with self.lock:
		lstTokens.union(pSetTokens)

def getTokenCount():
	return len(lstTokens)

def getTokenList():
	return lstTokens