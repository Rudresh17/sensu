from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
import csv
import threading
import time,datetime
import urllib,urllib.request
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException,WebDriverException,UnexpectedAlertPresentException
from django.http import HttpResponse
from selenium import webdriver


def bar_code():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options,executable_path='E:\Rudy\Internships\Sensus\chromedriver.exe')
    #driver=webdriver.chrome("E:\Rudy\Internships\Sensus\chromedriver.exe")
    driver.get('https://web.whatsapp.com/')
    
    for i in range(0,3):
        image=""
        try:
            time.sleep(6)
            #image=driver.find_element_by_xpath("//div[@class='_2EZ_m']//img[@alt='Scan me!']").get_attribute("src")
            image=driver.find_element_by_tag_name("img").get_attribute("src")
            #urllib.request.urlretrieve(image,"I:\\xampp\\htdocs\\\images\\"+str(17)+".jpg")
          
            continue
        except(NoSuchElementException,AttributeError):
            continue
        
    return image




def index(request):
    image=bar_code()
    return render(request,"magic/home.html",{"src":image})





























    
    