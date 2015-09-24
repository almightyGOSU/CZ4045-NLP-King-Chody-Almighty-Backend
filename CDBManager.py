import config
import pymysql

def getDBConnection():
	return pymysql.connect(
			host= config.DB_HOST,
			user=config.DB_USER,
			password=config.DB_PASSWORD,
			db=config.DB_NAME
		);