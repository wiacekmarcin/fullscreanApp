import sqlite3

conn = sqlite3.connect('/home/marcin/kredyty.sqlite')

cur = conn.cursor()
rest = 121212.12
stopa = 10.26
rata = 1500.58
b = (2018, 10)
e = (2028, 10)
for i in range((b[0]-2000)*12+b[1],(e[0]-2000)*12+e[1]):
	ods = rest*stopa/1200
	kap = rata - ods
	print("%d %0.2f %0.2f %0.2f" % (i, rest, ods, kap))
	cur.execute('INSERT INTO "raty" VALUES (NULL,8,%d, \'%0.2f\', \'%0.2f\', \'%0.2f\');' %(i, kap, ods, rest))
	rest -= kap
#cur.execute('SELECT * from raty')
#print(cur.fetchall())
conn.commit()
