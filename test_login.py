import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.order(1)
def test_login():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver,5)
    try:

        driver.get("https://www.saucedemo.com/")
        
        usuario=wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        contraseña=wait.until(EC.presence_of_element_located((By.ID,"password")))
        boton_login=wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        
        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()
        
        assert driver.current_url=="https://www.saucedemo.com/inventory.html",\
            print("Login fallido,URL no esperada.")
        print("\nLogin correcto.")
        
        header=driver.find_element(By.CLASS_NAME,"app_logo"),\
            print("Validacion de seccion fallida")
        assert header.text == "Swag Labs"
            
        seccion =driver.find_element(By.CLASS_NAME,"title"),\
            print("Validacion de titulo fallida")
        assert seccion.text == "Products"
        print("Verificacion de seccion correcta.")
    finally:
        driver.quit()