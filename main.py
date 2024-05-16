from selenium import webdriver											#import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import time																#import time
try:
	a=0																	#while loop
	while a!=1:															#while loop condition
		options = EdgeOptions()
		options.add_experimental_option('excludeSwitches', ['enable-logging'])
		driver = webdriver.Edge(options=options)
		#driver = webdriver.Edge()
		#driver.get('https://bing.com')
		print("Wait ...")												#print wait
		for i in range(1,100):
			#options.add_experimental_option('excludeSwitches', ['enable-logging'])
			driver.get('https://bing.com')								#bing opens
			element = driver.find_element(By.ID, 'sb_form_q')
			element.send_keys(str(i))
			element.submit()
			print("Sucess attempt ",i,"\n")
			time.sleep(5)
		
except:
	print("error try again")
