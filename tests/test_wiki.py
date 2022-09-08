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
@allure.title('Test search')
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

    assert len(search_results) > 0, 'List should be more 0'

    add_video(driver.session_id, 'Search Wikipedia')

    driver.quit()


@allure.tag('mobile')
@allure.title('Test hide news')
def test_hide_news():
    """
    Testing hide news
    """
    driver = create_driver(test_hide_news)

    first_block_news = driver.find_elements_by_id("org.wikipedia.alpha:id/view_card_header_title")[0]
    first_header_menu = driver.find_elements_by_id("org.wikipedia.alpha:id/view_list_card_header_menu")[0]
    title_first_block = first_block_news.text

    first_header_menu.click()
    item_menu = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/title")))
    item_menu.click()

    new_first_block_news = driver.find_elements_by_id("org.wikipedia.alpha:id/view_card_header_title")[0]
    title_new_first_block = new_first_block_news.text

    assert title_first_block is not title_new_first_block, 'Titles should be different'

    add_video(driver.session_id, 'Testing hide news')

    driver.quit()
