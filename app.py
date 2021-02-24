import json
import logging
import pandas
from flask import Flask, abort, jsonify
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


def readcsv(*colonnes):
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
    logging.debug("Utilisation de la fonction hello_world()")
    logging.debug("L'app fonctionne correctement")
    # utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'


def allcountries():
    logging.debug("Utilisation de la fonction allcountries()")
    df = readcsv('Region')
    countries = list(sorted(set(df['Region'].to_list())))
    logging.debug(countries)
    return countries


def bycountry(country):
    logging.debug(f"Utilisation de la fonction bycountry({country.title()})")
    df = readcsv('Region', 'Year', 'Value')
    df = df.loc[df['Region'].isin([country.title()])]
    df = df.sort_values(by='Year', ascending=False)
    res = {}
    res["Country"] = str(df.iloc[0][0])
    res["Year"] = int(df.iloc[0][1])
    res["Emissions"] = float(df.iloc[0][2])
    logging.debug(res)
    return json.dumps(res)


@app.route('/latest_by_country/<country>')
def by_country(country):
    # on veut la valeur la plus récente
    # des emissions totales pour le pays demandé
    logging.debug(f"Utilisation de la fonction by_country({country.title()})")
    if country.title() in allcountries():
        logging.debug(f"Pays demandé : {country.title()}")
        return bycountry(country)
    else:
        logging.warning(f"Le pays {country.title()} n'est pas dans la liste")
        return json.dumps({
            "message": "Le pays choisi n'est pas dans la liste"})
        abort(404)


def allyears():
    logging.debug("Utilisation de la fonction allyears()")
    df = readcsv('Year')
    years = list(sorted(set(df['Year'].to_list())))
    logging.debug(years)
    return years


def byyear(year):
    logging.debug(f"Utilisation de la fonction byyear({year})")
    globalemission = ["Emissions (thousand metric tons of carbon dioxide)"]
    df = readcsv('Year', 'Value', 'Emission')
    df = df.loc[df['Year'].isin([str(year)])]
    df = df.loc[df['Emission'].isin(globalemission)]
    res = {}
    res["Year"] = year
    res["Total"] = round(df['Value'].mean(), 3)
    logging.debug(res)
    return json.dumps(res)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # on cherche la moyenne des émissions
    # totales au niveau mondial pour une année demandée
    logging.debug(f"Utilisation de la fonction average_for_year({year})")
    logging.debug(f"Année demandée : {year}")
    if int(year) in allyears():
        return byyear(year)
    else:
        logging.warning(f"L'année {year} n'est pas dans la liste")
        return json.dumps({
            "message": "L'année choisie n'est pas dans la liste"})
        abort(404)


def bypercapita(country):
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
    return json.dumps(res)


@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Utilisation de la fonction per_capita({country.title()})")
    if country.title() in allcountries():
        logging.debug(f"Pays demandé : {country.title()}")
        return bypercapita(country)
    else:
        logging.warning(f"Le pays {country.title()} n'est pas dans la liste")
        return json.dumps({
            "message": "Le pays choisi n'est pas dans la liste"})
        abort(404)


if __name__ == "__main__":
    app.config.update(
        ENV="development"
    )
    app.run(debug=True)
