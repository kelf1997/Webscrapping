from bs4 import BeautifulSoup
import re
import requests
import csv
import urllib.request as ur

#years = ['2004']
years = ['2002', '2004', '2006', '2008', '2009', '2011', '2013', '2014', '2015', '2017', '2018']
url = []
for year in years:
	url.append('http://www.piano-e-competition.com/midi_'+year+'.asp')

regex = re.compile('/MIDIFiles/')



f = csv.writer(open('mididata.csv', 'w'))
f.writerow(['filename', 'composer', 'year', 'title'])



def scraping(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	
	for table in soup.find_all('table', attrs={'class':'detail-text'}):
		for tr in table.find_all('tr'):
			try:
				if tr.find_all('td')[1].find('a'):
				#if tr.find_all('td')[1].find('a', attrs={'href':re.compile('MIDIFiles')}):			
					link = tr.find_all('td')[1].find('a').get('href')
					year = url[-8:-4]
					filename = link.split('/')[-1]
					title = tr.find_all('td')[1].text
					composer = tr.find_all('td')[0].text
					print(filename, composer, year, title)
					downloadfile = ur.URLopener()
					downloadfile.retrieve('http://www.piano-e-competition.com'+link, filename)
					f.writerow([filename, composer, year, title])
			except:
				continue

for i in url:
	#print(i)
	scraping(i)


#contents = soup.find_all('a', attrs={'href': re.compile(r'MID$')})
#for tr in table.find_all('tr'):




"""
url = 'http://www.piano-e-competition.com/MIDIFiles/2011/Kurz01.MID'

image_name = 'test3.jpg'
testfile = ur.URLopener()
testfile.retrieve(url, image_name)
"""
