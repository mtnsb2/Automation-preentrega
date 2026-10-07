import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.order(3)
def test_carrito():

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
      
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
      
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

        carrito_validacion_cantidad= driver.find_elements(By.CSS_SELECTOR,"div.cart_list .cart_item")
        assert len(carrito_validacion_cantidad) == 2
        print("\nAdicion de productos al carrito correcta.")
    
        carrito_validacion_nombre=driver.find_elements(By.CSS_SELECTOR,"div.cart_list .inventory_item_name")
        productos_carrito_lista = [items.text for items in carrito_validacion_nombre]
        assert "Sauce Labs Backpack" in productos_carrito_lista
        assert "Sauce Labs Bike Light" in productos_carrito_lista
        print("Funcionalidad de carrito exitosa.")
    
    finally:
           driver.quit()