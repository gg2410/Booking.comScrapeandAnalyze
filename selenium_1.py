import imp
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd



os.environ['PATH'] += r"C:\Python39\chromedriver_win32"
driver = webdriver.Chrome()
 
driver.get('https://www.booking.com/hotel/my/the-kuala-lumpur-journal.html?label=gen173nr-1DCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AojHsJMGwAIB0gIkMGYzZmUzMTEtY2MwMy00NzUzLWI1MTUtZTRkZmI1OGE0ZTQy2AIE4AIB&sid=020a420ffcb880f536c59adfe668777f&aid=304142&ucfs=1&arphpl=1&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=107&sr_order=popularity&srpvid=20ab01c0d4c201bb&srepoch=1651283306&from_sustainable_property_sr=1&from=searchresults#hotelTmpl')

#Get the Name
driver.implicitly_wait(30)
name = driver.find_element(by=By.CLASS_NAME, value="hp__hotel-name")
name_list = [name.text] * 100

#Open Review Tab
driver.find_element(by=By.ID, value="show_reviews_tab").click()


#Choosing English Language Filter
driver.implicitly_wait(30)
time.sleep(5)
driver.find_element(by=By.ID, value="review_lang_filter").click()
driver.find_element(by=By.XPATH, value='//*[@id="review_lang_filter"]/div/div/ul/li[2]/button').click()


#Sorting By New
driver.implicitly_wait(30)
time.sleep(5)
select = Select(driver.find_element(by=By.ID, value='review_sort'))
select.select_by_index(1)

list_of_comment_ratings = []
list_of_comments = []
while len(list_of_comments) < 100 :
    time.sleep(5)
    driver.implicitly_wait(5)
    review_text = driver.find_elements(by=By.CLASS_NAME, value='c-review__title--ltr')
    for t in review_text:
        list_of_comments.append(t.text)
    
    time.sleep(5)
    driver.implicitly_wait(5)
    review_ratings = driver.find_elements(by=By.CLASS_NAME, value='c-score')
    for i in review_ratings:
        list_of_comment_ratings.append(i.text)


    driver.find_element(by=By.CLASS_NAME, value="pagenext").click()

csv_bangkok_dict = {'Comment_Text': list_of_comments, 'Name': name_list , 'Rating': list_of_comment_ratings}
data = pd.DataFrame(csv_bangkok_dict)
data.to_csv('Kuala_Lumpur.csv', mode='a')
