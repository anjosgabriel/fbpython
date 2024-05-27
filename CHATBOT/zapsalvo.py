from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
# import openai

# api = 'ZtckdvL9zvm4oB8pHJ0dZRSgPhCrO25A'


#######API DO EDITACODIGO##########################################
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

api = requests.get("https://editacodigo.com.br/index/api-whatsapp/ZtckdvL9zvm4oB8pHJ0dZRSgPhCrO25A" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()	

##########################################


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(options=chrome_options2)

driver.get('https://web.whatsapp.com/')


def bot():

    try:
        ######PEGAR A MENSAGEM E CLICAR NELA
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha =  webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()


        ##### LER A NOVA MSG _21Ahp
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e  in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)

        if msg[:1]=='1':
            resposta= 'VC DIGITOU 1'
        else:
            resposta = 'vc digitou algo'

      
        
        #RESPONDE A MSG
        campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
        campo_de_texto.click()
        time.sleep(10)
        campo_de_texto.send_keys(resposta,Keys.ENTER)
        time.sleep(10)    

        #FECHA O CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        

    except:
        print('buscando novas notificações')

while True:

    bot() 
