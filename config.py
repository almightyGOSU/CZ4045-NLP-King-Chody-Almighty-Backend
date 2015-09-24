import os

DB_HOST= os.getenv("OPENSHIFT_MYSQL_DB_HOST", "localhost")
DB_USER = os.getenv("OPENSHIFT_MYSQL_DB_USERNAME", "admin")
DB_PASSWORD= os.getenv("OPENSHIFT_MYSQL_DB_PASSWORD", "admin")
DB_NAME= "nlp"

NLTK_PATH= os.getenv("OPENSHIFT_DATA_DIR", "")