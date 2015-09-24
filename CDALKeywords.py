import CDBManager

def getAllKeywords():
	objConnection = CDBManager.getDBConnection()

	try:
	    with objConnection.cursor() as objCursor:
	        # Read a single record
	        strSQL = "SELECT strKeywords FROM tblKeywords"
	        cursor.execute(strSQL)
        	lstKeywords = list(objCursor.fetchall())
	finally:
   		connection.close()

	return lstKeywords