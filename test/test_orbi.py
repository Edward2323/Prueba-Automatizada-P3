from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import Logintest
import capturas

def test_orbi():

    driver = webdriver.Chrome()

    driver.get("https://orbi.edu.do/orbi/")

    driver.maximize_window()


    Logintest.test_login(driver)


    time.sleep(2)

    capturas.captura(driver, "Login incorrecto")


    Logintest.test_login(driver, 1)

    time.sleep(4)

    capturas.captura(driver, "Login correcto-anuncio")


    time.sleep(3)

    link = driver.find_element(By.LINK_TEXT, "Aceptar")

    time.sleep(3)


    driver.execute_script("arguments[0].scrollIntoView();", link)

    time.sleep(2)

    capturas.captura(driver, "Boton-aceptar-anuncio")

    link.click()

    assert "INICIO" in driver.page_source, "Error al iniciar sesion"

    time.sleep(5)

    capturas.captura(driver, "Inicio")


    link1 = driver.find_element(By.LINK_TEXT, "MI MENÚ")
    link1.click()


    
    time.sleep(2)

    capturas.captura(driver, "Mi menu")

    assert "Gestión Docencia" in driver.page_source, "Error en mi menu"

    driver.find_element(By.LINK_TEXT, "Gestión Docencia").click()

    time.sleep(2)

    capturas.captura(driver, "Gestion-Docencia")


    driver.find_element(By.LINK_TEXT, "Consulta Calificación").click()

    time.sleep(2)

    capturas.captura(driver, "Consulta-Calificacion")


    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, "divInformacionPieL"))

    time.sleep(2)

    capturas.captura(driver, "Calificacion")



    driver.find_element(By.LINK_TEXT, "INICIO").click()

    time.sleep(5)

    link1 = driver.find_element(By.LINK_TEXT, "MI MENÚ").click()

    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Gestión Docencia").click()


    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Histórico Calificación").click()

    time.sleep(2)

    capturas.captura(driver, "Historico-calificacion")


    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, "portlet-content"))

    time.sleep(2)

    capturas.captura(driver, "Historico")


    driver.find_element(By.LINK_TEXT, "INICIO").click()

    time.sleep(5)

    link1 = driver.find_element(By.LINK_TEXT, "MI MENÚ").click()

    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Académico").click()

    time.sleep(2) 

    capturas.captura(driver, "Academico")


    driver.find_element(By.LINK_TEXT, "Auditoria Plan Estudio Estudiante").click()

    time.sleep(2) 

    capturas.captura(driver, "Plan-de-estudios")


    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, "portlet-content"))

    time.sleep(2)

    capturas.captura(driver, "Plan-estudios")

    time.sleep(2) 

    driver.find_element(By.LINK_TEXT, "INICIO").click()

    time.sleep(5)

    link1 = driver.find_element(By.LINK_TEXT, "MI MENÚ").click()

    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Académico").click()

    time.sleep(2) 

    driver.find_element(By.LINK_TEXT, "Consulta Estudiante Línea de Tiempo").click()

    time.sleep(2) 

    capturas.captura(driver, "Consulta Estudiante Línea de Tiempo")


    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.LINK_TEXT, "2023-C-3"))

    time.sleep(1)

    capturas.captura(driver, "Linea de tiempo")

    driver.find_element(By.LINK_TEXT, "2023-C-3").click()

    time.sleep(1)

    capturas.captura(driver, "Linea de tiempo_1")

    time.sleep(2) 

    driver.find_element(By.LINK_TEXT, "INICIO").click()

    time.sleep(5)





    # time.sleep(5)

    driver.quit()