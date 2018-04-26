

import time, requests, sqlite3

ads_from_server = ["Ad 1", "Ad 2", "Ad 3"]
ads_from_disk = ["Old Ad 1", "Old Ad 2", "Old Ad 3"]

def main():
	create_db()
	return

	ads = []
	if (is_connected() and new_ads_available()):
		ads = download_ads()
	else:
		ads = load_ads_from_disk()

	display_ads(ads)

def create_db():
	print("test")
	connection = sqlite3.connect("testserver.db")
	global cursor
	cursor = connection.cursor()

def create_tables():
	
	with connection:

		sql = 'DROP TABLE persons'
		cursor.execute(sql)

		sql = "CREATE TABLE persons(id INT, firstName VARCHAR(255) NOT_NULL, lastName VARCHAR(255) NOT_NULL, email VARCHAR(255) NOT_NULL, passwordHash VARCHAR(255) NOT_NULL)"
		cursor.execute(sql)

		#sql = "CREATE TABLE IF NOT EXISTS admins(id INT PRIMARY KEY, firstName VARCHAR(255) NOT_NULL, lastName VARCHAR(255) NOT_NULL, email VARCHAR(255) NOT_NULL, passwordHash VARCHAR(255) NOT_NULL, FOREIGN KEY(id) REFERENCES persons(id), FOREIGN KEY(firstName) REFERENCES persons(firstName), FOREIGN KEY(lastName) REFERENCES persons(lastName), FOREIGN KEY(email) REFERENCES persons(email), FOREIGN KEY(passwordHash) REFERENCES persons(passwordHash) )"
		#cursor.execute(sql)

		#sql = "CREATE TABLE IF NOT EXISTS ads(id INT PRIMARY KEY, text TEXT NOT_NULL)"
		#cursor.execute(sql)	

	
		cursor.execute('INSERT INTO persons VALUES (1, "Nicolas", "Boxhammer", "ab@cd.ef", 12345)')
		connection.commit()
		try:
			cursor = connection.cursor()
			cursor.execute("select * from persons")
			data = cursor.fetchone()
			print(data)
		except sqlite3.Error as e:
			print ('entry_get_id() Error %s:' + str(e.args[0]))
			connection.close()
			sys.exit(1)
		return data 
	
		#number_of_rows = cursor.execute("select * from persons")
		#result = cursor.fetchall()	 
		#print(result[0])
		#connection.close()

#def add_ads():
	#cursor.execute('INSERT INTO ads(id, text) VALUES (0, "DB Ad 1"), (1, "DB Ad 2"), (2, "DB Ad 3");')

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
