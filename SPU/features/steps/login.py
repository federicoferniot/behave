from behave import *
from calvin.base_test import BaseTest
from pages.page_objects.default_page import DefaultPage


@given('estoy en el home')
def step_impl(context):
    context.baseTest = BaseTest()
    context.baseTest.driver_set_up(context.baseTest.CHROME, "http://10.2.1.56:8190/")
    context.baseTest.driver.maximize_window()


@when('me logueo con usuario gestor')
def step_impl(context):
    context.page = DefaultPage(context.baseTest.driver)
    context.page.loguearse('jsellan', '12345678')


@then('estoy en el escritorio comprador')
def step_impl(context):
    assert('Escritorio' in context.page.url, context.page.url)