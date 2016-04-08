import os
import json

v=os.getenv('VCAP_SERVICES')
if v is None:
	data=json.load(open('credentials.json'));
else:
	data=json.loads(v);
watson_url=data['tone_analyzer'][0]['credentials']['url']
watson_username=data['tone_analyzer'][0]['credentials']['username']
watson_password=data['tone_analyzer'][0]['credentials']['password']
twitter_url=data['twitterinsights'][0]['credentials']['url']
cloudant_username=data['cloudantNoSQLDB'][0]['credentials']['username']
cloudant_password=data['cloudantNoSQLDB'][0]['credentials']['password']
