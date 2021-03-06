import CDBManager

def insertNewTypes(pSetTypes):
	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:

			strSQL = "CALL insertType(%s,%s);"
			
			objCursor.executemany(strSQL, pSetTypes)
			objConnection.commit()

			intId=1
	except Exception as e:
		intId = -99
		print (e)
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