from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import modules.daycap as daycap
import modules.cookiesfilter as cookiesfilter
import configs 


quarta_feira_d = daycap.cap_description_day()
quarta_feira_c = daycap.cap_calendar_day()

driver = webdriver.Chrome()
driver.get("https://streamyard.com/")

cookies = cookiesfilter.extract_name_and_value(configs.export_cookies)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
driver.maximize_window()
sleep(4)

# Abrir Agendamento #
for titulo in configs.titles:

    liveStream_button = driver.find_element(By.XPATH, "//button[contains(.,'Transmissão ao vivo')]")
    liveStream_button.click()

    channel_button =driver.find_element(By.XPATH,  "(//input[@type='checkbox'])[21]")
    channel_button.click()

    # Inserindo Informações #

    t_button = driver.find_element(By.XPATH, "//fieldset/div/div/input")
    t_button.click()
    t_button.send_keys(titulo)
    sleep(1)
    d_button = driver.find_element(By.XPATH, "//div/textarea")
    d_button.click()
    d_button.send_keys(f"Tratamento Espiritual {quarta_feira_d}")

    p_button = driver.find_element(By.XPATH, "//select")
    privacy = Select(p_button)
    privacy.select_by_value(configs.visibility[1])

    set_d_button = driver.find_element(By.XPATH, "//label[contains(.,'Agendar para depois')]")
    set_d_button.click()
    calendar_button = driver.find_element(By.XPATH, "//span/div/div/input")
    calendar_button.click()
    day_c_button = driver.find_element(By.XPATH, f"//button[contains(.,'{quarta_feira_c}')]")
    day_c_button.click()

    h_button = driver.find_element(By.XPATH, "//div[2]/div/div/select")
    hours = Select(h_button)
    hours.select_by_visible_text(configs.hours)

    m_button = driver.find_element(By.XPATH, "//div[3]/div/div/select")
    minutes = Select(m_button)
    minutes.select_by_visible_text(configs.minutes)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(f"/home/user/Documents/Dev/dir/thumbs/{configs.titles.index(titulo) + 1}.png")
    sleep(5)
    s_thumb = driver.find_element(By.XPATH, "//button[contains(.,'Aplicar')]")
    s_thumb.click()
    agendar = driver.find_element(By.XPATH, "//button[contains(.,'Criar transmissão ao vivo')]")
    agendar.click()
    sleep(30)

driver.quit()
