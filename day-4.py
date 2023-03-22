from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class sauceDemoTest:
    # username ve password alanlarının boş bırakılması durumu.
    def notEnteredUsernameAndPassword(self): #

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        sleep(1)

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Username is required" == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(5)

    # sadece username alanının doldurulması password alanının boş bırakılması durumu.
    def notEnteredPassword(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")

        sleep(1)
        
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        username.send_keys("abc")
        
        sleep(1)

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Password is required" == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(5)
    # kilitlenmiş bir hesabın sisteme giriş yaparken karşılaştığı sonuç.
    def lockedUser(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")

        sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce")

        sleep(1)

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Sorry, this user has been locked out." == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(1)
    # username ve password kutucuklarının yanında çıkan uyarı mesajını kapatma durumu.
    def ıcon(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        
        sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        errorIcon = driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()

        sleep(5)

    # sisteme giriş yapıldığı takdirde yönlendirilen sayfayı görme durumu.
    def redirectToSite(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("standard_user") 
        password.send_keys("secret_sauce") 

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        link = driver.current_url
        if "/inventory.html" in link:
            print("Doğru sayfadasınız.")

        sleep(5)
       
        
    # bir üstteki fonksiyon sonucu açılan sayfada kaç adet ürün olduğunu gösteren durum.  
    def NumberOfProducts(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")

        username.send_keys("standard_user") 
        password.send_keys("secret_sauce") 

        lgnButton = driver.find_element(By.ID, "login-button")
        lgnButton.click()

        sleep(1)

        listOfProduct = driver.find_elements(By.CLASS_NAME, "inventory_item") 

        print(f"Toplam Ürün Sayısı: {len(listOfProduct)}")

        sleep(5)



test1 = sauceDemoTest()
test1.notEnteredUsernameAndPassword()

test2 = sauceDemoTest()
test2.notEnteredPassword()

test3 = sauceDemoTest()
test3.lockedUser()

test4 = sauceDemoTest()
test4.ıcon()

test5 = sauceDemoTest()
test5.redirectToSite()

test6 = sauceDemoTest()
test6.NumberOfProducts()