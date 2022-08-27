from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pymysql

while True:
    try:
        conexao = pymysql.connect(host='localhost',
                                  database='meubd',
                                  user='root',
                                  password='senha')
        cursor = conexao.cursor()

        options = Options()  # ficar invisivel
        options.headless = False
        driver = webdriver.Chrome(ChromeDriverManager().install())
        wait = WebDriverWait(driver, 60)

        url = "https://blaze.com/pt/games/crash"
        driver.get(url)
        crashes = []
        sleep(2)
        while True:
            crash = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/span[1]").text
            crash = crash.replace('X', '')
            print(crash)
            #subir crash pro banco de dados
            sql = f"INSERT INTO meubd.crash (crash, dt_consulta) VALUES ({crash}, now())"
            print(sql)
            cursor.execute(sql)
            conexao.commit()

            while True:
                crash2 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/span[1]").text
                crash2 = crash2.replace('X', '')
                if crash2 == crash:
                    sleep(1)
                else:
                    break
    except Exception as erro:
        print(erro)
