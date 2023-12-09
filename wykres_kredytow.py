#-*- encoding : utf-8 -*-
import sys, os
import datetime
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor
from dateutil.relativedelta import relativedelta

import mysql.connector

def countL(y, m):
	return y*12+m

def textlength(draw, str, font):
	return draw.textsize(str, font)[0]

cnx = mysql.connector.connect(user='kredyty', password='kredyty',
                              host='192.168.10.254',
                              database='kredyty')
kredyty = []
maxMonth = 0
if cnx and cnx.is_connected():
	with cnx.cursor() as cursor:
		ddact = datetime.date.today()
		liczba = countL(ddact.year-2000, ddact.month)

		sql='SELECT * FROM `RataWidok` WHERE data = %d' % liczba
		print(sql)
		cursor.execute(sql)

		for k in cursor.fetchall():
			print(k)
			kred = {}
			kred['opis'] = k[5]
			kred['wys_raty'] = k[8]
			kred['koniec'] = k[10]
			kred['poczatek'] = k[9]
			kred['wolumen'] = k[6]
			kred['dzien'] = k[7]
			kred['stopa'] = k[11]
			kred['nr_raty'] = k[12]
			kred['poz_rat'] = k[13]
			kred['rata_ods'] = k[3]
			kred['rata_kap'] = k[2]
			kred['do_splacenia'] = k[4]
			if maxMonth < kred['koniec']:
				maxMonth = kred['koniec'] 
			kredyty.append(kred)

		
maxMonth += 6
kredyty.sort(key=lambda x : x['stopa']*x['do_splacenia'])
print(kredyty)
#sys.exit(0)

#fontpath = '/home/marcin/git.devel.marcin/fulscreanapp/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
fontpath = '/home/pi/fullscreanApp/fonts/robotic/Roboto-Regular.ttf'
font = ImageFont.truetype(fontpath, 14)
font8 = ImageFont.truetype(fontpath,  10)

def createBackground():
	
	
	ddact = datetime.date.today()
	print(maxMonth)
	print(ddact.year)
	print(ddact.month)
	maxM = maxMonth - 12* (ddact.year -2000) - ddact.month
	print(maxM)
	wm = 5
	wh = 12
	width = 330+maxM*wm
	height = 16 + (len(kredyty)+1)*wh
	
	margin = 130
	
	im = Image.new("L", (width, height), color="black")
	draw = ImageDraw.Draw(im)
	
	sumaRat = 0.0
	sumaKredytow = 0.0
	sumaPozostalo = 0.0
	sumaOdsetek = 0.0
	
	max_opis = 0
	max_dzien = 0
	max_kwota_raty = 0
	max_odsetki = 0
	max_zostalo_kwota = 0
	max_wolumen = 0
	sum_kwota_raty = 0
	sum_odsetki = 0
	sum_zostalo = 0
	sum_wolumen = 0
	for k in kredyty:
		to = textlength(draw, "%s" % k['opis'], font=font8)
		if to > max_opis : max_opis = to
		
		td = textlength(draw, "%d" % k['dzien'], font=font8)
		if td > max_dzien : max_dzien = td
		
		tk = textlength(draw, "%0.2f" % k['wys_raty'], font=font8)
		if tk > max_kwota_raty : max_kwota_raty = tk
		sum_kwota_raty += k['wys_raty']
		
		tk = textlength(draw, "%0.2f" % k['rata_ods'], font=font8)
		if tk > max_odsetki : max_odsetki = tk
		sum_odsetki +=  k['rata_ods']
		
		tk = textlength(draw, "%0.2f" % k['do_splacenia'], font=font8)
		if tk > max_zostalo_kwota : max_zostalo_kwota = tk
		sum_zostalo += k['do_splacenia']
		
		tk = textlength(draw, "%0.2f" % k['wolumen'], font=font8)
		if tk > max_wolumen : max_wolumen = tk
		sum_wolumen += k['wolumen']
	
	tk = textlength(draw, "%0.2f" % sum_kwota_raty, font=font8)
	if tk > max_kwota_raty : max_kwota_raty = tk
		
	tk = textlength(draw, "%0.2f" % sum_odsetki, font=font8)
	if tk > max_odsetki : max_odsetki = tk
	
	tk = textlength(draw, "%0.2f" % sum_zostalo, font=font8)
	if tk > max_zostalo_kwota : max_zostalo_kwota = tk
		
	tk = textlength(draw, "%0.2f" % sum_wolumen, font=font8)
	if tk > max_wolumen : max_wolumen = tk
	
	draw.text((0, 0), u"Opis", font = font8, fill="white")
	draw.text((max_opis+max_dzien+5-textlength(draw,"Dz",font=font8),0), u"Dz", font = font8, fill="white")
	draw.text((max_opis+max_dzien+max_kwota_raty+10-textlength(draw,"Rata",font=font8), 0), u"Rata", font = font8, fill="white")
	draw.text((max_opis+max_dzien+max_kwota_raty+max_odsetki+15-textlength(draw,"Odset.",font=font8), 0), u"Odset.", font = font8, fill="white")
	#draw.text((max_opis + max_dzien + max_kwota_raty + max_odsetki + 20, 0), u"Miesieczne raty", font = font8, fill="white")
	margin = max_opis + max_dzien + max_kwota_raty + max_odsetki + 20
	draw.text((width-max_wolumen-5, 0), u"Wolumen", font = font8, fill="white")
	draw.text((width-max_wolumen-max_zostalo_kwota-10, 0), u"Zostalo", font = font8, fill="white")
		
	for h in range(len(kredyty)):
		opis = kredyty[h]['opis']
		kwota_raty = kredyty[h]['wys_raty']
		cala_kwota = kredyty[h]['wolumen']
		odsetki = kredyty[h]['rata_ods']
		zostala_kwota = kredyty[h]['do_splacenia']
		dzien = kredyty[h]['dzien']

		draw.text((0, 16+h*wh), "%s" % (opis), font = font8, fill="white")
		
		tl = textlength(draw, "%d" % dzien, font=font8)
		draw.text((max_opis+max_dzien+10-tl, 16+h*wh), "%d" % dzien, font=font8, fill="white")
		
		tl = textlength(draw, "%0.2f" % kwota_raty, font=font8)
		draw.text((max_opis+max_dzien+max_kwota_raty+15-tl, 16+h*wh), " %.2f " % kwota_raty, font=font8, fill="white")

		tl = textlength(draw, "%0.2f" % odsetki, font=font8)
		draw.text((max_opis+max_dzien+max_kwota_raty+max_odsetki+20-tl, 16+h*wh), "%0.2f" % odsetki, font=font8, fill="white")
		
		tl = textlength(draw, "%.2f" % cala_kwota, font=font8)
		draw.text((width-tl, 16+h*wh), "%.2f" % cala_kwota, font=font8, fill="white")
		
		tl = textlength(draw, "%0.2f" % zostala_kwota, font=font8)
		draw.text((width-max_wolumen-5-tl, 16+h*wh), " %.2f " % zostala_kwota, font=font8, fill="white")
		
		sumaRat += kwota_raty 
		sumaKredytow += cala_kwota
		sumaOdsetek += odsetki
		sumaPozostalo += zostala_kwota

	draw.text((0, 16+len(kredyty)*wh), u"Razem", font = font8, fill="white")

	if sumaKredytow > 0:
		
		tl = textlength(draw, "%0.2f" % sumaRat, font=font8)
		draw.text((max_opis+max_dzien+max_kwota_raty+15-tl, 16+len(kredyty)*wh), " %.2f " % sumaRat, font=font8, fill="white")

		tl = textlength(draw, "%0.2f" % sumaOdsetek, font=font8)
		draw.text((max_opis+max_dzien+max_kwota_raty+max_odsetki+20-tl, 16+len(kredyty)*wh), "%0.2f" % sumaOdsetek, font=font8, fill="white")
		
		tl = textlength(draw, "%.2f" % sumaKredytow, font=font8)
		draw.text((width-tl, 16+len(kredyty)*wh), "%.2f" % sumaKredytow, font=font8, fill="white")
		
		tl = textlength(draw, "%0.2f" % sumaPozostalo, font=font8)
		draw.text((width-max_wolumen-5-tl, 16+len(kredyty)*wh), " %.2f " % sumaPozostalo, font=font8, fill="white")
		
	for mon in range(maxM):
		dd = ddact + relativedelta(months=mon)
		m = dd.month
		y = dd.year-2000
		#print(y, m)
		if m == 1:
			draw.text((margin+mon*wm, 0), "%d" % y, font = font, fill="white")
			
		for h in range(len(kredyty)):
			ilosc_rat_przeszlych = kredyty[h]['nr_raty']
			ilosc_rat_przyszlych = kredyty[h]['poz_rat']
			ilosc_rat_wszystkich = ilosc_rat_przeszlych + ilosc_rat_przyszlych
			k = kredyty[h]['koniec']
			if k > y*12+m:
				draw.rectangle((margin+mon*wm+1, h*wh+16+1, margin+mon*wm+4, h*wh+16+wh-1), fill="gray", outline="gray")
			if k == y*12+m:
				draw.text((margin+mon*wm+5, 16+h*wh), "Rata %d z %d" % (ilosc_rat_przeszlych, ilosc_rat_przeszlych + ilosc_rat_przyszlych), font = font8, fill="white")
				#tl = textlength(draw, "%.2f / %.2f" % (cala_kwota-zostala_kwota, cala_kwota), font = font8)
				#draw.text((width-tl, 16+h*wh), "%.2f / %.2f" % (cala_kwota-zostala_kwota, cala_kwota), font = font8, fill="white")
	
	fpath = '/home/pi/tmp/kredyty_%d_%02d.png' % (ddact.year, ddact.month)
	im.show()
	print(im.size)
	im.save(fpath)
createBackground()
