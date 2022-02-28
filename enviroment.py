from selenium import webdriver
import os


def before_feature(context,feature):  
    context.driver = webdriver.Chrome(os.getenv('PATH_BROWSER')) #Defino el path para chrome

def after_feature(context, feature):  #Cierre al finalizar cada feature
    context.driver.quit()
