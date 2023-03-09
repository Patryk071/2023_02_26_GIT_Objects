import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Otwiera przeglądarkę i przenosi na wskazaną stronę www
driver.get("https://www.google.pl")
print("Jesteś w środku kodu")

# Musimy znaleźć id przycisku "akceptuj" i skąd bierzemy nazwę
buttonAccept = driver.find_element("id", "L2AGLb")
buttonAccept.click()

# Zapis bez biblioteki selenium.webdriver.common.by import By
#searchInput = driver.find_element("name", "q")

# Zapis z biblioteką selenium.webdriver.common.by import By
searchInput = driver.find_element(By.NAME, "q")

searchInput.send_keys("Aktualna pogoda w Krakowie")

## Po wpisaniu zapytania o pogodę możemy kliknąć "wyszukaj", czyli "btnK"
# buttonSearch = driver.find_element("name", "btnK")
# buttonSearch.submit()

# lub możemy zasymuwać wciśnięcie ENTERA
# aby wcisnąć ENTER musimy zaimportować selenium.webdriver.common.keys import Keys
searchInput.send_keys(Keys.ENTER)

# Zapisanie screenshota z ekranu chrome
driver.get_screenshot_as_file("Screen_z_ekranu.png")

time.sleep(5)
print("Jesteś na końcu kodu")

# Zamyka przeglądarkę
driver.quit()