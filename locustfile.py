from locust import Locust, TaskSet, task
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        driver = webdriver.Chrome()
        driver.get("https://en.wikipedia.org/wiki/Special:Random")
        header=[]
        body=[]
        content = driver.page_source
        soup = BeautifulSoup(content)
        for div in soup.find('div', ref=True, attrs={'class':'mw-body'}):
            header=div.find('div', attrs={'id':'firstHeading'})
            body=div.find('div', attrs={'id':'mw-content-text'})
        df = pd.DataFrame({'Header': header, 'Body': body})
        df.to_csv('wikiScrap.csv', index=False, encoding='utf-8')

#This hella doesn't work in this state, but is close. Will use the locust to hit UI. my Python-fu is biggest hold up.
class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000