from datetime import datetime as dt
from json import load
import requests


def getResume():
	with open("../resume.json") as f:
		resume = load(f)
	return resume

def main():
	URL = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

	resume = getResume()

	try:
		response = requests.post(url=URL, data=resume)
		if response.status_code == 200:
			print("Okay")
	except:
		print("error")
		print(response.status_code)
		print(response.reason)
	finally:
		print(resume)
		

if __name__ == '__main__':
	main()
