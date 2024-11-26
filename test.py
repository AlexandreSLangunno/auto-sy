from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta


cookies = (
    { "name": "language", "value": "pt" },)
titulos = ["titulo"]
driver = webdriver.Chrome()
driver.get("https://streamyard.com/")
thumb_path = ""
def qf_d():
    hoje = datetime.now()
    dia_da_semana = hoje.weekday()
    diferenca = 2 - dia_da_semana

    if diferenca <= 0:
        diferenca += 7


    quarta_feira = hoje + timedelta(days=diferenca)
    data_formatada = quarta_feira.strftime("%d/%m/%Y")
    
    return data_formatada


def qf_c():
    hoje = datetime.now()
    dia_da_semana = hoje.weekday()
    diferenca = 2 - dia_da_semana

    if diferenca <= 0:
        diferenca += 7


    quarta_feira = hoje + timedelta(days=diferenca)
    data_formatada = quarta_feira.strftime("%d")
    
    return data_formatada


quarta_feira_d = qf_d()
quarta_feira_c = qf_c()

for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
driver.maximize_window()
sleep(4)

# Abrir Agendamento #

liveStream_button = driver.find_element(By.XPATH, "//button[contains(.,'Transmissão ao vivo')]")
liveStream_button.click()


#channel_button = driver.find_element(By.XPATH, f"//input[@aria-label='{channel_name}']")
#for channel in channel_button:
#    channel.click()

channel_button =driver.find_element(By.XPATH,  "(//input[@type='checkbox'])[21]")
channel_button.click()

# Inserindo Informações #

t_button = driver.find_element(By.XPATH, "//fieldset/div/div/input")
t_button.click()
t_button.send_keys(titulos[0])

d_button = driver.find_element(By.XPATH, "//textarea")
d_button.click()
d_button.send_keys(f"Descrição {quarta_feira_d}")

p_button = driver.find_element(By.XPATH, "//select")
privacy = Select(p_button)
privacy.select_by_value('unlisted')

set_d_button = driver.find_element(By.XPATH, "//label[contains(.,'Agendar para depois')]")
set_d_button.click()
calendar_button = driver.find_element(By.XPATH, "//span/div/div/input")
calendar_button.click()
q_c_button = driver.find_element(By.XPATH, f"//button[contains(.,'{quarta_feira_c}')]")
q_c_button.click()

h_button = driver.find_element(By.XPATH, "//div[2]/div/div/select")
hours = Select(h_button)
hours.select_by_visible_text('19')

m_button = driver.find_element(By.XPATH, "//div[3]/div/div/select")
minutes = Select(m_button)
minutes.select_by_visible_text('45')

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(thumb_path)
sleep(2)
s_thumb = driver.find_element(By.XPATH, "//button[contains(.,'Aplicar')]")
s_thumb.click()
agendar = driver.find_element(By.XPATH, "//button[contains(.,'Criar transmissão ao vivo')]")
agendar.click()

driver.quit()

# Inserir dados #
