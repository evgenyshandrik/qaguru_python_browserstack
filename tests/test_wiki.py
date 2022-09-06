"""
Test wiki app
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import create_driver
from util.attachment import add_video


@allure.tag('mobile')
@allure.description('Test search form')
def test_search():
    """
    Testing search form
    """
    driver = create_driver(test_search)

    search_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys("BrowserStack")
    search_results = driver.find_elements_by_class_name("android.widget.TextView")

    assert len(search_results) > 0

    add_video(driver.session_id, 'Video steps of test')

    driver.quit()
