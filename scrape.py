from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import datetime
# from selenium.webdriver.common.by import by
# from bs4 import BeautifulSoup as bs
import pandas as pd
import zipfile
import pdfkit
import shutil
import time
import json
# import glob
import os

print("here!")


driver = webdriver.Chrome(executable_path = "/home/hbaier/Desktop/hnd_scrape/chromedriver")


# for pagina in range(1, 1749):

for pagina in range(35, 1749):

    print(pagina)

    # try:

    url = f"http://estadisticas.se.gob.hn/see/busqueda.php?pagina={str(pagina)}"

    driver.get(url)

    time.sleep(2)

    school_ids = []
    table = driver.find_element_by_xpath("//table[@class='listado']")
    for row in table.find_elements_by_xpath(".//tr[@class='normal_s']"):
        # print([td for td in row.find_elements_by_xpath(".//td")])
        info = [td.text for td in row.find_elements_by_xpath(".//td")]
        school_ids.append(info[1])

    # print(school_ids)

    inputs = driver.find_elements_by_xpath("//input[@name='centro_seleccionado']")
    inputs = [inp.get_attribute('value') for inp in inputs]

    # print(inputs)

    for index in range(len(inputs)):
        with open("id_refs.txt", "a") as f:
            f.write(str(inputs[index]) + " " + str(school_ids[index]) + "\n")

    for inp in inputs:

        try:

            driver.get(f"http://estadisticas.se.gob.hn/see/centro_educativo.php?id={inp}")
            time.sleep(2)
            boleta_input = driver.find_element_by_xpath("//input[@id='check_0']")
            # print(boleta_input.get_attribute('value'))
            pdfkit.from_url(f"http://estadisticas.se.gob.hn/see/boleta_basica_p7_mostrar.php?id={boleta_input.get_attribute('value')}", f'pdfs2/school_{inp}.pdf')

        except:

            pass

driver.quit()
