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
	kategorie TEXT,
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
#


conn.commit()
conn.close()
