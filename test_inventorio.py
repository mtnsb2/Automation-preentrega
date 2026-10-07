import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.order(2)
def test_inventorio():

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
        print("Menu encontrado.")
        
        filtro =driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()
        print("Filtro encontrado.")
        
    finally:
        driver.quit()