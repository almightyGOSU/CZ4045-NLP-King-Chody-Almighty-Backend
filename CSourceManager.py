import CDALSource;
import CCorpusManager;
from flask import url_for

def addNewSource(pJsonSource):
	##CCorpusManager.addTokens();
	intId = CDALSource.insertNewSource();

	if intId < 0:
		return None

	return url_for('getSource', source_id=intId, _external=True)
