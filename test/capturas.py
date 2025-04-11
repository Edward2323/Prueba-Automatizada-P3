import os

def captura(driver, nombre):
    if not os.path.exists("utils/capturas/{nombre}.png"):
        captura = f"utils/capturas/{nombre}.png"
        driver.save_screenshot(captura)
    