import logging
import numpy as np
import pycountry_convert as pc
from statistics import mean
from readcsv_o import readcsv


def allcountries():
    """
    Cette fonction permet de réduire la liste des pays en supprimant
    les doublons avec set() et de les classer
    par ordre croissant avec sorted().
    On retrouve chaque pays du fichier dans une liste.

    This function allows you to reduce the list of countries by deleting
    the duplicates with set() and to sort them
    in ascending order with sorted().
    Each country in the file is found in a list.
    """
    logging.debug("Utilisation de la fonction allcountries()")
    df = readcsv('Region')
    countries = list(sorted(set(df['Region'].to_list())))
    logging.debug(countries)
    return countries


def bycountry(country):
    """
    Cette fonction permet, en fonction du pays choisi, de récupérer
    l'entrée la plus récente concernant l'émission totale de CO2
    en Milliers de tonnes.

    This function allows, depending on the chosen country, to retrieve
    the most recent entry for total CO2 emissions
    in Thousands of tons.
    """
    logging.debug(f"Utilisation de la fonction bycountry({country.title()})")
    df = readcsv('Region', 'Year', 'Value')
    df = df.loc[df['Region'].isin([country])]
    df = df.sort_values(by='Year', ascending=False)
    res = {}
    res["Country"] = str(df.iloc[0][0]).title()
    res["Year"] = int(df.iloc[0][1])
    res["Emissions"] = float(df.iloc[0][2])
    logging.debug(res)
    return res


def allyears():
    """
    Cette fonction permet de réduire la liste des années en supprimant
    les doublons avec set() et de les classer
    par ordre croissant avec sorted().
    On retrouve chaque année du fichier dans une liste.

    This function allows you to reduce the list of years by deleting
    the duplicates with set() and to sort them
    in ascending order with sorted().
    Each year of the file can be found in a list.
    """
    logging.debug("Utilisation de la fonction allyears()")
    df = readcsv('Year', 'Region')
    years = list(sorted(set(df['Year'].to_list())))
    logging.debug(years)
    return years


def byyear(year):
    """
    Cette fonction permet, en fonction de l'année choisi, de récupérer
    la moyenne des émission totales de CO2 (en Milliers de tonnes)
    au niveau mondial.

    This function allows, depending on the chosen year, to retrieve
    average total CO2 emissions (in Thousands of tons)
    worldwide.
    """
    logging.debug(f"Utilisation de la fonction byyear({year})")
    globalemission = ["Emissions (thousand metric tons of carbon dioxide)"]
    df = readcsv('Year', 'Value', 'Emission', 'Region')
    df = df.loc[df['Year'].isin([str(year)])]
    df = df.loc[df['Emission'].isin(globalemission)]
    res = {}
    res["Year"] = year
    res["Total"] = round(df['Value'].mean(), 3)
    logging.debug(res)
    return res


def bypercapita(country):
    """
    Cette fonction permet, en fonction du pays choisi,
    d'afficher les émissions de CO2 (en tonnes par habitant)
    par rapport aux différentes années de relevés.

    This function allows, depending on the chosen country,
    display CO2 emissions (in tons per capita)
    in relation to the different survey years.
    """
    logging.debug(f"Utilisation de la fonction bypercapita({country.title()})")
    capita = ["Emissions per capita (metric tons of carbon dioxide)"]
    df = readcsv('Region', 'Year', 'Emission', 'Value')
    df = df.loc[df['Region'].isin([country])]
    df = df.loc[df['Emission'].isin(capita)]
    res = {}
    nbannee = len(allyears())
    i = 0
    while i < nbannee:
        res[int(df.iloc[i][1])] = float(df.iloc[i][3])
        i += 1
    logging.debug(res)
    return res


def allcontinent():
    all_continent = [
        "Europe",
        "Asia",
        "Africa",
        "North America",
        "South America",
        "Oceania",
        "Antartic"
        ]
    return all_continent


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(
        country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(
        country_continent_code)
    return country_continent_name


europe = []
asia = []
africa = []
north_america = []
south_america = []
oceania = []
antartica = []
continent = {}


def nom_continent(country_name):
    try:
        if country_name.title() == 'Kosovo':
            europe.append(country_name)
            continent["Europe"] = europe
        elif country_name.title() == 'Bosnia And Herzegovina':
            europe.append(country_name)
            continent["Europe"] = europe
        elif country_name.title() == 'Republic Of Moldova':
            europe.append(country_name)
            continent["Europe"] = europe
        elif country_name.title() == 'Trinidad And Tobago':
            south_america.append(country_name)
            continent["South America"] = south_america
        elif country_name.title() == 'United States Of America':
            north_america.append(country_name)
            continent["North America"] = north_america
        elif country_to_continent(country_name.title()) == "Europe":
            europe.append(country_name)
            continent["Europe"] = europe
        elif country_to_continent(country_name.title()) == "Asia":
            asia.append(country_name)
            continent["Asia"] = asia
        elif country_to_continent(country_name.title()) == "Africa":
            africa.append(country_name)
            continent["Africa"] = africa
        elif country_to_continent(country_name.title()) == "North America":
            north_america.append(country_name)
            continent["North America"] = north_america
        elif country_to_continent(country_name.title()) == "South America":
            south_america.append(country_name)
            continent["South America"] = south_america
        elif country_to_continent(country_name.title()) == "Oceania":
            oceania.append(country_name)
            continent["Oceania"] = oceania
        elif country_to_continent(country_name.title()) == "Antartic":
            antartica.append(country_name)
            continent["Antartic"] = antartica
        else:
            print("Hey BOUG, il y a peut etre un problème")
    except KeyError as e:
        print(f"{e} Tiens tu as une erreur ici aussi")


def percontinents():
    for country_name in allcountries():
        nom_continent(country_name)
    return continent


def bycontinent(continents):
    """
    Fonction qui permet d'afficher la moyenne de CO2 pour un continent
    """
    dfmoy = []
    for country in percontinents()[continents]:
        df = readcsv('Region', 'Year', 'Value', 'Emission')
        df = df.loc[df['Region'].isin([country])]
        df = df.sort_values(by='Year', ascending=False)
        dfyear = df.iloc[0][1]
        df = df.iloc[0][3]
        if isinstance(df, np.float):
            dfmoy.append(df)
            moy = mean(dfmoy)
    res = {}
    res["Continent"] = str(continents)
    res["Year"] = int(dfyear)
    res["Emissions"] = float(moy)
    logging.debug(res)
    return res
