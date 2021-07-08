from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

host = "https://localhost.com"

def register(driver):
  # Initial page: Change password page
  wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
  inputs = driver.find_elements_by_xpath("//input[@type='password']")

  for input in inputs:
    input.send_keys("123456asdfgh")

  checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
  checkboxes[1].click()

  driver.find_element_by_xpath("//button[@type='submit']").click()

  # Initial page: Set the URL
  print("Step: Initial page: Set the URL")
  time.sleep(2)
  wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
  driver.find_element_by_xpath("//button[@type='submit']").click()

def login(driver):
  wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login-username-local'  ]")))
  inputs = driver.find_elements_by_xpath("//input[@id='login-username-local']")
  for input in inputs:
    input.send_keys("admin")

  inputs = driver.find_elements_by_xpath("//input[@type='password']")

  for input in inputs:
    input.send_keys("123456asdfgh")

  driver.find_element_by_xpath("//button[@type='submit']").click()

  time.sleep(2)

def click_on_whats_new_close(driver):
  #Click on close button of Whats new
  try:
    driver.find_element_by_xpath("/html/body/div[8]/div/div/div/button").click()
  except Exception:
    pass
  
def add_cluster(driver):
  driver.get("%s/g/clusters/add/select" % host)

def add_cluster_custom(driver):
  driver.get("%s/g/clusters/add/launch/custom" % host)

def go_dashboard(driver):
  driver.get("https://localhost.com/dashboard/c/local")
  time.sleep(2)
  wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Cluster Explorer')]")))

def create_deployment(driver):
  name = "deploy" + str(random.randint(0, 500000))
  driver.get("https://localhost.com/dashboard/c/local/explorer/apps.deployment/create")
  time.sleep(5)
  driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/section/form/div[1]/div[1]/div/div/div[1]/div[1]/div/div[2]/input").send_keys(name)
  driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/section/form/div[1]/div[3]/div/section[1]/div[1]/div[2]/div[1]/div/input").send_keys("alpine")
  driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/section/form/div[1]/div[3]/div/section[1]/div[5]/div/div[1]/div[2]/div/input").send_keys("/bin/ash -c sleep 100000000")
  driver.find_element_by_xpath("//*[text()='Create']").click()
  time.sleep(2)
  driver.find_element_by_xpath("// a[contains(text(),name)]")

if __name__ == '__main__' :
  opt = webdriver.FirefoxOptions()
  # options.addArguments("--headless", "--window-size=1920,1200", "--ignore-certificate-errors");
  # options.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true)
  opt.add_argument("--disable-web-security")
  opt.add_argument("--allow-running-insecure-content")
  opt.add_argument("--accept_untrusted_certs")

  # options.setCapability(CapabilityType.ACCEPT_INSECURE_CERTS, true)

  driver = webdriver.Firefox(options=opt)
  wait=WebDriverWait(driver, 5)
  driver.get(host)
  time.sleep(5)
  assert "Rancher" in driver.title

  # Are we in the register page?
  needs_register = False
  try:
    e = driver.find_element_by_xpath("//*[text()='Terms and Conditions']")
    needs_register = True
  except Exception:
    pass

  # Register or login
  if needs_register:
    register(driver)
  else:
    login(driver)

  click_on_whats_new_close(driver)
  # add_cluster_custom(driver)

  go_dashboard(driver)
  create_deployment(driver)
 
  # # Cluster Dashboard page
  # print("Step: Cluster cluster definition")
  # driver.get("https://localhost/c/local/monitoring")
  # time.sleep(2)
  

  time.sleep(20)

  driver.close()