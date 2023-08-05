import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
import time

TRENDING_URL = 'https://trends.google.com/trends/trendingsearches/realtime?geo=US&hl=en-US&category=t'

#Configuración de selenium para poder acceder a los trends sin ser bloqueados
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_items(driver):
  driver.get(TRENDING_URL)
  T_ITEMS_DIV_TAG = 'feed-item'
  items = driver.find_elements(By.TAG_NAME, T_ITEMS_DIV_TAG)
  return items

#Obtención de la información
def parse_item(item, counter):
  title_CLASS = item.find_element(By.CLASS_NAME, 'title')
  title = title_CLASS.text

  
  source_tag = item.find_element(By.CLASS_NAME, 'source-and-time')
  source = source_tag.text
  
  return{
        'ID': counter,
        'Title:': title,
        'source': source
        }
    
#Formato para el archivo Json
def parse_item_n(items):
  timestamp = datetime.datetime.now().isoformat()
  items_data = [parse_item(item, i + 1) for i, item in enumerate(items[:20])]
  return {
     'Data':{
        'Timestamp ' : timestamp,
        f'Trends {counter}' : items_data
     }
  }

   
  

if __name__ == "__main__":
    counter = 0
    while True:  # Bucle infinito
        counter += 1
        print('Creating Driver')
        driver = get_driver()

        print('Fetching the Trending topics')
        items = get_items(driver)

        print(f'Found {len(items)} items')

        print('parsing the top topics')
        items_data = [parse_item_n(items)]

        print(items_data)

        driver.quit()

        # Cargar datos existentes si el archivo JSON ya existe
        try:
            with open("data.json", "r", encoding="utf-8") as json_file:
                datos_existentes = json.load(json_file)
        except FileNotFoundError:
            datos_existentes = []

        # Combinar datos existentes con nuevos datos
        datos_actualizados = [items_data] + datos_existentes

        print('Saving data to a .json')

        # Decodificar caracteres especiales antes de guardar el JSON
        decoded_datos_actualizados = json.loads(json.dumps(datos_actualizados, ensure_ascii=False))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(decoded_datos_actualizados, json_file, indent=4, ensure_ascii=False)

        # Espera 60 segundos antes de la siguiente actualización
        print('Waiting for 60 seconds before the next update...')
        time.sleep(60)
 
