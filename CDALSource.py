import CDBManager
import CFileManager

def insertNewSource(pObjSource):

	if pObjSource.getSource() == "Social" and pObjSource.getTokenCount() < 20:
		return -99

	if pObjSource.getSource() == "Web" and pObjSource.getSentenceCount() < 5 and pObjSource.getTokenCount() < 80:
		return -99

	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:
			strSQL = "INSERT INTO `tblCorpus`(`strUrl`, `intTokenCount`, `intSentenceCount`, `intTypeCount`) VALUES (%s, %s, %s, %s)"
			objCursor.execute(strSQL, (pObjSource.getURL(),
								pObjSource.getTokenCount(), pObjSource.getSentenceCount(), 
								pObjSource.getTypeCount()))
			objConnection.commit()

			strSQL = "SELECT LAST_INSERT_ID()"

			objCursor.execute(strSQL)

			intId = objCursor.fetchone()[0]
	except:
		intId = -99
	finally:
		objConnection.close()

	CFileManager.saveToFile(str(intId), pObjSource.getContents())

	return intId

def getDocumentsCount():

	return "owen"

	##try:
	##	with objConnection.cursor() as objCursor:
##
##			strSQL = "SELECT MAX(intDocNo) FROM tblCorpus"
##
##			objCursor.execute(strSQL)
##			intCount = objCursor.fetchone()[0]
##	except:
##		intCount = -99
##	finally:
##		objConnection.close()

##	return intCount
