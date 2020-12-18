from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger('Selenium - Scenario2')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('Uruchamiamy przeglądarkę')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
logger.info('Wchodzimy na stronę www.upc.pl')
driver.get("https://www.upc.pl/")

logger.info('Podajemy naszą lokalizację')
driver.find_element_by_xpath("//div[@id='homecenter-rfs-template-id']//input").send_keys('Gdańsk' + (Keys.TAB) + 'Pawia' + (Keys.TAB) + '2A' + (Keys.ENTER))

logger.info('Wybór pakietu')
driver.find_element_by_xpath("//span[text()='Internet']").click()

logger.info('WYbór okresu umowy')
driver.find_element_by_xpath("//span[text()='krótka umowa']").click()

logger.info('Wyswietlenie dodatkowych uslug')
# //h4[contains(@class, 'title option__title')]
DodatkoweUslugi = driver.find_elements_by_xpath("//h4[contains(@class, 'title option__title')]")
Uslugi = [Usluga.get_attribute("textContent") for Usluga in DodatkoweUslugi]
for nazwa in Uslugi:
    print("Nazwa uslugi: " + nazwa)

logger.info('Zamykamy przeglądarkę')
driver.close()



