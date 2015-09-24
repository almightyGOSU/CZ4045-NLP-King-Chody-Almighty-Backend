import config

def getDBConnection():
	return pymsql.connect(
			host= config.DB_HOST,
			user=config.DB_USER,
			password=config.DB_PASSWORD,
			db=config.DB_NAME
		);