#-*- encoding : utf-8 -*-
import sys, os
import datetime
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor
from dateutil.relativedelta import relativedelta

kredyty = [
	('Santander',  148.52, (2024, 10), 1000),
	('mbank',  494.77, (2030, 4), 1000),
	('Agricol 1', 469.78, (2027, 2), 1000),
	('Agricol 2', 303.99, (2028, 7), 1000),
	('Agricol 3', 310.73, (2025, 5), 1000),
	('Millenium', 700.00, (2027, 5), 1000),
	('Pekao S.A 1', 1100.00, (2023, 12), 1000),
	('Pekao S.A 2', 1500.00, (2027, 12), 1000)
]

kredyty.sort(key=lambda x : 12*x[2][0]+x[2][1])
print(kredyty)
	

#fontpath = '/home/marcin/git.devel.marcin/fulscreanapp/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
fontpath = '/home/pi/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
font = ImageFont.truetype(fontpath, 14)
font8 = ImageFont.truetype(fontpath,  8)

def createBackground():
	
	maxM = 100
	ddact = datetime.date.today()
	wm = 5
	wh = 10
	width = 100+maxM*wm
	height = 16 + (len(kredyty)+1)*wh
	
	margin = 140
	
	im = Image.new("RGB", (width, height), color="black")
	draw = ImageDraw.Draw(im)
	
	suma = 0.0
	for h in range(len(kredyty)):
		opis, kwota, _, _ = kredyty[h]
		draw.text((0, 16+h*wh), "%s - %.2f" % (opis, kwota), font = font8, fill="white")
		suma += kwota 
	draw.text((0, 16+len(kredyty)*wh), "Razem - %.2f" % (suma), font = font8, fill="white")
	
	for mon in range(maxM):
		dd = ddact + relativedelta(months=mon)
		m = dd.month
		y = dd.year
		print(y, m)
		if m == 1:
			draw.text((margin+mon*wm, 0), "%d" % y, font = font, fill="white")
			
		for h in range(len(kredyty)):
			opis, kwota, k, all = kredyty[h]
			if k[0]*12+k[1] >= y*12+m:
				draw.rectangle((margin+mon*wm+1, h*wh+16+1, margin+mon*wm+4, h*wh+16+wh-1), fill="gray", outline="gray")
			if k[0]*12+k[1] == y*12+m:
				draw.text((margin+mon*wm+5, 16+h*wh), "%.2f" % all, font = font8, fill="white")
	fpath = '/tmp/kredyty_%d_%02d.png' % (ddact.year, ddact.month)
	im.save(fpath)
createBackground()
