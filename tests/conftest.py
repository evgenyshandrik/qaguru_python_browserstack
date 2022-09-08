"""
Configuration test
"""
import os
import pytest
from dotenv import load_dotenv
from appium import webdriver
from datetime import date


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


def create_driver(func) -> webdriver:
    """
    Create driver
    """
    USER = os.getenv('LOGIN')
    KEY = os.getenv('KEY')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')

    desired_cap = {
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "os_version": "9.0",
        "platformName": "android",
        "project": "Python project",
        "build": "browserstack-build-" + str(date.today()),
        "name": func.__name__.capitalize().replace('_', ' ')
    }

    return webdriver.Remote(
        command_executor=f"http://{USER}:{KEY}@{APPIUM_BROWSERSTACK}/wd/hub",
        desired_capabilities=desired_cap
    )
