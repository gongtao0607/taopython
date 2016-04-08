import credentials
import requests
from requests.auth import HTTPBasicAuth

API=credentials.watson_url+"/v3/tone?version=2016-02-11&sentences=false"
USERNAME=credentials.watson_username
PASSWORD=credentials.watson_password
def analyze(content):
	url = API
	data = {"body": content}
	headers = {'Content-Type': 'text/plain'}
	auth = HTTPBasicAuth(USERNAME, PASSWORD)
	j=requests.post(url,data=data,headers=headers,auth=auth).json()
	result=[]
	for cat in j["document_tone"]["tone_categories"]:
		for tone in cat["tones"]:
			result.append({"tone": tone["tone_name"], "score": tone["score"]})
	return result

