from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

gen_dict={}
gen_dict['L5'] = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[14]/ul/li[3]/ul/li[3]/span/div[1]/input'
gen_dict['L7'] = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[14]/ul/li[3]/ul/li[2]/span/div[1]/input'
gen_dict['L8'] = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[14]/ul/li[3]/ul/li[1]/span/div[1]/input'


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options)


def download(datalist,general,model):
    browser.get('https://earthexplorer.usgs.gov/')
    #/html/body/div[1]/div[1]/div[1]/div[2]/div[2]  expand
    Datasets=WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]')))
    Datasets.click()
    time.sleep(5)

    Sensor=WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[14]/div')))
    Sensor.click()
    time.sleep(2)

    Sensor_genal=WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[14]/ul/li[3]/div')))
    Sensor_genal.click()
    time.sleep(2)


    choose= WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH, gen_dict[general])))
    choose.click()
    time.sleep(2)


    additional_Criteria=WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]')))
    additional_Criteria.click()
    time.sleep(2)

    landsat_id = WebDriverWait(browser, 150).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/fieldset/form/div[1]/div[1]/div[2]/i')))
    landsat_id.click()
    time.sleep(2)

    num = 0
    for data in datalist:
        landsat_id_input = WebDriverWait(browser, 150).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/fieldset/form/div[1]/'
                                                  'div[2]/div[2]/div[1]/div[1]/input')))
        if(num!=0):
            landsat_id_input.clear()
        landsat_id_input.send_keys(data)
        time.sleep(2)

        results=WebDriverWait(browser, 150).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]')))
        results.click()
        time.sleep(2)

        if(model=='download'):
            download = WebDriverWait(browser, 150).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/form/div[2]/div[2]/div[1]/table/tbody/tr/td/ul/li[5]/div[1]/a[5]/div')))
            download.click()
            time.sleep(2)


            product_options = WebDriverWait(browser, 150).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div[1]/div[2]/div[1]/div[1]/button')))
            product_options.click()
            time.sleep(2)


            download_product = WebDriverWait(browser, 150).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button')))
            download_product.click()
            time.sleep(2)
        if(model=='bulkdownload'):
            download = WebDriverWait(browser, 150).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/form/div[2]/div[2]/div[1]/table/tbody/tr/td/ul/li[5]/div[1]/a[6]/div')))
            download.click()
            time.sleep(2)

        additional_Criteria = WebDriverWait(browser, 150).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]')))
        additional_Criteria.click()
        time.sleep(2)

        num+=1

if __name__ == '__main__':
    txt = open("L5.txt", 'r')
    datalist = txt.readlines()

    # login
    browser.get('https://ers.cr.usgs.gov/login/')
    username = browser.find_element_by_xpath('//input[@name="username"]')
    username.send_keys('')
    password = browser.find_element_by_xpath('//input[@name="password"]')
    password.send_keys('')  # 密码

    dr_buttoon = browser.find_element_by_xpath('//input[@id="loginButton"]').click()
    time.sleep(2)

    download(datalist,'L5','bulkdownload')

