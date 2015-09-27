import CDBManager

def insertNewTypes(pSetTypes):
	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:

			strSQL = "INSERT INTO tblTypes (strWord, intCount) VALUES (%s,%s) ON DUPLICATE KEY UPDATE intCount=intCount+%s;"

			objCursor.executemany(strSQL, pSetTypes)
			objConnection.commit()

			intId=1
	except:
		intId = -99
	finally:
		objConnection.close()

	return intId

def getTypes():
	objConnection = CDBManager.getDBConnection()

	try:
	    with objConnection.cursor() as objCursor:
	        # Read a single record
	        strSQL = "SELECT strWord FROM tblTypes"
	        objCursor.execute(strSQL)
        	lstTokens = set(row[0] for row in objCursor.fetchall())
	finally:
   		objConnection.close()

	return lstTokens