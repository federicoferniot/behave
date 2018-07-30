"""DefaultPage module"""
from calvin.core import BasePage
from pages.locators.default_locator import DefaultPageLocators

class DefaultPage(BasePage):
    """
    Include your page description here
    """
    def loguearse(self, user, passw):
        self.find_element(DefaultPageLocators.BOTON_INGRESAR).click()
        self.find_element(DefaultPageLocators.NOMBRE_USUARIO).value = user
        self.find_element(DefaultPageLocators.CONTRASENIA_USUARIO).value = passw
        self.find_element(DefaultPageLocators.CONFIRMAR_INGRESO).click()