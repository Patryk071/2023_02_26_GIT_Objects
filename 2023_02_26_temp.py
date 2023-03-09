import time
from selenium import webdriver

driver = webdriver.Chrome()

# Otwiera przeglądarkę i przenosi na wskazaną stronę www
driver.get("https://www.google.pl")
print("Jesteś w środku kodu")

# Musimy znaleźć id przycisku "akceptuj" i skąd bierzemy nazwę
buttonAccept = driver.find_element("id", "L2AGLb")
buttonAccept.click()

searchInput = driver.find_element("name", "q")
searchInput.send_keys("Aktualna pogoda w Krakowie")

buttonSearch = driver.find_element("name", "btnK")
buttonSearch.submit()

time.sleep(5)
print("Jesteś na końcu kodu")

# Zamyka przeglądarkę
driver.quit()