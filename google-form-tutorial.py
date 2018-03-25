import time
import random
from selenium import webdriver

chromedriver = "C:/Users/User/Desktop/selenium tutorial/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chromedriver)

link = 'https://docs.google.com/forms/d/1wb9KmfOmXQLsCQ1qgGMBNO7RfnJg_Q6fpBT2_W6SkS4/viewform?edit_requested=true'
driver.get(link)

xps = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div['
xpm = ']/div[2]/div/content/div/label['
xpe = ']/div/div[1]/div[3]/div'
submit_xp = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div/content/span'
another_xp = '/html/body/div/div[2]/div[1]/div[2]/div[3]/a'
maxnum = [2,5,3,4,2,2,3]

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
		time.sleep(0.5)
	
	submit = driver.find_element_by_xpath(submit_xp)
	submit.click()
	time.sleep(random.randint(1,3))
	
	r = driver.find_element_by_xpath(another_xp)
	r.click()
	

