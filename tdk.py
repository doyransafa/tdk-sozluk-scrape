import os, time, re, random
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='546800asd',
    database='tdk'
)

tdk = db.cursor()
insert_kelimeler_query = 'INSERT INTO kelimeler (kelime,koken) VALUES (%s, %s)'
insert_anlamlar_query = 'INSERT INTO anlamlar (anlam,kelime_id) VALUES (%s, %s)'


os.environ['PATH'] += r'/Users/safadoyran/Desktop/code/chromedriver_mac64'
driver = webdriver.Chrome()

def loop_through_words(word_list):
    driver.get('https://sozluk.gov.tr/')

    for word in word_list:
        search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'tdk-srch-input')))
        search_box.send_keys(word)
        search_button = driver.find_element(By.ID, 'tdk-search-btn')
        search_button.click()
        time.sleep(random.randint(1,2))
        search_box.clear()
        time.sleep(random.randint(1,2))
        es_sesliler = driver.find_elements(By.CSS_SELECTOR, '[id^="bulunan-gts"]')
        ozellikler = driver.find_elements(By.CSS_SELECTOR, '[id^="ozellikler-gts"]')
        anlamlar = driver.find_elements(By.CSS_SELECTOR, '[id^="anlamlar-gts"]')
        for index, es_sesli in enumerate(es_sesliler):
            if (driver.find_element(By.ID, 'bulunmayan-gts').text): 
                print(f'{word} Not Found!!!')
                with open('/Users/safadoyran/Desktop/code/python/scrape/not_found.txt', 'w') as file:
                    file.write(f'{word}\n')
                    file.close()
            # print(index)
            kelime = ([re.sub(', [^,]+|\([^)]+\)', '', es_sesli.text), ozellikler[index].text])
            # print(re.sub(', [^,]+|\([^)]+\)', '', es_sesli.text))
            # print(ozellikler[index].text)
            tdk.execute(insert_kelimeler_query, kelime)
            kelime_id = tdk.lastrowid
            anlamlar_list = re.findall('(?<!\d)\s*([A-ZİŞÇÜÖ].*?)(?=(?:\s*\d+\.|$))', anlamlar[index].text, flags=re.DOTALL | re.UNICODE)
            anlamlar_tuple_list = [(anlam, kelime_id) for anlam in anlamlar_list]
            # print(anlamlar_tuple_list)
            tdk.executemany(insert_anlamlar_query, anlamlar_tuple_list)
            db.commit()


# wiki_link = 'https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:S%C3%B6zc%C3%BCk_listesi'
def collect_words(link):
    driver.get(link)
    list_of_links = []
    name_of_links = []

    os.mkdir(f'{os.getcwd()}/kelimeler')
    os.chdir('kelimeler')

    linkler = driver.find_elements(By.CSS_SELECTOR, '#mw-content-text > div.mw-parser-output > div > ul > li > a')
    for link in linkler:
        list_of_links.append(link.get_attribute('href'))
        name_of_links.append(link.text)

    for index, link in enumerate(list_of_links):
        with open(f'{name_of_links[index]}.txt', 'w') as file:
            driver.get(link)
            words = driver.find_elements(By.CSS_SELECTOR, '#mw-content-text > div.mw-parser-output > ul > li > a')

            for word in words:
                file.write(f'{word.text}\n')


def read_from_file(file):
    
    with open(file, 'r', encoding='utf8', errors='ignore') as file:
        words = file.read().split('\n')

        loop_through_words(words)        


def read_from_folder(folder_name):

    os.chdir(f'{os.getcwd()}/{folder_name}')
    target_path = os.getcwd()
    file_list = [f for f in os.listdir(target_path) if not f.startswith('.')]
    # Sort the file list by creation time
    sorted_file_list = sorted(file_list, key=lambda x: os.path.getctime(os.path.join(target_path, x)))

    for file in sorted_file_list:
        print(f'-----\nStarted reading file {file} at:{time.time()} \n-----')
        read_from_file(file)
        print(f'-----\nFinished reading file {file} at:{time.time()} \n-----')


read_from_folder('kelimeler')

