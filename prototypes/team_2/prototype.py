import time, requests

ads_from_server = ["Ad 1", "Ad 2", "Ad 3"]
ads_from_disk = ["Old Ad 1", "Old Ad 2", "Old Ad 3"]

def main():
	ads = []
	if (is_connected() and new_ads_available()):
		ads = download_ads()
	else:
		ads = load_ads_from_disk()

	display_ads(ads)

def display_ads(ads):
	while(True):
		for ad in ads:
			print(ad)
			time.sleep(1)
	
def is_connected():
	try:
		requests.get('https://www.google.com/', timeout=2)
		return True
	except:
		return False

def new_ads_available():
	return True

def download_ads():
	return ads_from_server

def load_ads_from_disk():
	return ads_from_disk

main()
