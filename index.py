from flask import Flask, jsonify ,request, abort
import CKeywordManager
import CSourceManager
from nltk.corpus import brown

app = Flask(__name__)

def validateJson(pObjRequest):
	if(not pObjRequest.json):
		abort(400)

@app.route("/", methods=["GET"])
def index():
	strOutput = ""
	for strWord in brown.words():
		strOutput += strWord
		strOutput += " , "

	return strOutput

@app.route("/keywords", methods=["GET"])
def getKeywords():
	lstKeywords = CKeywordManager.getAllKeywords()
	return jsonify({ "keywords":lstKeywords})

@app.route("/source" , methods=["POST"])
def addSource():
	validateJson(request)

	strUri = CSourceManager.addNewSource(request.json)

	if strUri == None:
		abort(503)

	return jsonify({"insert-uri":strUri}) , 201

@app.route("/source/<int:source_id>", methods=["GET"])
def getSource(source_id):
	return "hello"

if __name__ == "__main__":
	app.debug = True
	app.run()