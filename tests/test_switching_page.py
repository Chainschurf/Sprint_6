import allure
from data import Links


class TestSwitchingPage:

    @allure.title("Verify 'Самокат' Logo Redirects to Homepage")
    @allure.description("Verifying that clicking the 'Самокат' logo redirects to the 'Самокат' homepage")
    def test_click_samokat_logo(self, driver, switching_page):
        switching_page.open_order_page()
        switching_page.load_for_whom_page()
        switching_page.click_the_samokat_logo()
        switching_page.load_samokat_window()
        current_url = switching_page.driver.current_url
        expected_url = Links.URL
        assert current_url == expected_url, "URLs are different!"

    @allure.title("Verify 'Yandex' Logo Redirects to 'Дзен' homepage")
    @allure.description("Verifying that clicking the 'Яндекс' logo redirects to the 'Дзен' homepage")
    def test_click_yandex_logo(self, driver, switching_page):
        switching_page.click_the_yandex_logo()
        switching_page.switch_to_new_window()
        switching_page.load_dzen_window()
        current_url = switching_page.driver.current_url
        expected_url = Links.DZEN_URL
        assert current_url == expected_url, "URLs are different!"
