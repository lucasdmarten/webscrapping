from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path='./geckodriver')

def openDriver():
    driver.get('https://deriv.com')
    sleep(4)
    login = driver.find_element_by_class_name('button__Button-sc-16zlxpb-1')
    login.click()
def login():
    enterEmail = driver.find_element_by_id('txtEmail')
    email = 'otaviomf123@gmail.com'#input('digite seu email: ')
    enterEmail.send_keys(email)
    enterPass = driver.find_element_by_id('txtPass')
    password = '.BF3ryXn$4J65Ka'#password = getpass.getpass('Password:')
    enterPass.send_keys(password)
    loginEnter = driver.find_element_by_name('login')
    loginEnter.click()
def cleanMessage():
    clickMessage = driver.find_element_by_class_name('notification__cta-button')
    clickMessage.click()
def choicePair():
    choice = driver.find_element_by_class_name('cq-symbol')
    choice.click()
    sleep(8)
    pair="usd/jpy"
    searchPairs = driver.find_element_by_class_name('data-hj-whitelist')
    searchPairs.send_keys(pair)
    sleep(8)
    pairClick = driver.find_element_by_class_name('ic-frxUSDJPY')
    pairClick.click()
def changeToDemo():
    loginInfo = driver.find_element_by_class_name('acc-info')
    loginInfo.click()
    changeToDemo = driver.find_element_by_xpath("//ul/li[2]")
    changeToDemo.click()
    demoOK = driver.find_element_by_class_name('acc-switcher__id')
    demoOK.click()
def changeAmount():
    findInputAmount = \
    driver.find_element_by_xpath("//div[@class='dc-input-wrapper']/input[1]")
    findInputAmount.clear()
    findInputAmount.send_keys('100')
def buy():
    buy =\
     driver.find_element_by_xpath("//button[@id='dt_purchase_multup_button']")
    buy.click()
def sell():
    sell =\
      driver.find_element_by_xpath("//button[@id='dt_purchase_multdown_button']")
    sell.click()
def close():
    close =\
    driver.find_element_by_xpath("//div[@class='dc-contract-card-item__footer']")
    sleep(8)
    close.click()

print('--'*10+'openDriver')
sleep(8)
openDriver()

print('--'*10+'login')
sleep(8)
login()

print('--'*10+'changeToDemo')
sleep(8)
changeToDemo()

print('--'*10+'choicePair')
sleep(8)
choicePair()

print('--'*10+'changeAmount')
sleep(8)
changeAmount()

print('--'*10+'buy')
sleep(8)
buy()

print('--'*10+'sell')
sleep(8)
sell()

print('--'*10+'close')
sleep(8)
close()

print('--'*10+'close')
sleep(8)
close()
