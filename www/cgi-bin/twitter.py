import credentials,json
import requests

SIZE=100;
API=credentials.twitter_url+"/api/v1/messages/search?size="+str(SIZE)+"&q=";
def search(keyword):
	url=API+keyword
	j=requests.get(url).json();
	output_string=""
	for tweet in j["tweets"]:
		if tweet["message"]["twitter_lang"] == "en" and tweet["message"]["verb"] == "post":
			#tweet["message"]["postedTime"]
			#tweet["message"]["body"]
			output_string+=(tweet["message"]["body"]+u"\n")
	return output_string
