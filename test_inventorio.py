import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.order(2)
def test_inventorio():

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

        assert driver.title == "Swag Labs"
        print("\nSeccion correcta.")
        
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Se encontraron {len(productos)} productos.")
        assert len(productos)==6
        print("Verificacion de productos exitosa.")
    
        primer_producto=driver.find_element(By.CSS_SELECTOR,".inventory_list .inventory_item_name")
        assert primer_producto.text == "Sauce Labs Backpack"
        print("Nombre del primer producto correcto.")
    
        primer_producto_precio=driver.find_element(By.CSS_SELECTOR,".inventory_list .inventory_item_price")
        assert primer_producto_precio.text == "$29.99"
        print("Precio del primer producto correcto.")
        
        menu =driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()
        
        filtro =driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()
        
    finally:
        driver.quit()