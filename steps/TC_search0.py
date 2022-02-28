from behave import *
from BDDCommon.CommonSteps.stepscommon import *
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@when('I select a valid departing date')
def select_departing_date(context):
    today = date.today().strftime('%d %B %Y')
    date_from = '//*[@id="app"]/div/section[1]/div[3]/div/div[1]/div/div/input'
    context.browser.find_element_by_xpath(date_from).send_keys(today)
    #cancel datepicker hack --no-work
    #webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()

@when('I select a valid returning date')
def select_returning_date(context):
    date_return = '//*[@id="app"]/div/section[1]/div[3]/div/div[2]/div/div/input'
    tomorrow = (date.today() + timedelta(days=1)).strftime('%d %B %Y')
    context.browser.find_element_by_xpath(date_return).send_keys(tomorrow)
    #cancel datepicker hack--no-work
    #webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()


@when('I select valid quantity adults')
def select_qty_adults(context):
    input_adults = '//*[@id="app"]/div/section[1]/div[3]/div/div[3]/div/input'
    context.browser.find_element_by_xpath(input_adults).click()
    context.browser.find_element_by_xpath('//*[@id="app"]/div/section[1]/div[3]/div/div[3]/ul/li[3]').click()
    #context.browser.find_element_by_xpath(input_adults).send_keys("2")
    
@when('I click on select destination')
def click_destination(context):
    btn_destination = '//*[@id="app"]/div/section[1]/div[4]/button'
    context.browser.find_element_by_xpath(btn_destination).click()
        
@then('I should find planets cards')
def find_planets_cards(context):
    card_planets = '//*[@id="app"]/div/section[2]/div[5]/div/div'
    context.browser.find_element_by_xpath(card_planets)