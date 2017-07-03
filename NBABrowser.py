from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

player_first = "Lebron"
player_last = "James"
start = 2016
end = 2017
f = open(player_first + player_last + "Stats.txt","w")
while True:
	driver = webdriver.Chrome()
	driver.get("http://stats.nba.com/players/gamelogs/#!?Season=" + str(start) + '-' + str(str(end)[-2:]) + "&SeasonType=Regular%20Season&CF=PLAYER_NAME*E*" + player_first + "%20" + player_last)
	try:
		load_more = driver.find_element_by_class_name("table-addrows__button")
		load_more.click()
	except NoSuchElementException:
		print("Cannot keep doing this")
		driver.quit()
	f = open(player_first + player_last + "Stats.txt","a")
	f.write(str(driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div[1]/table").text.split()))
	start -= 1
	end -= 1
	if start < 2002:
		break