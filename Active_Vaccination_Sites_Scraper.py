from bs4 import BeautifulSoup
import requests 
import csv

csv_file= open('AVS_scrape.csv','w')

csv_writer = csv.writer(csv_file)

source = requests.get('https://sacoronavirus.co.za/active-vaccination-sites/').text

soup = BeautifulSoup(source, 'lxml')

categories = []

try:
	match = soup.find('thead')
	for heading in match.tr.find_all('th'):
		categories.append(heading.text)

except Exception as e:
	match = None

#length=len(categories)
print('')
csv_writer.writerow([categories[0],categories[1],categories[2],categories[3]])

try:
	match = soup.find('tbody',class_='row-hover')
except Exception as e:
	match = None

print('Active Vaccination Sites')
print('as of 11th June 2021')
print(" ")

for site in match.find_all('tr'):
	try:
		province = site.find('td',class_='column-1').text
	except Exception as e:
		province = None

	try:
		district= site.find('td',class_='column-2').text
	except Exception as e:
		district=None

	try:
		facility= site.find('td',class_='column-3').text
	except Exception as e:
		facility= None 

	try:
		sector= site.find('td',class_='column-4').text
	except Exception as e:
		sector =None

	csv_writer.writerow([province,district,facility,sector])

	print ('Province: '+ province )
	print ('District: '+ district)
	print ('Facility: '+ facility)
	print ('Sector: '+ sector)
	
csv_file.close()
####################################################################################################################
print(" ")

csv_file= open('Stats.csv','w')

csv_writer = csv.writer(csv_file)
source = requests.get('https://sacoronavirus.co.za/').text

soup = BeautifulSoup(source, 'lxml')

match = soup.find('div',class_='fusion-counters-box counters-box row fusion-clearfix fusion-columns-5')

for data in match.find_all('div',class_='fusion-counter-box fusion-column col-counter-box counter-box-wrapper col-lg-2 col-md-2 col-sm-2 fusion-counter-box-icon-top'):

	try:
		stat = data.find('div',class_='counter-box-content').text
	except Exception as e:
		stat = None

	try:
		number = data.find('span',class_='display-counter')['data-value']
		stat2 = str(number)
	except Exception as e:
		stat2 = None

	csv_writer.writerow([stat, stat2])
	
	print (stat)
	print (stat2)

csv_file.close()
#####################################################################

source = requests.get('https://coronavirus.westerncape.gov.za/covid-19-dashboard').text

soup = BeautifulSoup(source, 'lxml')

try:
	body = soup.find('div',class_='field-item even')

	disclaimer = body.em.text

	pass
except Exception as e:
	disclaimer = None

print(disclaimer)






