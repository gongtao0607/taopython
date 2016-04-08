import credentials
import json
from cloudant.account import Cloudant
from cloudant.query import Query

USERNAME=credentials.cloudant_username
PASSWORD=credentials.cloudant_password
client = Cloudant(USERNAME, PASSWORD, account=USERNAME)
client.connect()
session = client.session()
db = client["taopython"]
db.create_index(fields=["query", "time"])

def store(query,time,content,analysis):
	doc=db.create_document({"query":query,"time":time,"content":content,"analysis":json.dumps(analysis)})
	return doc

def load(id):
	return db[id]

def search(query):
	resp=db.get_query_result(selector={"query":query},fields=["_id", "time"])
	#resp=db.get_query_result(selector={"query":query},fields=["_id", "time"],sort=["time"])
	return resp
