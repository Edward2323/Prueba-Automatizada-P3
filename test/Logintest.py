from selenium.webdriver.common.by import By
import json

def obtener_credenciales(usuario):
    with open("Credenciales.json", "r") as archivo:
        datos = json.load(archivo)
        return datos[usuario]["username"], datos[usuario]["password"]
    

def test_login(driver, user=0):
    if user == 1:
        username, password = obtener_credenciales("usuario_correcto")
    else:
        username, password = obtener_credenciales("usuario_incorrecto")


    textbox_user = driver.find_element(By.ID, "txtNombreUsuario")
    textbox_user.clear()  
    textbox_user.send_keys(username) 

    textbox_pass = driver.find_element(By.ID, "txtContrasena")
    textbox_pass.clear()  
    textbox_pass.send_keys(password)  

    driver.find_element(By.ID, "btnSesion").click()








