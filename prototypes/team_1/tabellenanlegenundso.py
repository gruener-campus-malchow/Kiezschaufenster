#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('baba.db')
c = conn.cursor()

# ~~~ Tabellen anlegen ~~~
# Orte
c.execute(u'''CREATE TABLE IF NOT EXISTS Orte(
	stadt TEXT,
	land TEXT,
	straße TEXT,
	hausnummer TEXT,
	id INTEGER PRIMARY KEY,
	bezeichnung TEXT
)''')
# Werbebildschirme 
c.execute(u'''CREATE TABLE IF NOT EXISTS Werbebildschirme(
	breite INTEGER,
	höhe INTEGER,
	id INTEGER PRIMARY KEY,
	orte_id INTEGER,
	FOREIGN KEY(orte_id) REFERENCES Orte(id)
)''')
# Ränge
c.execute(u'''CREATE TABLE IF NOT EXISTS Ränge(
	id INTEGER PRIMARY KEY,
	bezeichnung TEXT,
	werbung_einstellen INTEGER,
	bildschirm_anlegen INTEGER
)''')
# Personen
c.execute(u'''CREATE TABLE IF NOT EXISTS Personen(
	vorname TEXT,
	nachname TEXT,
	passwort_hash TEXT,
	id INTEGER PRIMARY KEY,
	rang_id INTEGER,
	email TEXT,
	FOREIGN KEY(rang_id) REFERENCES Ränge(id)
)''')
# Werbungen
c.execute(u'''CREATE TABLE IF NOT EXISTS Werbungen(
	dauer FLOAT,
	min_breite INTEGER,
	max_breite INTEGER,
	min_länge INTEGER,
	max_länge INTEGER,
	kategorie INTEGER,
	id INTEGER PRIMARY KEY,
	url TEXT,
	autor_id INTEGER,
	FOREIGN KEY(autor_id) REFERENCES Personen(id)
)''')
# Werbung_auf_Bildschirm
c.execute(u'''CREATE TABLE IF NOT EXISTS Werbung_auf_Bildschirm(
	id INTEGER PRIMARY KEY,
	bildschirm_id INTEGER,
	werbung_id INTEGER,
	FOREIGN KEY(bildschirm_id) REFERENCES Werbebildschirme(id),
	FOREIGN KEY(werbung_id) REFERENCES Werbungen(id)
)''')
# Kategorie_zu_Bildschirm
c.execute(u'''CREATE TABLE IF NOT EXISTS Kategorie_zu_Bildschirm(
	id INTEGER PRIMARY KEY,
	bildschirm_id INTEGER,
	kategorie INTEGER,
	FOREIGN KEY(bildschirm_id) REFERENCES Werbebildschirme(id)
)''')

# ~~~ Beispielwerte einfügen ~~~

#Insert into Orte
c.execute('''INSERT INTO orte(stadt,land,straße,hausnummer,id,bezeichnung)
VALUES(:stadt,:land,:straße,:hausnummer,:id,:bezeichnung)''',
{'stadt':'Berlin', 'land':'Deutschland', 'straße':'Doberaner Straße', 'hausnummer':'55', 'id':1, 'bezeichnung':'Schule Gruener Campus Malchow' })

#Insert into Werbebildschirme
c.execute('''INSERT INTO Werbebildschirme(breite,höhe,id,orte_id)
VALUES(:breite,:höhe,:id,:orte_id)''',
{'breite':1980, 'höhe':1080, 'id':1, 'orte_id':1})

#Insert into Ränge
c.execute('''INSERT INTO Ränge(id,bezeichnung,werbung_einstellen,bildschirm_anlegen)
VALUES(:id,:bezeichnung,:werbung_einstellen,:bildschirm_anlegen)''',
{'id':1,'bezeichnung':'Installateur','werbung_einstellen':0,'bildschirm_anlegen':1})

#Insert into Personen
c.execute('''INSERT INTO Personen(vorname,nachname,passwort_hash,id,rang_id,email)
VALUES(:vorname,:nachname,:passwort_hash,:id,:rang_id,:email)''',
{'vorname':'Hans', 'nachname':'Heinrich', 'passwort_hash':'71834aadd787622', 'id':1, 'rang_id':1, 'email':'hans.heinrich777@gmail.com'})

#Insert into Werbungen
c.execute('''INSERT INTO Werbungen(dauer,min_breite,max_breite,min_länge,max_länge,kategorie,id,url,autor_id)
VALUES(:dauer,:min_breite,:max_breite,:min_länge,:max_länge,:kategorie,:id,:url,:autor_id)''',
{'dauer':120, 'min_breite':1980, 'max_breite':1980, 'min_länge':1080, 'max_länge':1080, 'kategorie':1, 'id':1, 'url':'ballsport.de', 'autor_id':1})

#Insert into Werbung_auf_Bildschirm
c.execute('''INSERT INTO Werbung_auf_Bildschirm(id,bildschirm_id,werbung_id)
VALUES(:id,:bildschirm_id,:werbung_id)''',
{'id':1, 'bildschirm_id':1, 'werbung_id':1})

#Insert into Kategorie_zu_Bildschirm
c.execute('''INSERT INTO Kategorie_zu_Bildschirm(id,bildschirm_id,kategorie)
VALUES(:id,:bildschirm_id,:kategorie)''',
{'id':1, 'bildschirm_id':1, 'kategorie':1})

conn.commit()
conn.close()
