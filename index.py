from flask import Flask, jsonify ,request, abort
import CKeywordManager
import CSourceManager
import config
from CCorpusManager import CCorpusManager
from flask import Response

from nltk.corpus import brown

app = Flask(__name__)

def validateJson(pObjRequest):
	if(not pObjRequest.json):
		abort(400)

@app.route("/", methods=["GET"])
def index():

	intCount = 0

	strOutput = ""
	for strWord in brown.words():
		strOutput += strWord
		strOutput += " , "
		intCount = intCount + 1

		if intCount >=50:
			return strOutput

	return strOutput

@app.route("/types", methods=["GET"])
def getTypes():
	strOutput = ""
	for strWord in CCorpusManager.getTokenList():
		strOutput += strWord
		strOutput += "<br/>"

	return strOutput

@app.route("/summary", methods=["GET"])
def getCorpusSummary():
	lstStats = CSourceManager.getCorpusSummary()

	return "<html><body><table border='1'><th><td>Something</td><td>Status</td></th><tr><td>Document Count</td><td>" + str(lstStats[0]) + "</td></tr><tr><td>Token Count</td><td>" + str(lstStats[1]) + "</td></tr><tr><td>Type Count</td><td>" + str(lstStats[2]) + "</td></tr><tr><td>Sentence Count</td><td>" + str(lstStats[3]) + "</td></tr></table><div>Call <strong style='color: #FF0000;'>+65 9017 2413</strong> for any technical issues</div></body></html>"

@app.route("/keywords", methods=["GET"])
def getKeywords():
	lstKeywords = CKeywordManager.getAllKeywords()
	return jsonify({ "keywords":lstKeywords})

@app.route("/source" , methods=["POST"])
def addSource():
	##validateJson(request)

	strUri = CSourceManager.addNewSource(request.get_json())

	if strUri == None:
		abort(503)

	return jsonify({"insert-uri":strUri}) , 201

@app.route("/source/length")
def getDocumentCount():
	return str(CCorpusManager.getDocumentsCount())

@app.route("/source/token/<int:source_id>", methods=["GET"])
def getSourceTokens(source_id):

	strOutput = ""

	for strToken in CSourceManager.getSourceTokens(source_id):
		strOutput += str(strToken)
		strOutput += "<br/>"

	return strOutput

@app.route("/source/tags/<int:source_id>", methods=["GET"])
def getSourceTags(source_id):
	strOutput = ""

	for strToken in CSourceManager.getSourcePOS(source_id):
		strOutput += str(strToken)
		strOutput += "<br/>"

	return strOutput

@app.route("/source/<int:source_id>", methods=["GET"])
def getSource(source_id):
	strOutput = ""
	for strWord in CSourceManager.getSource(source_id):
		strOutput += str(strWord)
		strOutput += "<br/>"

	return strOutput

@app.route("/source/all")
def getFullSource():
	return Response(CSourceManager.getFullSource(), mimetype='text/html')

@app.route("/stats/concordance/<word>", methods=["GET"])
def getCorpusConcordance(word):
	strOutput = ""
	for strWord in CSourceManager.getSourceConcordance(word):
		strOutput += str(strWord)
		strOutput += "<br/>"

	return strOutput

@app.route("/stats/similar/<word>" , methods=["GET"])
def getCorpusSimilarity(word):
	strOutput = "" 
	for strWord in CSourceManager.getSourceSimilarity(word):
		strOutput += str(strWord)
		strOutput += "<br/>"

	return strOutput

if __name__ == "__main__":
	app.debug = True
	##CCorpusManager.loadTokens()

	app.run()