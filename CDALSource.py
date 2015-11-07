import CDBManager
import CFileManager

def getSource(pIntId):
	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:
			strSQL = "SELECT * FROM  tblCorpus WHERE  intDocNo =%s"

			objCursor.execute(strSQL, pIntId)

			objRow = objCursor.fetchone()

			aryResult = [objRow[0], objRow[1], objRow[2], objRow[3], objRow[4]]

	except:
		aryResult = []
	finally:
		objConnection.close()

	return aryResult


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

	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:
			strSQL = "SELECT MAX(intDocNo) FROM tblCorpus"

			objCursor.execute(strSQL)

			intCount = objCursor.fetchone()[0]
	except:
		intCount = -99
	finally:
		objConnection.close()

	return intCount

def getTypes():
	objConnection = CDBManager.getDBConnection()

	try:
	    with objConnection.cursor() as objCursor:
	        # Read a single record
	        strSQL = "SELECT strWord FROM tblTypes"
	        objCursor.execute(strSQL)
        	lstKeywords = [row[0] for row in objCursor.fetchall()]
	finally:
   		objConnection.close()

	return lstKeywords

def getCorpusSummary():

	objConnection = CDBManager.getDBConnection()

	try:
	    with objConnection.cursor() as objCursor:
	        # Read a single record
	        strSQL = "SELECT COUNT(intDocNo) FROM `tblCorpus`"
	        objCursor.execute(strSQL)
	        lstStats = [objCursor.fetchone()[0],"owen", "owen", "owen"]
        	#lstStats = objCursor.fetchone()[0]
	finally:
   		objConnection.close()

	return lstStats
