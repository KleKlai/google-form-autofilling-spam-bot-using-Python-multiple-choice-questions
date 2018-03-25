import time
import random
from selenium import webdriver

chromedriver = "location of your chrome driver application"
driver = webdriver.Chrome(chromedriver)

link = 'google form link here'
driver.get(link)

xps = 'starting of the XPath'
xpm = 'middle of the XPath'
xpe = 'ending of the XPath'
submit_xp = 'XPath of submit button'
another_xp = 'XPath of submit_another_response'
maxnum = [2,5,3,4,2,2,3]  #number of choice for each questions

num_ans = []
for i in range(0, len(maxnum)):
	num_ans.append(random.randint(1,maxnum[i]))


nqT = len(maxnum)
while(1):
	for i in range(1,nqT+1):
		x_p = xps +str(i)+xpm + str(num_ans[i-1]) + xpe
		print(x_p)  #optional
		d = driver.find_element_by_xpath(x_p)
		d.click()
		#time.sleep(random.randint(1,2))
		#change the speed of clicking by reducing sleep time
		time.sleep(0.5)
	
	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(random.randint(1,3))
	
	r = driver.find_element_by_xpath(another_xp)
	r.click()
