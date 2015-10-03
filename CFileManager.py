import config

def saveToFile(pStrName, pStrContents):
	with open(config.FILE_PATH + pStrName + ".txt", 'w') as objFile:
		objFile.write(pStrContents)

def readFromFile(pStrName):
	with open(config.FILE_PATH + pStrName + ".txt", 'r') as objFile:
		strContents = objFile.read()

	return strContents