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


def indexx(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('E:\Rudy\Developments\sensus\magic\client_secret.json', scope)
    client = gspread.authorize(creds)
    driver = webdriver.Chrome(options=options,executable_path="E:\Rudy\Developments\sensus\magic\chromedriver.exe")
    driver.get('https://web.whatsapp.com/')
    messages=[]
    numbers=[]
    time_slot=[]
    sheet = client.open("test").sheet1


    for i in range(10,13):
        number = sheet.cell(i,1).value
        numbers.append(number)
        message=sheet.cell(i,2).value
        messages.append(message)
        times=sheet.cell(i,5).value
        time_slot.append(times)


    var=3
    check=len(messages)
    col=5
    row=3

    curTime=datetime.datetime.now()
    curHour=curTime.time().hour
    curMin=str(curTime.time().minute)

    for i in range(0,4):
        time.sleep(2)
        driver.get("https://wa.me/"+"91"+numbers[i])
        send=driver.find_element_by_id("action-button")
        send.click()
        #time.sleep(20)
        #time_check=str(time_slot[i])
        #if(time_check[0]==curHour and time_check[2]==curMin[0] and time_check[3]==curMin[1]):
        while check>0:
            try:

                msg_box = driver.find_element_by_class_name('_2S1VP')
                time.sleep(56)
                msg_box.send_keys(messages[i])
                button = driver.find_element_by_class_name('_35EW6')
                button.click()
                time.sleep(4)
                sheet.update_cell(var,11,"YES")
                if(curHour>=12):
                    time_now=str(curHour)+":"+str(curMin)+"PM"
                    sheet.update_cell(row,col,time_now)
                else:
                    time_now=str(curHour)+":"+str(curMin)+"AM"
                    sheet.update_cell(row,col,time_now)
                row+=1
                
                break
            except (NoSuchElementException,WebDriverException,UnexpectedAlertPresentException):
                print("not connected...trying again")
            
    
        
        var+=1
        check-=1
        time.sleep(1)

    messages_list=[]
    col=7
    row=3


    for r in range(0,4):
        col=7
        messages_list.clear()
        driver.get("https://wa.me/"+"91"+numbers[r])
        send=driver.find_element_by_id("action-button")
        send.click()
        time.sleep(20)
        msg_box = driver.find_element_by_class_name('_2S1VP')
        msg_box.click()
        messages = driver.find_elements_by_xpath('//*[@class="_3_7SH _3DFk6 message-in tail"]//span[@dir="ltr"]')

        for a in range(0,len(messages)):
            messages_list.append(messages[a].text)

        if(len(messages_list)>=4):
            for k in range(len(messages_list)-4,len(messages_list)):
                sheet.update_cell(row,col,messages_list[k])
                col+=1
                
        else:
            continue
            

        row+=1   
    
        time.sleep(2)




    row=3
    col=6
    last_message=[]



    for r in range(0,4):
        driver.get("https://wa.me/"+"91"+numbers[r])
        send=driver.find_element_by_id("action-button")
        send.click()
        time.sleep(20)
        last_message.clear()
        if(curHour>=12):
            time_now=str(curHour)+":"+str(curMin)+"PM"
            sheet.update_cell(row,col,time_now)
        else:
            time_now=str(curHour)+":"+str(curMin)+"AM"
            sheet.update_cell(row,col,time_now)

        last_message=driver.find_elements_by_xpath('//div[@class="_2f-RV"]//span[@data-icon="msg-dblcheck"]')
        if(last_message[len(last_message)-1].is_displayed()):
            sheet.update_cell(row,12,"YES")
        else:
            sheet.update_cell(row,12,"NO")
        blue_tick=driver.find_elements_by_xpath('//div[@class="_3_7SH _3DFk6 message-out"]//*[@class="_2f-RV"]//*[@class="_32uRw"]//span[@data-icon="msg-dblcheck-ack"]')
        if(len(blue_tick)>0):
                if(blue_tick[len(blue_tick)-1].is_displayed()):
                    sheet.update_cell(row,13,"NO")
                else:
                    sheet.update_cell(row,13,"NO")
        else:
            sheet.update_cell(row,13,"NO")


        row+=1





















    return(request,"magic/home.html")
