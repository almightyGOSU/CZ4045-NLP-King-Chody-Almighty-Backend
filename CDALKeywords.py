import CDBManager

def getAllKeywords():
	objConnection = CDBManager.getDBConnection()

	try:
	    with objConnection.cursor() as objCursor:
	        # Read a single record
	        strSQL = "SELECT strKeywords FROM tblKeywords"
	        objCursor.execute(strSQL)
        	lstKeywords = [row[0] for row in objCursor.fetchall()]
	finally:
   		objConnection.close()

	return lstKeywords