import sqlite3

conn = sqlite3.connect('/home/marcin/kredyty.sqlite')

cur = conn.cursor()
rest = 4752.44
for i in range(265,297):
	print(i, rest)
	cur.execute('INSERT INTO "raty" VALUES (NULL,1,%d, \'148,52\', \'0,00\', \'%0.2f\');' %(i, rest))
	rest -= 148.52
cur.execute('SELECT * from raty')
print(cur.fetchall())
conn.commit()
