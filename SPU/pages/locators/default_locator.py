"""DefaultPage Locator module"""
from calvin.core import Locator
from selenium.webdriver.common.by import By

class DefaultPageLocators:
    """
    Include your locator description here
    """
    # LOCATOR_NAME =       Locator(By.METHOD_TO_SEARCH,'ATTRIBUTE_OF_ELEMENT_TO_SEARCH')
    BOTON_INGRESAR = Locator(By.XPATH, "//strong[contains(.,'Ingresar')]")
    NOMBRE_USUARIO = Locator(By.XPATH, "//input[@id='ctl00_CtrlMenuPortal_logIn_txtUsername_txtTextBox']")
    CONTRASENIA_USUARIO = Locator(By.XPATH, "//input[@id='ctl00_CtrlMenuPortal_logIn_txtPassword_txtTextBox']")
    CONFIRMAR_INGRESO = Locator(By.XPATH, "//input[@id='ctl00_CtrlMenuPortal_logIn_btnIngresar']")