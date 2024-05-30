# Generated by Django 5.0.1 on 2024-05-30 22:29

from django.db import migrations

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import random

def llenar_datos_por_defecto(apps, schema_editor):
    Property = apps.get_model('properties', 'Property')
    User = apps.get_model('users', 'User')
    
    owner = User.objects.first()
    
    browser = uc. Chrome()
    url = "https://www.idealista.com/pro/engel-volkers-madrid/"
    browser. get(url)
    browser.implicitly_wait(10)
    browser. find_element(
        "xpath", '//*[@id="didomi-notice-agree-button"]').click()
    html = browser.page_source

    soup = bs(html, 'lxml')

    articles = soup.find('main', {'class': 'listing-items'}).find_all('article')

    # print(articles)

    id_muebles = [article.get('data-element-id') for article in articles]

    print(id_muebles)

    list_ = list()

    browser.close()
    # id_muebles = ['101738996', '103565392', '101184519', '102848914', '104554565', '104174540', '102711209', '103163793', '102321942', '102729947', '101183612', '102385625', '104746718', '104418575', '102703404', '103960809', '102961447', '97799867', '103199813', '104983034', '101981389', '103247149', '104325413', '104322460', '103338590', '97029619', '102685558', '104524789', '103719012', '104789403']

    id_muebles = id_muebles[:3]

    for idDepartament in id_muebles:
        
        browser = uc. Chrome()
        departamentUrl = f"https://www.idealista.com/pro/engel-volkers-madrid/inmueble/{idDepartament}"
        
        browser.get(departamentUrl)
        browser.implicitly_wait(2)
        browser.find_element ("xpath",'//*[@id="didomi-notice-agree-button"]').click()
        html = browser.page_source
        
        soup = bs(html, 'lxml')
        
        title = soup.find('span', {'class':'main-info__title-main'}).text
        location = soup.find('span', {'class': 'main-info__title-minor'}).text.split(',')[0]
        price = soup.find('span', {'class': 'txt-bold'}).text.replace('.', '')
        print('title, location, price',title, location, price)
        
        c1 = soup.find('div', {'class': 'details-property'}).find('div', {'class': 'details-property-feature-one'})
        
        # print(c1)
        
        characteristics = [caract.text.strip() for caract in c1.find_all('li')]
        
        print(characteristics)
        
        c2 = soup.find('div', {'id': 'headerMap'})
        
        ubication = [zona.text.strip() for zona in c2.find_all('li')]
        
        list_.append({
            'title': title,
            'price': float(price),
            'location': location,
            'description': ", ".join(characteristics),
            'street': ubication[0],
            'colony': ubication[2],
            'city': ubication[1],
            'postal_code': str(random.randint(100000, 999999)),
            # 'type': random.choice(['Casa', 'Departamento'])
        })

        browser.close()
        # print(ubication)

    print(list_)

    # Ingresa los datos por defecto
    for property in list_:
        Property.objects.create(
            description=property['description'],
            street=property['street'],
            colony=property['colony'],
            city=property['city'],
            postal_code=property['postal_code'],
            price=property['price'],
            type= random.choice((('house', "Casa"),('deparment', "Departamento"),('land', "Terreno"),)),
            owner=owner
            # Ingresa otros campos según tus necesidades
        )

class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_property_thumbnail'),
    ]

    operations = [
        migrations.RunPython(llenar_datos_por_defecto),
    ]
