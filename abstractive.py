# 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
# MediaConcise: Effortless Content Recaps
import requests
import extractive as ex

def abstract(text):
	if(len(text)>5000):
		text=ex.extract(text)
	API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
	headers = {"Authorization": "Bearer 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"}

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()
	
	output = query({
		"inputs": text,
	})[0]
	result=output["summary_text"]
	return result