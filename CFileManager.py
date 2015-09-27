import config

def saveToFile(pStrName, pStrContents):
	with open(config.FILE_PATH + pStrName + ".txt", 'w') as objFile:
		objFile.write(pStrContents)