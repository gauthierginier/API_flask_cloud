import json
import logging
import pandas
from flask import Flask, abort
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


def readcsv(*colonnes):
    return pandas.read_csv(
        'data.csv',
        header=2,
        names=[
            'id',
            'Region',
            'Year',
            'Emission',
            'Value',
            'footnote',
            'source'],
        usecols=colonnes)


@app.route('/')
def hello_world():
    # utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'


def allcountries():
    df = readcsv('Region')
    countries = list(set(df['Region'].to_list()))
    return countries


def bycountry(country):
    df = readcsv('Region', 'Year', 'Value')
    df = df.loc[df['Region'].isin([country.title()])]
    df = df.sort_values(by='Year', ascending=False)
    res = {}
    res["country"] = str(df.iloc[0][0])
    res["year"] = int(df.iloc[0][1])
    res["emissions"] = float(df.iloc[0][2])
    return json.dumps(res)


@app.route('/latest_by_country/<country>')
def by_country(country):
    # on veut la valeur la plus récente
    # des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    if country.title() in allcountries():
        return bycountry(country)
    else:
        return json.dumps({
            "message": "Le pays choisi n'est pas dans la liste"})
        abort(404)


def allyears():
    df = readcsv('Year')
    years = list(set(df['Year'].to_list()))
    return years


def byyear(year):
    print("On est dans la fonction")
    globalemission = ["Emissions (thousand metric tons of carbon dioxide)"]
    df = readcsv('Year', 'Value', 'Emission')
    df = df.loc[df['Year'].isin([str(year)])]
    df = df.loc[df['Emission'].isin(globalemission)]
    print(df['Value'].mean())
    res = {}
    res["Year"] = year
    res["Total"] = df['Value'].mean()
    return json.dumps(res)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # on cherche la moyenne des émissions
    # totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    if int(year) in allyears():
        return byyear(year)
        # return jsonify({"year":"1975", "total":12333555.9})
    else:
        return json.dumps({
            "message": "L'année choisie n'est pas dans la liste"})
        abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    return None
    # if country.lower() == "albania":
    #     return json.dumps({1975:4338.334, 1985 : 6929.926, 1995 : 1848.549, 2005:3825.184, 2015:3824.801, 2016:3674.183, 2017:4342.011})
    # else:
    #     #erreur 404 si on demande un pays qui n'est pas connu
    #     abort(404)


if __name__ == "__main__":
    app.run(debug=True)
