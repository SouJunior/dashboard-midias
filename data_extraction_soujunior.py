from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#----------------------------------------------------------------------------
# Login to linkedin
#----------------------------------------------------------------------------

### load selenium driver
service = Service('chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://linkedin.com/')
sleep(2)

### find username_id and input the email
username = driver.find_element(By.NAME,'session_key')
username.send_keys('seuemaildecadastronolinkedin')

### find password_id and input the password
password = driver.find_element(By.ID,'session_password')
password.send_keys('senhadolinkedin')

### click the login button
login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")
login_btn.click()
sleep(4)

# Store the ID of the original window
original_window = driver.current_window_handle

#----------------------------------------------------------------------------
# Visitors Download
#----------------------------------------------------------------------------

### Open a new tab and switches to new tab - compagny_page
driver.switch_to.new_window('tab')
driver.get('https://www.linkedin.com/company/82326952/admin/analytics/visitors/')
sleep(5)

### open the calendar
open_calendar = driver.find_element(By.CLASS_NAME,'ph2')
open_calendar.click()
sleep(2)

### close the calendar (apenas para a continuação do teste, porque não consegui interagir com o drop-down menu)
close_calendar = driver.find_element(By.CLASS_NAME,'ph2')
close_calendar.click()
sleep(2)

### select "Personalizado"

#personalizado = driver.find_elementent(By. , '')
#personalizado.click()
#sleep(6)

### select the days

### click the "Atualizar" button

### click the export button
export_btn = driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--primary']")
export_btn.send_keys(Keys.ENTER)
sleep(5)
### Como clicar em "exportar" da tela que aparece? (ver interação com pop-up)

#----------------------------------------------------------------------------
# Followers Download
#----------------------------------------------------------------------------

### Open a new tab and switches to new tab - compagny_page
driver.switch_to.new_window('tab')
driver.get('https://www.linkedin.com/company/82326952/admin/analytics/followers/')
sleep(5)

### open the calendar
open_calendar = driver.find_element(By.CLASS_NAME,'ph2')
open_calendar.click()
sleep(2)

### close the calendar (apenas para a continuação do teste, porque não consegui interagir com o drop-down menu)
close_calendar = driver.find_element(By.CLASS_NAME,'ph2')
close_calendar.click()
sleep(2)

### select "Personalizado"

#personalizado = driver.find_elementent(By. , '')
#personalizado.click()
#sleep(6)

### select the days

### click the "Atualizar" button

### click on the export button
export_btn = driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--primary']")
export_btn.send_keys(Keys.ENTER)
sleep(5)

#Como clicar em "exportar" da tela que aparece? (ver interação com pop-up)

#----------------------------------------------------------------------------
# Contents Download
#----------------------------------------------------------------------------

### Open a new tab and switches to new tab - compagny_page
driver.switch_to.new_window('tab')
driver.get('https://www.linkedin.com/company/82326952/admin/analytics/updates/')
sleep(2)

### open the calendar
open_calendar = driver.find_element(By.CLASS_NAME,'ph2')
open_calendar.click()
sleep(2)

### close the calendar (apenas para a continuação do teste, porque não consegui interagir com o drop-down menu)
close_calendar = driver.find_element(By.CLASS_NAME,'ph2')
close_calendar.click()
sleep(2)

### select "Personalizado"

#personalizado = driver.find_elementent(By. , '')
#personalizado.click()
#sleep(6)

### select the days

### click the "Atualizar" button

### click the export button
export_btn = driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--primary']")
export_btn.send_keys(Keys.ENTER)
sleep(5)

#Como clicar em "exportar" da tela que aparece? (ver interação com pop-up)

#----------------------------------------------------------------------------
# Quit all tabs
#----------------------------------------------------------------------------
### Back to the original_window and quit
driver.switch_to.window(original_window)
sleep(2)
driver.quit()