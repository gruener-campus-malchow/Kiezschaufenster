import time, requests
import tkinter as tk

ads_from_server = ["Ad 1", "Ad 2", "Ad 3"]
ads_from_disk = ["Old Ad 1", "Old Ad 2", "Old Ad 3"]

class Window(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		master.attributes("-fullscreen", True)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.text = tk.Label(self, text="Hi", font="Arial 24")
		self.text.pack()

def test():
	print("test")

def main():
	root = tk.Tk()
	window = Window(master=root)

	ads = []
	if (is_connected() and new_ads_available()):
		ads = download_ads()
	else:
		ads = load_ads_from_disk()

	display_ads(window, ads)
	window.mainloop()

ad_index = 0
def display_ads(window, ads):
	def test():
		global ad_index
		ad_index+=1	

		if ad_index > len(ads):
			ad_index = 1	

		window.text.config(text=ads[ad_index-1])
		window.text.after(1000, test)	
	window.text.after(1000, test)
		

#	window.after(1000, display_ads)
#	for ad in ads:
#		print(ad)
#		time.sleep(1)
	
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
