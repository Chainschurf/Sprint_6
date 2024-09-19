from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_AREA = By.XPATH, "//div[@id='accordion__heading-7']" # Локатор для области с вопросами
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']/parent::div" # Локатор для вопроса
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']" # Локатор для ответа
    COOKIE_BUTTON = By.XPATH, "//button[@id='rcc-confirm-button']" # Локатор для кнопки принятия кук
    SAMOKAT_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]" # Локатор для логотипа "Самоката"
    YANDEX_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]" # Локатор для логотипа "Яндекс"

