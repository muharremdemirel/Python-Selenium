from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Demo:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
         self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_empty_username_password(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"))
 
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        errorMassage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMassage.text == "Epic sadface: Username is required"
        


    @pytest.mark.parametrize("username,password",[("standard_user","qwert")])
    
    def test__password(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
      
        errorMassage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMassage.text == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])   
    def test_locked_user(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
       
        errorMassage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMassage.text == "Epic sadface: Sorry, this user has been locked out."


    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_page(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert True


    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_inventory_page(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_number_of_products(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        products=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{password}.png")
        assert 6 == len(products)


    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_error_icon(self,username,password):

        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
    
        closeBtn=self.driver.find_element(By.CLASS_NAME,"error-button")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        closeBtn.click()
        assert 0 == len(self.driver.find_elements(By.CLASS_NAME,"error_icon"))

    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_add(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))
        addInput=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        addInput.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-{username}-{password}.png")
        shopping_cart_badge=self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        assert 1 == int(shopping_cart_badge)

        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_remove(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))
        addInput=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        addInput.click()

        self.waitForElementVisible((By.ID,"remove-sauce-labs-fleece-jacket"))
        removeInptut=self.driver.find_element(By.ID,"remove-sauce-labs-fleece-jacket")
        removeInptut.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-remove-{username}-{password}.png")
        try:
            shopping_cart_badge = self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

        except:
            assert True

    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_product_detail(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()   
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[1]/div"))
        detailInput=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[1]/div")
        detailInput.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-product-detail-{username}-{password}.png")


    def waitForElementVisible(self,locator,timeout=10):
     WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))    