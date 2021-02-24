import logging
import json
import pandas
from flask import Flask, abort, jsonify
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


def readcsv(*colonnes):
    """
    Cette fonction permet de lire le fichier csv avec pandas.read_csv(),
    sans prendre ne compte les 2 premières lignes avec header=2,
    renommant chaques colonnes avec names=[],
    et permet d'utiliser les colonnes voulues avec usecols=(colonnes).

    This function reads the csv file with pandas.read_csv(),
    without taking into account the first 2 lines with header=2,
    renaming each column with names=[],
    and allows to use the desired columns with usecols=(columns).
    """
    logging.debug(f"Utilisation de la fonction readcsv({colonnes})")
    logging.info("Lecture du fichier csv")
    return pandas.read_csv(
        'data.csv',
        header=2,
        names=[
            'id',
            'Region',
            'Year',
            'Emission',
            'Value',
            'Footnote',
            'Source'],
        usecols=colonnes)


@app.route('/')
def hello_world():
    """
    Cette fonction permet de vérifier que la route pour l'API
    fonctionne en affichant 'Hello, World!'.

    This function checks that the route for the API
    works by displaying 'Hello, World!.
    ---
    example request for API
    ---
    get: http://localhost:5000/
    result : Hello, World!
      description: print 'Hello, World!'
    """
    logging.debug("Utilisation de la fonction hello_world()")
    logging.debug("L'app fonctionne correctement")
    # utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'


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
    df = df.loc[df['Region'].isin([country.title()])]
    df = df.sort_values(by='Year', ascending=False)
    res = {}
    res["Country"] = str(df.iloc[0][0])
    res["Year"] = int(df.iloc[0][1])
    res["Emissions"] = float(df.iloc[0][2])
    logging.debug(res)
    return jsonify(res)


@app.route('/latest_by_country/<country>')
def by_country(country):
    """
    Cette fonction est utilisé si la route '/latest_by_country/<country>'
    est utilisée.
    Si le pays choisi est dans la liste des pays de la fonction allcountries()
    alors on appel la fonction bycountry()
    Sinon un message d'erreur nous préviens que le pays choisi n'est pas dans
    la liste.

    This function is used if the route '/latest_by_country/<country>' is used.
    is used.
    If the selected country is in the list of countries in the allcountries()
    function then we call the function bycountry()
    Otherwise an error message will warn us that the selected country is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000/latest_by_country/bulgaria
    result : {"Country": "Bulgaria", "Year": 2017, "Emissions": 42819.932}
      description: print the latest entry for total CO2 emissions
    in Thousands of tons.
    """
    # on veut la valeur la plus récente
    # des emissions totales pour le pays demandé
    logging.debug(f"Utilisation de la fonction by_country({country.title()})")
    if country.title() in allcountries():
        logging.debug(f"Pays demandé : {country.title()}")
        return bycountry(country)
    else:
        logging.warning(f"Le pays {country.title()} n'est pas dans la liste")
        return jsonify({
            "message": "Le pays choisi n'est pas dans la liste"})
        abort(404)


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
    df = readcsv('Year')
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
    df = readcsv('Year', 'Value', 'Emission')
    df = df.loc[df['Year'].isin([str(year)])]
    df = df.loc[df['Emission'].isin(globalemission)]
    res = {}
    res["Year"] = year
    res["Total"] = round(df['Value'].mean(), 3)
    logging.debug(res)
    return jsonify(res)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    """
    Cette fonction est utilisé si la route '/average_by_year/<year>'
    est utilisée.
    Si l'année choisie est dans la liste des années de la fonction allyears()
    alors on appel la fonction byyear()
    Sinon un message d'erreur nous préviens que l'année choisie n'est pas dans
    la liste.

    This function is used if the route '/average_by_year/<year>'.
    is used.
    If the chosen year is in the list of years in the allyears() function
    then we call the byyear() function
    Otherwise an error message will warn us that the chosen year is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000/average_by_year/2017
    result : {"Year": "2017", "Total": 219666.446}
      description: print average total CO2 emissions (in Thousands of tons)
    worldwide.
    """
    # on cherche la moyenne des émissions
    # totales au niveau mondial pour une année demandée
    logging.debug(f"Utilisation de la fonction average_for_year({year})")
    logging.debug(f"Année demandée : {year}")
    if int(year) in allyears():
        return byyear(year)
    else:
        logging.warning(f"L'année {year} n'est pas dans la liste")
        return jsonify({
            "message": "L'année choisie n'est pas dans la liste"})
        abort(404)


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
    df = df.loc[df['Region'].isin([country.title()])]
    df = df.loc[df['Emission'].isin(capita)]
    res = {}
    nbannee = len(allyears())
    i = 0
    while i < nbannee:
        res[int(df.iloc[i][1])] = float(df.iloc[i][3])
        i += 1
    logging.debug(res)
    return jsonify(res)


@app.route('/per_capita/<country>')
def per_capita(country):
    """
    Cette fonction est utilisé si la route '/per_capita/<country>'
    est utilisée.
    Si le pays choisi est dans la liste des pays de la fonction allcountries()
    alors on appel la fonction bypercapita()
    Sinon un message d'erreur nous préviens que le pays choisi n'est pas dans
    la liste.

    This function is used if the route '/per_capita/<country>' is used.
    is used.
    If the selected country is in the list of countries in the allcountries()
    function then we call the function bypercapita()
    Otherwise an error message will warn us that the selected country is not in
    the list.
    ---
    example request for API
    ---
    get: http://localhost:5000//per_capita/Morocco
    result : {
        "1975": 0.543,
        "1985": 0.722,
        "1995": 0.963,
        "2005": 1.285,
        "2010": 1.432,
        "2015": 1.591,
        "2016": 1.568,
        "2017": 1.627
        }
      description: print CO2 emissions (in tons per capita)
    in relation to the different survey years.
    """
    logging.debug(f"Utilisation de la fonction per_capita({country.title()})")
    if country.title() in allcountries():
        logging.debug(f"Pays demandé : {country.title()}")
        return bypercapita(country)
    else:
        logging.warning(f"Le pays {country.title()} n'est pas dans la liste")
        return jsonify({
            "message": "Le pays choisi n'est pas dans la liste"})
        abort(404)


if __name__ == "__main__":
    app.config.update(
        ENV="development",
        JSON_SORT_KEYS=False
        )
    app.run(debug=True)
