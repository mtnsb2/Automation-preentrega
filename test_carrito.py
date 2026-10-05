import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.order(3)
def test_carrito():

    driver = webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        usuario=driver.find_element(By.ID,"user-name")
        contraseña=driver.find_element(By.ID,"password")
        boton_login=driver.find_element(By.ID,"login-button")
        
        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()
        time.sleep(3)
        
        
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
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