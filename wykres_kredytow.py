#-*- encoding : utf-8 -*-
import sys, os
import datetime
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor
from dateutil.relativedelta import relativedelta

def countL(y, m):
	return y*12+m

def textlength(draw, str, font):
	return draw.textsize(str, font)[0]

def wylicz_pozostala_kwota(kwota, stopa, rata, ilosc_rat, rat_do_konca):
	sumazob=kwota
	r = ilosc_rat
	while r != rat_do_konca:
		odsetki = sumazob*stopa/1200
		splkap = rata-odsetki
		sumazob = sumazob-splkap
		r-=1
	return sumazob

dane_kredytow = [
	('Santander 0%',  148.52, (2024, 10), (2019, 10), 8911, 0),
	('mbank 13.35%',  494.77, (2030, 4), (2023, 4), 26900, 13.35),
	('Agricol 7.2%', 469.78, (2027, 2), (2021, 2), 27400, 7.2),
	('Agricol 7.2%', 303.99, (2028, 7), (2021, 7), 20000, 7.2),
	('Agricol 0%', 310.73, (2025, 5), (2021, 1), 12429, 0),
	('Millenium 6.7%', 694.02, (2028, 3	), (2020, 3), 51466.14, 6.7),
	('Pekao S.A 10.8%', 1141.02, (2024, 1), (2017, 1), 97043.80, 10.76),
	('Pekao S.A 10.3%', 1500.58, (2028, 10), (2018, 10), 121212.12, 10.26),
]

ddact = datetime.date.today()
liczba = countL(ddact.year, ddact.month)

kredyty = []
for kr in dane_kredytow:
	kredyt = [kr[0], kr[1], kr[2], kr[3], kr[4], kr[5]]
	nr_rest = countL(kr[2][0], kr[2][1]) - liczba
	nr_raty = liczba - countL(kr[3][0], kr[3][1])
	if nr_rest < 0:
		continue
	kredyt.append(nr_raty)
	kredyt.append(nr_rest)
	kredyt.append(wylicz_pozostala_kwota(kr[4], kr[5], kr[1], nr_raty+nr_rest, nr_rest))
	kredyty.append(kredyt)


kredyty.sort(key=lambda x : countL(x[2][0],x[2][1]))
	

#fontpath = '/home/marcin/git.devel.marcin/fulscreanapp/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
fontpath = '/home/pi/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
font = ImageFont.truetype(fontpath, 14)
font8 = ImageFont.truetype(fontpath,  10)

def createBackground():
	
	maxM = 100
	ddact = datetime.date.today()
	wm = 5
	wh = 12
	width = 230+maxM*wm
	height = 16 + (len(kredyty)+1)*wh
	
	margin = 140
	
	im = Image.new("L", (width, height), color="black")
	draw = ImageDraw.Draw(im)
	
	sumaRat = 0.0
	sumaKredytow = 0.0
	sumaPozostalo = 0.0
	for h in range(len(kredyty)):
		opis, kwota, _, _, cala_kwota, _, _, _, zostala_kwota = kredyty[h]
		draw.text((0, 16+h*wh), "%s" % (opis), font = font8, fill="white")
		tl = textlength(draw, " %.2f " % kwota, font=font8)
		draw.text((margin-5-tl, 16+h*wh), " %.2f " % kwota, font=font8, fill="white")
		
		tl = textlength(draw, " %.2f " % (cala_kwota-zostala_kwota), font=font8)
		draw.text((width-65-tl, 16+h*wh), " %.2f " % (cala_kwota-zostala_kwota), font=font8, fill="white")
		
		tl = textlength(draw, " %.2f " % cala_kwota, font=font8)
		draw.text((width-5-tl, 16+h*wh), " %.2f " % cala_kwota, font=font8, fill="white")
		
		sumaRat += kwota 
		sumaKredytow += cala_kwota
		sumaPozostalo += zostala_kwota

	draw.text((0, 16+len(kredyty)*wh), u"Razem", font = font8, fill="white")
	if sumaKredytow > 0:
		tl = textlength(draw, " %.2f " % sumaRat, font=font8)
		draw.text((margin-5-tl, 16+len(kredyty)*wh), u" %.2f " % sumaRat, font = font8, fill="white")
		#draw.text((margin+15, 16+len(kredyty)*wh), u"Zostalo do splacenia %.2f z %.2f (%.0f %%)" % (sumaPozostalo, sumaKredytow, 100*sumaPozostalo/sumaKredytow), font = font8, fill="white")
		
		tl = textlength(draw, " %.2f " % (sumaKredytow-sumaPozostalo), font=font8)
		draw.text((width-65-tl, 16+len(kredyty)*wh), " %.2f " % (sumaKredytow-sumaPozostalo), font=font8, fill="white")
		
		tl = textlength(draw, " %.2f " % sumaKredytow, font=font8)
		draw.text((width-5-tl, 16+len(kredyty)*wh), " %.2f " % sumaKredytow, font=font8, fill="white")
		
	for mon in range(maxM):
		dd = ddact + relativedelta(months=mon)
		m = dd.month
		y = dd.year
		#print(y, m)
		if m == 1:
			draw.text((margin+mon*wm, 0), "%d" % y, font = font, fill="white")
			
		for h in range(len(kredyty)):
			opis, kwota, k, _, cala_kwota, _, _, _, zostala_kwota = kredyty[h]
			if k[0]*12+k[1] >= y*12+m:
				draw.rectangle((margin+mon*wm+1, h*wh+16+1, margin+mon*wm+4, h*wh+16+wh-1), fill="gray", outline="gray")
			if k[0]*12+k[1] == y*12+m:
				draw.text((margin+mon*wm+5, 16+h*wh), "%.0f %% (%0.2f)" % (100*(cala_kwota-zostala_kwota)/cala_kwota,zostala_kwota), font = font8, fill="white")
				#tl = textlength(draw, "%.2f / %.2f" % (cala_kwota-zostala_kwota, cala_kwota), font = font8)
				#draw.text((width-tl, 16+h*wh), "%.2f / %.2f" % (cala_kwota-zostala_kwota, cala_kwota), font = font8, fill="white")
	
	fpath = '/home/pi/tmp/kredyty_%d_%02d.png' % (ddact.year, ddact.month)
	#im.show()
	im.save(fpath)
createBackground()
