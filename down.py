import urllib.request
from selenium import webdriver

def func(link): 	

#	link = "https://en.savefrom.net/#url=http://youtube.com/watch?v=89lQ5k5F_hM&list=RDMM89lQ5k5F_hM&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com"
	try:
		driver = webdriver.PhantomJS()
		driver.get(link)
		name = driver.find_element_by_xpath('//div[@class="row title"]')
		name =name.text + '.mp4'
		d_link = driver.find_element_by_xpath('//a[@class="link link-download subname ga_track_events download-icon"]')
		urllib.request.urlretrieve(d_link.get_attribute('href'), name)
		driver.close()
		return True
		
	except:
		driver.close()
		return False

def downlode(link):
	
	var = func(link)
	if var == True :
	   print("Downloding succesfull")
	else:
	   print("Downloding Failed")   





