import CDALSource;
from CCorpusManager import CCorpusManager;
from CSource import CSource
from flask import url_for
import CDALType

def addNewSource(pJsonSource):

	objSource = CSource(pJsonSource["URL"], 
				pJsonSource["Content"])

	intId = CDALSource.insertNewSource(
				objSource
			);

	if intId < 0:
		return None

	CCorpusManager.addTokens(objSource.getTypes());
	CDALType.insertNewTypes(objSource.getTypes())

	return intId;

	return url_for('getSource', source_id=intId, _external=True)
